import os # for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference
import googlemaps
from datetime import datetime
import pdb
from server import * 

def add_trip_to_session():
    """This helper function adds the trip id to the session"""
    
    session["trip_id"]  = trip_id

    db.session.add(trip_id)
    db.session.commit()

    return redirect("/") #trip_id

def start_oAuth(end_location, end_lat, end_lng, activity_types):
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
    print "\n\n\n\n", payload
    #type dict

    yelp_dict = {}
    # params = {}
    params[] =

    for a in activity_types:

        r = requests.get("https://api.yelp.com/v3/businesses/search?location=%scll=%s,%s&limit=5&term=%s", headers=payload, params= % (end_location, end_lat, end_lng, a)) #& connects parameters 
        yelp_dict["activity"[a]] = r.json

    pdb.set_trace()
    return yelp_results


# def whats_near(end_lat, end_lng, activity_types):
#     """Makes a call to Google Places API and returns a json object of the results"""
#     key = os.environ.get('KEY_KEY')
#     places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" #&key=SERVER_KEY
#     radar_places_url = "https://maps.googleapis.com/maps/api/place/radarsearch/json" #have to add radius, this is producing an invalid request check the docs 

    
#     activity_feedback = []

#     # for loop to go through each activity and add it as a request to the Google Places API
#     for a in activity_types:
#         # have the type specific to the iterating variable 
#         r = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s,%s&open_now=True&types=%s" % (key, end_lat, end_lng, a))
#         json_activity = r.json()
#         activity_feedback.append(json_activity)
#         import pdb; pdb.set_trace()

#     # return the compiled API calls for the activities the user requested
#     return activity_feedback 

# # Make a function to get the place details from the place ids still doesn't include the name of the place 
# def retrieve_place_details(place_id):
#     """Given json results, find the place details"""

#     key = os.environ.get('KEY_KEY')
#     retrieve_place_details = ("https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s" % (place_id, key))

# # Have the user choose a place to visit from the json
# def parse_activity_feedback(place_id):
#     """Input parameter is the json object and this function parses out the name and lat lng of the place in a dict"""
    
#     activity_feedback_details = {}
#     activity_feedback.split()

#     # Use .values()
#     place_location = ["results"][0] # location has the keys lat lng
#     place_name = ["results"][3] # check that this is the location name
#     place_activity_type = ["results"][10] # check that this is the activity_type

#     #add to the dictionary THIS MIGHT BE REPETITIVE
#     activity_feedback["activity_place"] = place_name, place_location, place_activity_type
#     # will want to present to the user place details along their route
#     # might need to filter this to be inbetween their start and end latlngs

# # geocoding by place name from Google Maps lecture 


# # #waypoints are stops between two destinations!
# # https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# # #need to find code for the user's current location 

# # # function that takes the json dictionary and takes the information needed for 