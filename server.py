import os #for the secrets.sh file 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
# from geopy.geocoders import Nominatim
from model import db, connect_to_db, Trip, Preference, TripPreference
import helper_functions

app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Show the homepage to the user.
    
    As a user, I want to see on the homepage the current time, 
    the desired location and the end time. There will also be activity 
    selection in a checklist for me to select. """

    # Returns a unicode list of the human readable names
    names = db.session.query(Preference.name).all()
    
    # flask uses Jinja to fill in the blanks and return a string of HTML
    html = render_template("homepage.html", names=names)

    #flask sends the fully-formed HTML string down the pipes to the front end
    return html

#this function will take the variables from the homepage and be used to soon ask the user if they want a direct route
@app.route('/submission', methods=['POST'])
def variables():
    """ Take the variables from the homepage""" 

    # Get the form variables
    # this is a string
    end_location = request.form["end_location"]
    #this is a string too
    arrival_time = request.form["arrival_time"]
    activity_types = request.form.getlist("activity_type") #tried activity_type and gave an empty list 
    #this needs to be in parantheses because it's a list not a dict.
    print activity_types #prints an empty list

    #store the activity preferences in the database this might need to be on JS like with favorites
    # act_lst= []
    # for activity in activity_type:
    #     act = Preferences(trip_id, activity_type=activity_type)
    #     act_lst.append(act)
    #     db.session.add(act)
  
    # activity_lst = []
    # act = Preference(trip_id, activity_type=activity_type)
    # for act in {{ name.name }}:
    #     valued = request.form.get(checkbox)
    #     if value:
    #         activity_lst.append(act)
    #         db.session.add(act)

    # print act_lst #this prints an empty list
    
    db.session.commit()

    # where do I want this information to go?
    return render_template("direct.html", 
                            end_location=end_location, 
                            arrival_time=arrival_time,
                            activity_types=activity_types)



if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000