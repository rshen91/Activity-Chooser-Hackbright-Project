import os #for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference

#store trip similar to user in a session
def add_trip_to_session():
    """This helper function adds the trip id to the session"""
    
    session["trip_id"]  = trip_id

    db.session.add(trip_id)
    db.session.commit()

    return trip_id

#function to list through Google places types gas etc. 
# def add_to_activity_list():
#     """Mark which activity types the user selected"""
    
#     activity_lst = []
#     act = Preferences(trip_id, activity_type=activity_type)
#     for act in {{ name.name }}:
#         valued = request.form.get(checkbox)
#         if value:
#             activity_lst.append(act)
#             db.session.add(act)

#     return checkbox, activity_lst


# geocoding by place name from Google Maps lecture 

# function using Google Directions and Google Places API to see from 
# what the user selected if it's along their way and prompt them to confirm 
# activity they want 

# #Google Places API 
# #separate parameters by &
# #os.environ needed for the secrets.sh
# url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
# payload = {'key1': 'value1', 'key2':'value2'} 
# r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?', data=payload)

# #waypoints are stops between two destinations!
# https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# #need to find code for the user's current location 

# # function that takes the json dictionary and takes the information needed for 