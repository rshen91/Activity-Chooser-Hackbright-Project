import os #for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
from geopy.geocoders import Nominatim

app = Flask(__name__)

app.secret_key = "ABC"
#request handout for requests library

@app.route('/')
def homepage():
    """Show the homepage to the user.
    
    As a user, I want to see on the homepage the current time, 
    the desired location and the end time. There will also be activity 
    selection in a checklist for me to select. """

    return render_template("homepage.html")

#this function will take the variables from the homepage and be used to soon ask the user if they want a direct route
@app.route('to where the homepage variables lead', methods= ["POST"])
def variables_coordinates():
    """ Take the variables from the homepage""" 
    end_location = request.form("end_location")
    arrival_time = request.form("arrival_time")
    print end_location
        print ((end_location.latitude, end_location.longitude)) # => will this give the lat/long coordinates
    print arrival_time 
    # user's current_address=
    # will need to convert the user current location to lat/long for google maps API
    # geopy https://pypi.python.org/pypi/geopy

@app.route('direct_or_not.html', methods=["POST"])
def direct_route():
    """Show the direct or not choice"""
    # if direct_reponse == yes:
    #     return render_template("direct_route.html")
    # else:
    #     return render_template("decision_for_activities.html")

#function to redirect once done with that request?

#Nina's lightning talk has info about getting json 


#Google Places API 
#separate parameters by &
#os.environ needed for the secrets.sh
url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
payload = {'key1': 'value1', 'key2':'value2'} 
r = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?', data=payload)

#waypoints are stops between two destinations!
https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

#need to find code for the user's current location 

# function that takes the json dictionary and takes the information needed

if __name__ == "__main__":
    app.run(debug=True)
    DebugToolbarExtension(app)
    app.run(host='0.0.0.0', port=5000)