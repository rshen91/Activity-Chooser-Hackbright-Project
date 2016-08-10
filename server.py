import os #for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference

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

#each trip will have it's own id and need to be stored in session similarly to user_id for login

#this function will take the variables from the homepage and be used to soon ask the user if they want a direct route
@app.route('/submission', methods= ["POST"])
def variables():
     """ Take the variables from the homepage""" 

     #Get the form variables
     end_location = request.form["end_location"]
     arrival_time = request.form["arrival_time"]
     activity_type = request.form["activity_type"]

     session["trip_id"] = trip.trip_id
     for activity in activity_type:
        act = Preferences(trip_id, activity_type=activity_type)

    # db.session.add(trip_id)
    # db.session.commit()

#function to list through Google places types gas etc. 

#open now doesnt get stored in the db 
#     # user's current_address=
#     # will need to convert the user current location to lat/long for google maps API
#     # geopy https://pypi.python.org/pypi/geopy

# @app.route('direct_or_not.html', methods=["POST"])
# def direct_route():
#     """Show the direct or not choice"""
#     # if direct_reponse == yes:
#     #     return render_template("direct_route.html")
#     # else:
#     #     return render_template("decision_for_activities.html")

# #function to redirect once done with that request?

# #Nina's lightning talk has info about getting json 


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

if __name__ == "__main__":
    # app.run(debug=True)
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5004)