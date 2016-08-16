def convert_address_to_latlong(end_location):
    """"This function takes the user's input for where they want to go and convert_address_to_latlong

    it to latitude and longitude coordinates"""
#     pip install geocoder 

    r = geocoder.google(end_location)
    return r.latlng 


# need a function to convert the end address to lat/long
# http://maps.googleapis.com/maps/api/geocode/json?address="end_location"&key=


# need a function to ask the user if they want a direct route

key = os.environ.get('KEY_KEY') #gets the server key and assigns it to a variable

<!-- <span id="end-location" data-lat="{{ latlng[0] }}" data-long="{{ latlng[1] }}"> </span>
 -->

 https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=AIzaSyAZPdIeAGcyvKhKXgAqaNbsyEz4Sg1qBX4&location=37.7749,122.4194&radius=50000