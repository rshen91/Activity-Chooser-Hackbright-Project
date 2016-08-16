import os # for the secrets.sh file?
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
from model import db, connect_to_db, Trip, Preference, TripPreference
from helper_functions import *
import geocoder
import json

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


@app.route('/submission', methods=['POST']) 
# how do you get the variables from a post request without rendering a page
# add to the trip_id table 
def variables():
    """ Get the variables from the homepage""" 

    # Get the form variables
    # this is a string
    end_location = request.form["end_location"]
    #this is a string too
    arrival_time = request.form["arrival_time"]
    #fixed the jinja loop in homepage.html to include the value that will be 
    #sent to the back end and assigned activity_types
    activity_types = request.form.getlist("activity_type") 

    #gives the lat/lng for the address the user inputs in the homepage
    r = geocoder.google(end_location)

    #Get the user's location from the hidden form in the homepage.html
    user_lat = request.form.get("lat") 
    print "\n\n\n\n" + user_lat + "\n\n\n\n"
    user_lng = request.form.get("lng")
    print "\n\n\n\n" + user_lng + "\n\n\n\n"

    db.session.commit()
    
    #right now this is going to direct.html 
    return render_template("/direct.html", 
                        end_location=end_location, 
                        arrival_time=arrival_time,
                        activity_types=activity_types,
                        latlng=r.latlng)

                        # user_lat=user_lat, this is having an issue removed 
                        # from the function so the server can run and can figure out the map
                        # user_lng=user_lng)

    #want to call this from helper_functions.py
    whats_near(end_location, activity_types)

################################################################################
# need to find out what activities are near them based on their location and the end location
# moved to helper function since I dont want it to render a page

    # get the request back from the places_url:
    # places_near_user_dict = json.load(open("whatever the response is .json"))
    # $.get(url, [data] successFunction)
#route to render a direct route html page with a map of the direct route

#render a page with the available activities along their route for them to select


#route to render a route with activities and a map with markers

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000