import os 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
import geocoder
from datetime import datetime
from model import db, connect_to_db, Trip, Preference, TripPreference
import json
import pdb
import googlemaps

app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Show the homepage to the user."""

    # Returns a unicode list of the human readable names
    names = db.session.query(Preference.name).all()

    return render_template("homepage.html", names=names)


@app.route('/activity_time', methods=['POST']) 
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
    #Think about if I need this since it's not carrying over to the final map
    user_lat = request.form.get("user_lat") 
    
    user_lng = request.form.get("user_lng")
    
    #user's current address based on lat lngs
    s = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(user_lat, user_lng, os.environ['KEY_KEY']))
    start_location = s.json()['results'][0]['formatted_address']

    # New trip being added to the Trip table
    trip_id = Trip(user_lat=user_lat, user_lng=user_lng, 
                   arrival_time=arrival_time, end_location=end_location, 
                   end_lat=end_lat, end_lng=end_lng)
    
    db.session.add(trip_id)
    db.session.commit()
    #The API call before the return statement 

    near_end_location_results = start_oAuth(end_location, end_lat, end_lng, activity_types)
    near_user_results = start_oAuth(start_location, user_lat, user_lng, activity_types)
    near_halfway = start_oAuth(, activity_types)
    return render_template("choose_activity.html",
                            activity=results,
                            end_location=end_location,
                            end_lat=end_lat,
                            end_lng=end_lng,
                            user_lat=user_lat,
                            user_lng=user_lng) 

       
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
# FIX ME ONLY ADDS ONE TYPE OF BUSINESS OUT OF EACH BUSINESS TYPE
        for business in all_businesses_in_activities:
            business = {
                'name': business['name'],
                'coordinates': {'lat': business.get('coordinates').get('latitude'),
                                'lng': business.get('coordinates').get('longitude')},
                'address': business.get('location'),
                'phone': business.get('phone'),
                'categories': business['categories']
                }
        
        storing_yelp_values.append(business)
    return storing_yelp_values

def add_preference_to_model(name, yelp_id):
    """From start_oAuth, can add the values to model.py for the user's preference"""
# add the name 
# add the yelp_id
# need to review one to many
    # db.session.commit() 

@app.route('/choose', methods=['POST'])
def activity_chosen():
    """Get the form variable chosen for the business the user wants in between"""

    chosen_phone = request.form.get("business_phone")
    # each business has a unique phone number
    chosen_business = request.form.get("business_name_"+ chosen_phone)
    chosen_business_lat = request.form.get("business_lat_" + chosen_phone) 
    chosen_business_lng = request.form.get("business_lng_" + chosen_phone) 
    print "\n\n\n\n\n\n" + chosen_business
    print "\n\n\n\n\n\n" + chosen_business_lat
    print "\n\n\n\n\n\n" + chosen_business_lng

    end_lat = request.form.get("end_lat")
    print "\n\n\n\n\n\n end_lat", end_lat
    end_lng = request.form.get("end_lng")
    print "\n\n\n\n\n\n end_lng", end_lng
    user_lat = request.form.get("user_lat")
    print "\n\n\n\n\n\n user_lat", user_lat
    user_lng = request.form.get("user_lng")
    print "\n\n\n\n\n\n user_lng", user_lng


    return render_template("final_route.html",
                            business_name=chosen_business,
                            activity_lat=chosen_business_lat,
                            activity_lng=chosen_business_lng,
                            user_lat=user_lat,
                            user_lng=user_lng,
                            end_lat=end_lat,
                            end_lng=end_lng)

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000