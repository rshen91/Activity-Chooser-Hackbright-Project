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
key = os.environ.get('browser_key')
#store trip similar to user in a session
def add_trip_to_session():
    """This helper function adds the trip id to the session"""
    
    session["trip_id"]  = trip_id

    db.session.add(trip_id)
    db.session.commit()

    return redirect("/") #trip_id


# will take in the activity_types, the end_location and the user's current location
# API parameters to see a bubble around it?
def whats_near(end_location, activity_types):
    """Hopefully this function will call the Google Places API and return a list(?) 
    of what locations are near the user BUT NOT NECESSARILY BTWN THEIR START/END"""

    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" #&key=SERVER_KEY
    
    search_payload = {"key": key, "location": end_location, "open_now": True, "type": activity_types }
    print search_payload
    r = requests.post(places_url, data=search_payload)
    
    print "\n\n\n\n\n\n\n\ " + r.url #to see what this looks like when it's "ready"
    
    #search_json = search_req.json()
    json_object = r.json() 
    print "\n\n\n\n\n\n\n\ " , json_object
    #see if this gives back lat lngs
    # location_id = search_json["results"][0]["location"]

    return json_object #can splice this up to get the values I want

# Have the user choose a place to visit from the json

# Google Directions API 
def whereto():
    """start with the user's location and get to the first marker?"""

    maps_url = "https://maps.googleapis.com/maps/api/directions/json" #&key=SERVER_KEY

    search_payload = {"origin": user_location, "destination": end_location, "key": key}
    r = requests.post('maps_url', data=search_payload)

    json_object = r.json()
# geocoding by place name from Google Maps lecture 


# #waypoints are stops between two destinations!
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# #need to find code for the user's current location 

# # function that takes the json dictionary and takes the information needed for 