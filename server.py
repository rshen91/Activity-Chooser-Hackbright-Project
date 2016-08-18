import os # for the secrets.sh file?
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
import geocoder
from model import db, connect_to_db, Trip, Preference, TripPreference
from helper_functions import *
import json
import pdb


app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Show the homepage to the user.
    
    As a user, I want to see on the homepage the current time, 
    the desired location and the end time. There will also be activity 
    selection in a checklist for me to select. """

    # Returns a unicode list of the human readable names
    names = db.session.query(Preference.name).all()
    # flask uses Jinja to fill in the blanks and return a string of HTML
    #flask sends the fully-formed HTML string down the pipes to the front end
    return render_template("homepage.html", names=names)


@app.route('/activity_time', methods=['POST']) 
# how do you get the variables from a post request without rendering a page
# add to the trip_id table 
def get_form_values():
    """ Get the variables from the homepage""" 

    # Get the form variables
    # this is a string
    end_location = request.form["end_location"]
    print "This is the end location \n\n\n\n\n\n", end_location 
    #this is a string too
    arrival_time = request.form["arrival_time"]
    #fixed the jinja loop in homepage.html to include the value that will be 
    #sent to the back end and assigned activity_types
    activity_types = request.form.getlist("activity_type") 
    print "These are the activity types \n\n\n\n\n", activity_types 

    #gives the lat/lng for the address the user inputs in the homepage
    r = geocoder.google(end_location)
    print "\n\n\n\n this is the  end location as lat lng" , r.latlng, "\n\n\n\n"
    # unpack the lat lng here for the api call in whats near (can't have a list)
    end_lat, end_lng = r.latlng
    # import pdb; pdb.set_trace()

    print "\n\n\n\n"  
    print end_lat
    print "\n\n\n\n" 
    print end_lng
    print "\n\n\n\n"

    #Get the user's location from the hidden form in the homepage.html
    user_lat = request.form.get("lat") 
    print "\n\n\n\n this is the lat from html of user's current loc" + user_lat + "\n\n\n\n"
    user_lng = request.form.get("lng")
    print "\n\n\n\n this is the lng from html of user's current loc" + user_lng + "\n\n\n\n"

    db.session.commit()
    
    #The API call before the return statement 
    start_oAuth(end_location, str(end_lat), str(end_lng), activity_types)

    # whats_near(end_lat, end_lng, activity_types)

    #right now this is going to direct.html 
    return render_template ("/direct.html", 
                        arrival_time=arrival_time,
                        activity_types=activity_types,
                        end_latlng=r.latlng,
                        end_location=end_location)

    #want to call this from helper_functions.py
@app.route('/activity')
def render_activity():
    """Takes the json place name, phone number, address, and displays to user"""

    return render_template("/activity.html")

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000