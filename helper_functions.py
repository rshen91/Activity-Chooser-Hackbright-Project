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

 #returns one of each activity selected

# def yelp_dict(yelp_response):
#     """Take out the values I want and render to a html template"""

#     yelp_response = json.dumps(yelp_response, ensure_ascii=False)
#     yelp_response_1 = yelp_response.get("activity").get("businesses")
#     for name, phone, coordinates in yelp_response:
#         print name, phone, coordinates
    # yelp_response_2 = yelp_response_1.get("businesses")
