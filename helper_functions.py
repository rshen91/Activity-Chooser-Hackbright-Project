import os # for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference
import googlemaps
from datetime import datetime

    # https://developers.google.com/maps/documentation/geocoding/intro

    # https://maps.googleapis.com/maps/api/geocode/json?address=Winnetka&key=YOUR_API_KEY
    # https://developers.google.com/maps/web-services/client-library
#store trip similar to user in a session
def add_trip_to_session():
    """This helper function adds the trip id to the session"""
    
    session["trip_id"]  = trip_id

    db.session.add(trip_id)
    db.session.commit()

    return redirect("/") #trip_id


# will take in the activity_types, the end_location and the user's current location
# API parameters to see a bubble around it?
def whats_near(end_lat, end_lng, activity_types):
    """Makes a call to Google Places API and returns a json object of the results"""
    key = os.environ.get('KEY_KEY')
    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" #&key=SERVER_KEY
    
    activity_feedback = []

    # for loop to go through each activity and add it as a request to the Google Places API
    for activity in activity_types:
        # have the type specific to the iterating variable 
        r = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s,%s&open_now=True&type=%s" % (key, end_lat, end_lng, activity))
        json_activity = r.json()
        activity_feedback.append(json_activity)

    # return the compiled API calls for the activities the user requested
    return activity_feedback 

# Have the user choose a place to visit from the json
def activity_feedback(activity_feedback):
    """Input parameter is the json object and this function parses out the name and lat lng of the place in a dict"""
    
    activity_feedback_details = {}
    activity_feedback.split()
    # will want to present to the user place details along their route
    # might need to filter this to be inbetween their start and end latlngs

# geocoding by place name from Google Maps lecture 


# #waypoints are stops between two destinations!
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# #need to find code for the user's current location 

# # function that takes the json dictionary and takes the information needed for 