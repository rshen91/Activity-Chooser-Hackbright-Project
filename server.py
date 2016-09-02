import os 
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
import geocoder
from datetime import datetime
from model import db, connect_to_db, Trip, Preference, TripPreference
import json
import googlemaps

app = Flask(__name__)

app.secret_key = "ABC"

@app.route('/')
def homepage():
    """Show the homepage to the user."""

    # Returns a unicode list of the human readable names
    names = db.session.query(Preference.name).all()
    return render_template("homepage.html", names=names)


@app.route('/activity_time', methods=['POST']) 
def get_form_values():
    """ Get the variables from the homepage""" 

    ################FORM VARIABLES##############################################
    end_location = request.form["end_location"] 
    arrival_time = request.form["arrival_time"]

    activity_types = request.form.getlist("activity_type") 
    # print "\n\n\n\n\n\n", activity_types
    #Get the user's location from the hidden form in the homepage.html
    user_lat = request.form.get("user_lat") 
    user_lng = request.form.get("user_lng")
    activity_location_preference = request.form["activity_location_preference"] 
    # it's a string
    
    #user's current address based on lat lngs
    s = requests.get("https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(user_lat, user_lng, os.environ['KEY_KEY']))
    start_location = s.json()['results'][0]['formatted_address']

    ###############GETTTING LAT LNGS FOR END ADDRESS############################
    # gives the lat/lng for the address the user inputs in the homepage
    r = geocoder.google(end_location)
     
    # unpack the lat lng here for the api call in whats near (can't have a list)
    end_lat, end_lng = r.latlng
    end_lat = str(end_lat)
    end_lng = str(end_lng)

    ##############ADDING THE TRIP TO THE MODEL##################################
    add_trip_to_table(user_lat, user_lng, arrival_time, end_location, end_lat, end_lng)

    # Model.add_preference_to_model(activity_types)

    ##############ACTIVITY YELP API CALL BASED ON LOCATION PREFERENCE###########
    if activity_location_preference == "near_end_location":
        results = start_oAuth(end_location, end_lat, end_lng, activity_types)
    else: # activity_location_preference == "near_user"
        results = start_oAuth(start_location, str(user_lat), str(user_lng), activity_types)
    
    return render_template("choose_activity.html",
                            activity=results,
                            end_location=end_location,
                            start_location=start_location,
                            end_lat=end_lat,
                            end_lng=end_lng,
                            user_lat=user_lat,
                            user_lng=user_lng,
                            activity_types=activity_types) 



@app.route('/choose', methods=['POST'])
def activity_chosen():
    """Get the form variable chosen for the business the user wants in between"""
    
    chosen_phone = request.form.get("business_phone")
    
    # each business has a unique phone number to select information only from the chosen business
    chosen_business = request.form.get("business_name_"+ chosen_phone)
    chosen_business_lat = request.form.get("business_lat_" + chosen_phone) 
    chosen_business_lng = request.form.get("business_lng_" + chosen_phone) 
    chosen_business_rating = request.form.get("business_rating_" + chosen_phone)
    chosen_business_image = request.form.get("business_image_" + chosen_phone)
    chosen_business_url = request.form.get("business_url_"+ chosen_phone)
    chosen_business_street = request.form.get("business_street_" + chosen_phone)
    chosen_business_city = request.form.get("business_city_" + chosen_phone)
    chosen_business_zipcode = request.form.get("business_zipcode_" + chosen_phone)
    
    # variables from hidden text fields in choose_activity.html 
    user_lat = request.form.get("user_lat")
    user_lng = request.form.get("user_lng")
    end_lat = request.form.get("end_lat")
    end_lng = request.form.get("end_lng")
    start_location = request.form.get("start_location")
    end_location = request.form.get("end_location")

    return render_template("final_route.html",
                            business_name=chosen_business,
                            business_rating=chosen_business_rating,
                            activity_lat=chosen_business_lat,
                            activity_lng=chosen_business_lng,
                            business_image=chosen_business_image,
                            business_url=chosen_business_url,
                            business_street=chosen_business_street,
                            business_city=chosen_business_city,
                            business_zipcode=chosen_business_zipcode,
                            user_lat=user_lat,
                            user_lng=user_lng,
                            end_lat=end_lat,
                            end_lng=end_lng,
                            end_location=end_location,
                            start_location=start_location)

    ############## HELPER FUNCTIONS ############################################
def start_oAuth(end_location, end_lat, end_lng, activity_types):
    """Uses oAuth and sends request to Yelp API for activity locations near end location. 

    The function compiles API response in a list of dictionaries, each business is a dictionary
    in the list"""
    
    resp = requests.post("https://api.yelp.com/oauth2/token",
                     data = {'grant_type': 'client_credentials',
                             'client_id': os.environ["app_id"],
                             'client_secret': os.environ["app_secret"]})

    for_get_request = resp.json()
    bearer_buddy = for_get_request["access_token"]


    payload = {'Authorization': 'Bearer '+ bearer_buddy}

    all_businesses = []
    all_businesses_in_activity = []

    # loop over the r.json() to build up the yelp_response dictionary
    for yelp_request in activity_types:
        #for each activity, send an API call to get business details
        r = requests.get("https://api.yelp.com/v3/businesses/search?location={}cll={},{}&limit=5&sort=1&term={}&category_filter={}".format(end_location, end_lat, end_lng, yelp_request, yelp_request), headers=payload)
        # print "\n\n\n\n\n\n\n", r.json()
        all_businesses_in_activity.extend(r.json()['businesses'])
        
        yelp_values = helper_function_api(all_businesses_in_activity)

        all_businesses.extend(yelp_values)
        
        unique_results = remove_duplicate_businesses(all_businesses)

    return unique_results

def helper_function_api(all_businesses_in_activity):
    """Creating a list of dictionaries from the json response in start_oAuth"""
    storing_yelp_values = []

    for business in all_businesses_in_activity:

            business = {
                'name': business.get('name'),
                'coordinates': {'lat': business.get('coordinates').get('latitude'),
                                'lng': business.get('coordinates').get('longitude')},
                'address': business.get('location'),
                'phone': business.get('phone'),
                'rating': business.get('rating'),
                'categories': business.get('categories'),
                'price': business.get('price'),
                'image_url': business.get('image_url'), #this is unicode
                'url' : business.get('url')
                }

            storing_yelp_values.append(business)
    # print "\n\n\n\n\n\n", storing_yelp_values
    return storing_yelp_values

def remove_duplicate_businesses(storing_yelp_values):
    """Helper function to remove duplicate businesses from start_oAuth

    >>> remove_duplicate_businesses([cat, cat, dog, fred])
    [cat, dog, fred]
    """
    
    unique_results = []

    for business in storing_yelp_values:
        if business not in unique_results:
            unique_results.append(business)

    return unique_results  

    ################ MODELS FUNCTION ###########################################       
def add_trip_to_table(user_lat, user_lng, arrival_time, end_location, end_lat, end_lng):
   """Add current trip to Trip table"""

   trip_id = Trip(user_lat=user_lat, user_lng=user_lng, 
                     arrival_time=arrival_time, end_location=end_location, 
                      end_lat=end_lat, end_lng=end_lng)
   db.session.add(trip_id)
   db.session.commit()

# Preference table is populated through sql yelp api file 
# How is TripPreference generated?


if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000