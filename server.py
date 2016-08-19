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
    end_lat = str(end_lat)
    end_lng = str(end_lng)

    print "\n\n\n\n"  
    print end_lat
    print "\n\n\n\n" 
    print end_lng
    print "\n\n\n\n"

    #Get the user's location from the hidden form in the homepage.html
    user_lat = request.form.get("user_lat") 
    print "\n\n\n\n this is the lat from html of user's current loc" + user_lat + "\n\n\n\n"
    user_lng = request.form.get("user_lng")
    print "\n\n\n\n this is the lng from html of user's current loc" + user_lng + "\n\n\n\n"

    db.session.commit()
    
    #The API call before the return statement 
    return  #app is going here but I want it to go through the start_oAuth function
    
#REMOVED APP.ROUTE HERE BECAUSE THE USER DOESNT NEED TO SEE WHAT THIS FUNCTION DOES    
def start_oAuth(end_location, end_lat, end_lng, activity_types):
    """Uses oAuth and sends request to Yelp API for activity locations near end location"""
# oAuth comes back with the bearer information and you have to do .json() because it's just a 200 response object
#this goes in your post request
    resp = requests.post("https://api.yelp.com/oauth2/token",
                     data = {'grant_type': 'client_credentials',
                             'client_id': os.environ["app_id"],
                             'client_secret': os.environ["app_secret"]})

    #this is a dictionary like json object 
    for_get_request = resp.json()
    bearer_buddy = for_get_request["access_token"]
    #bearer_buddy is a string

    payload = {'Authorization': 'Bearer '+ bearer_buddy}

    storing_yelp_values= []
    all_businesses_in_activities = []

    # loop over the r.json() to build up the yelp_response dictionary
    for yelp_request in activity_types:
        #for each activity, send an API call to get business details
        r = requests.get("https://api.yelp.com/v3/businesses/search?location={}cll={},{}&limit=5&sort=1&term={}&category_filter={}".format(end_location, end_lat, end_lng, yelp_request, yelp_request), headers=payload)
        all_businesses_in_activities.extend(r.json()['businesses'])
            #each of these businesses should be added to the list 
        for business in all_businesses_in_activities:
            # for each business give me the name, coordinates, address and phone number
            # businesses = {}
            business = {
                'name': business['name'],
                'coordinates': {'lat': business.get('coordinates').get('latitude'),
                                'lng': business.get('coordinates').get('longitude')},
                'address': business.get('location'),
                'phone1': business.get('phone'),
                'categories': business['categories']
                }
        storing_yelp_values.append(business)
    # storing_yelp_values 
    return render_template("choose_activity.html",
                            activity=storing_yelp_values,
                            end_location=end_location)


if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000