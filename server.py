import os #for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference

app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Show the homepage to the user.
    
    As a user, I want to see on the homepage the current time, 
    the desired location and the end time. There will also be activity 
    selection in a checklist for me to select. """

    # Returns a unicode list of the human readable names
    names=db.session.query(Preference.name).all()

    return render_template("homepage.html", names=names)

#this function will take the variables from the homepage and be used to soon ask the user if they want a direct route
@app.route('/submission', methods= ['POST'])
def variables():
    """ Take the variables from the homepage""" 

    #Get the form variables
    end_location = request.form.get["end_location"]
    print end_location
    arrival_time = request.form.get["arrival_time"]
    print arrival_time
    activity_type = request.form.get["activity_type"] #will this be a list in a list?
    print activity_type

    #store trip similar to user in a session
    session["trip_id"] = trip.trip_id
    
    #store the activity preferences in the database
    for activity in activity_type:
        act = Preferences(trip_id, activity_type=activity_type)

    db.session.add(act)
    db.session.add(trip_id)
    # db.session.commit()

#function to list through Google places types gas etc. 

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

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000