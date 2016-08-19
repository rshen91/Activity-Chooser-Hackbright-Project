import os 
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
    """Show the homepage to the user."""

    # Returns a unicode list of the human readable names
    names = db.session.query(Preference.name).all()

    return render_template("homepage.html", names=names)


@app.route('/activity_time', methods=['POST']) 
# add to the trip_id table 
def get_form_values():
    """ Get the variables from the homepage""" 

    # Get the form variables
    end_location = request.form["end_location"]

    arrival_time = request.form["arrival_time"]

    activity_types = request.form.getlist("activity_type") 

    #gives the lat/lng for the address the user inputs in the homepage
    r = geocoder.google(end_location)
    
    # unpack the lat lng here for the api call in whats near (can't have a list)
    end_lat, end_lng = r.latlng
    end_lat = str(end_lat)
    end_lng = str(end_lng)

    #Get the user's location from the hidden form in the homepage.html
    user_lat = request.form.get("user_lat") 
    
    user_lng = request.form.get("user_lng")
    
    db.session.commit()

    #The API call before the return statement 
    results = start_oAuth(end_location, end_lat, end_lng, activity_types)
    
    return render_template("choose_activity.html",
                            activity=results,
                            end_location=end_location) #app is going here but I want it to go through the start_oAuth function
    
#REMOVED APP.ROUTE HERE BECAUSE THE USER DOESNT NEED TO SEE WHAT THIS FUNCTION DOES    
def start_oAuth(end_location, end_lat, end_lng, activity_types):
    """Uses oAuth and sends request to Yelp API for activity locations near end location. 

    The function compiles API response in a list of dictionaries, each business is a dictionary
    in the list"""

    resp = requests.post("https://api.yelp.com/oauth2/token",
                     data = {'grant_type': 'client_credentials',
                             'client_id': os.environ["app_id"],
                             'client_secret': os.environ["app_secret"]})

    for_get_request = resp.json()
    bearer_buddy = for_get_request["access_token"]


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

            business = {
                'name': business['name'],
                'coordinates': {'lat': business.get('coordinates').get('latitude'),
                                'lng': business.get('coordinates').get('longitude')},
                'address': business.get('location'),
                'phone1': business.get('phone'),
                'categories': business['categories']
                }
        storing_yelp_values.append(business)
    return storing_yelp_values
    


if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000