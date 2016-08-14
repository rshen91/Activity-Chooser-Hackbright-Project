import os # for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference
import googlemaps
from datetime import datetime

# gmaps = google.maps.Client(key=)
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

# need a function to convert the end address to lat/long
# http://maps.googleapis.com/maps/api/geocode/json?address="end_location"&key=

def convert_address_to_latlong(end_location):
    """"This function takes the user's input for where they want to go and convert_address_to_latlong

    it to latitude and longitude coordinates"""
#     pip install geocoder 

    r = geocoder.google(end_location)
    return r.latlng 


# need a function to find the current location of the user
# HTML 5 geolocation?

# need a function to ask the user if they want a direct route



# will take in the activity_types, the end_location and the user's current location
# API parameters to see a bubble around it?
def whats_near(end_location, activity_types):
    """Hopefully this function will call the Google Places API and return a list(?) 
    of what locations are near the user"""

    key = os.environ.get('KEY_KEY') #gets the server key and assigns it to a variable
    places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" #&key=SERVER_KEY
    
    #first api call?
    search_payload = {"key": key, "location": end_location, "radius":1000, "opennow": {{ opennow }}, "type": activity_types }
    r = requests.post('places_url', data=search_payload)
    
    print "\n\n\n\n\n\n\n\ " + r.url #to see what this looks like when it's "ready"
    #search_json = search_req.json()
    json_object = r.json() 
    #see if this gives back lat lngs
    # location_id = search_json["results"][0]["location"]

    return json_object


# geocoding by place name from Google Maps lecture 

# function using Google Directions and Google Places API to see from 
# what the user selected if it's along their way and prompt them to confirm 
# activity they want 

# Google Places API 
# separate parameters by &
# os.environ needed for the secrets.sh
# url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
# payload = {'key1': 'value1', 'key2':'value2'} 
# r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?', data=payload)

# #waypoints are stops between two destinations!
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# #need to find code for the user's current location 

# # function that takes the json dictionary and takes the information needed for 