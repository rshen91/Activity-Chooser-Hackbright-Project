import os 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
from model import db, connect_to_db, Trip, Preference, TripPreference
import googlemaps
import pdb
from server import * 
from pprint import pprint 

def add_trip_to_session():
    """This helper function adds the trip id to the session"""
    
    session["trip_id"]  = trip_id

    db.session.add(trip_id)
    db.session.commit()

    return redirect("/") #trip_id

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
    print "\n\n\n\n This is the payload \n\n\n\n\n", payload
    #type dict

    yelp_response = {} #adding to a list because of TypeError: string indices must be integers, not unicode
    
    #Returns 5 of the first things in the first activity type FIXME: VARIETY
    count = 0
    # loop over the r.json() to build up the yelp_response dictionary
    for yelp_request in activity_types:
            r = requests.get("https://api.yelp.com/v3/businesses/search?location={}cll={},{}&limit=5&sort=1&term={}&category_filter={}".format(end_location, end_lat, end_lng, yelp_request, yelp_request), headers=payload)
            print "\n\n\n\n this the yelp get request \n\n\n", r.json()
            yelp_values = r.json().values()
            print "\n\n\n\n this the yelp get request with .values()\n\n\n", yelp_values
            pdb.set_trace()
            yelp_values = yelp_response[yelp_request] = {
                    'name': yelp_values.get('name'), #list object has no attribute get
                    'coordinates': {'lat': yelp_values['coordinates']['latitude'], 
                                    'lng': yelp_values['coordinates']['longitude']},
                    'address': yelp_values.values('location'), ##how to get out of dictionaries another dictionary and assign it a key
                    'phone': yelp_values.get('phone')
            }
            count += 1
    pdb.set_trace()
    print "\n\n\n\n\n THIS IS THE YELP RESPONSE \n\n\n", yelp_response
    print "\n\n\n\n\n THIS IS THE YELP VALUES \n\n\n", yelp_values
# def yelp_dict(yelp_response):
#     """Take out the values I want and render to a html template"""

#     yelp_response = json.dumps(yelp_response, ensure_ascii=False)
#     yelp_response_1 = yelp_response.get("activity").get("businesses")
#     for name, phone, coordinates in yelp_response:
#         print name, phone, coordinates
    # yelp_response_2 = yelp_response_1.get("businesses")
