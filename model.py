from flask import Flask, session, render_template, request, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import requests

app = Flask(__name__)

app.secret_key = 'ABC'
#figure out how to import Google Maps Directions API and Google Places API Web Service

@app.route('/')
def homepage():
    """Show the homepage to the user.
    As a user, I want to see on the homepage the current time, 
    the desired location and the end time. There will also be activity 
    selection in a checklist for me to select. """

    return render_template("homepage.html")

#this function will take the variables from the homepage and be used to soon ask the user if they want a direct route
@app.route('where the homepage variables lead', methods= ["POST"])
def variables_coordinates():
    end_location = request.form.get("end_location")
    arrival_time = request.form.get("arrival_time")

    

#will need to convert the user current location to lat/long for google maps API
#need to find code for the user's current location 