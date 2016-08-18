import os # for the secrets.sh file?
from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
import requests
from model import db, connect_to_db, Trip, Preference, TripPreference
from helper_functions import *
import geocoder
import json
import pdb

app = Flask(__name__)

app.secret_key = "ABC"

# oAuth for version 3 of yelp API, see https://github.com/Yelp/yelp-api-v3/blob/master/docs/tutorials/get-start-yelp-api-v3.md#get-an-access-token
# https://api.yelp.com/oauth2/token
def start_oAuth():
# oAuth comes back with the bearer information and you have to do .json() because it's just a 200 response object
#this goes in your post request
    resp = requests.post("https://api.yelp.com/oauth2/token",
                     data = {'grant_type': 'client_credentials',
                             'client_id': os.environ.get(app_id),
                             'client_secret': os.environ.get(app_secret)})

    for_get_request = resp.json()
    pdb.set_trace()
# Yelp version 3 requires the oAuth in the header

# r = requests.post(https://api.yelp.com/oauth2/token, data=json.dumps(payload), headers=headers)

# Query: 
# https://api.yelp.com/v2/search/?location=683 sutter street san francisco&sort=1&limit=5&category_filter=active,beautysvc,shopping

# "region"
# {
#     "region": {
#         "span": {
#             "latitude_delta": 0.0012685096703393128, 
#             "longitude_delta": 0.00340162597498761
#         }, 
#         "center": {
#             "latitude": 37.788428973466, 
#             "longitude": -122.41098139362501
#         }
#     }, 
#     "total": 40, 
#     "businesses": [
#         {
#             "is_claimed": true, 
#             "rating": 5.0, 
#             "mobile_url": "http://m.yelp.com/biz/last-minute-gear-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "rating_img_url": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/f1def11e4e79/ico/stars/v1/stars_5.png", 
#             "review_count": 118, 
#             # I want the NAME 
#             "name": "Last Minute Gear", 
#             "snippet_image_url": "http://s3-media1.fl.yelpcdn.com/photo/NgqAKCz3FXuXXLHrIY0FXQ/ms.jpg", 
#             "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/c7623205d5cd/ico/stars/v1/stars_small_5.png", 
#             "url": "http://www.yelp.com/biz/last-minute-gear-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "location": {
#                 "city": "San Francisco", 
#                 "display_address": [
#                     "Lower Nob Hill", 
#                     "San Francisco, CA"
#                 ], 
#                 "geo_accuracy": 9.5, 
#                 "neighborhoods": [
#                     "Lower Nob Hill"
#                 ], 
#                 "country_code": "US", 
#                 "address": [],
#                 # I want the coordinates 
#                 "coordinate": {
#                     "latitude": 37.7878523781613, 
#                     "longitude": -122.41252758725
#                 }, 
#                 "state_code": "CA"
#             }, 
#             "phone": "4158131881", 
#             "snippet_text": "Last minute gear saved me while planning for a last minute trip to Yosemite. I rented a bear box from LMG and it was great having the peace of mind knowing...", 
#             "image_url": "https://s3-media4.fl.yelpcdn.com/bphoto/Czsp7ZXZLL7cn0-6eDjhAA/ms.jpg", 
#             "categories": [
#                 [
#                     "Sports Wear", 
#                     "sportswear"
#                 ], 
#                 [
#                     "Outdoor Gear", 
#                     "outdoorgear"
#                 ]
#             ], 
#             "display_phone": "+1-415-813-1881", 
#             "rating_img_url_large": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/22affc4e6c38/ico/stars/v1/stars_large_5.png", 
#             "id": "last-minute-gear-san-francisco", 
#             "is_closed": false, 
#             "distance": 128.05403527495227
#         }, 
#         {
#             "is_claimed": true, 
#             "rating": 5.0, 
#             "mobile_url": "http://m.yelp.com/biz/coco-spa-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "rating_img_url": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/f1def11e4e79/ico/stars/v1/stars_5.png", 
#             "review_count": 42, 
#             "name": "CoCo Spa", 
#             "snippet_image_url": "http://s3-media1.fl.yelpcdn.com/photo/3pCi6IPQl48fUiRD-F834Q/ms.jpg", 
#             "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/c7623205d5cd/ico/stars/v1/stars_small_5.png", 
#             "url": "http://www.yelp.com/biz/coco-spa-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "location": {
#                 "cross_streets": "Powell St & Mason St", 
#                 "city": "San Francisco", 
#                 "display_address": [
#                     "490 Post St", 
#                     "Ste 1701", 
#                     "Union Square", 
#                     "San Francisco, CA 94102"
#                 ], 
#                 "geo_accuracy": 9.5, 
#                 "neighborhoods": [
#                     "Union Square"
#                 ], 
#                 "postal_code": "94102", 
#                 "country_code": "US", 
#                 "address": [
#                     "490 Post St", 
#                     "Ste 1701"
#                 ], 
#                 "coordinate": {
#                     "latitude": 37.7881812, 
#                     "longitude": -122.4098946
#                 }, 
#                 "state_code": "CA"
#             }, 
#             "menu_date_updated": 1471055706, 
#             "phone": "4156598535", 
#             "snippet_text": "You don't go to CoCo Spa to just get a facial - you almost get a mini therapy session plus glowing skin to boot. Both CoCo and Ainsley truly care about...", 
#             "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/7HgchBR4V8oThhEnXRQbEQ/ms.jpg", 
#             "categories": [
#                 [
#                     "Skin Care", 
#                     "skincare"
#                 ], 
#                 [
#                     "Waxing", 
#                     "waxing"
#                 ], 
#                 [
#                     "Cosmetics & Beauty Supply", 
#                     "cosmetics"
#                 ]
#             ], 
#             "display_phone": "+1-415-659-8535", 
#             "rating_img_url_large": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/22affc4e6c38/ico/stars/v1/stars_large_5.png", 
#             "menu_provider": "single_platform", 
#             "id": "coco-spa-san-francisco", 
#             "is_closed": false, 
#             "distance": 150.99212022363798
#         }, 
#         {
#             "is_claimed": true, 
#             "rating": 5.0, 
#             "mobile_url": "http://m.yelp.com/biz/alisha-valverde-medical-skin-aesthetics-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "rating_img_url": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/f1def11e4e79/ico/stars/v1/stars_5.png", 
#             "review_count": 113, 
#             "name": "Alisha Valverde Medical Skin Aesthetics", 
#             "snippet_image_url": "http://s3-media4.fl.yelpcdn.com/photo/tngbwB0Z583akev_uUmVIA/ms.jpg", 
#             "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/c7623205d5cd/ico/stars/v1/stars_small_5.png", 
#             "url": "http://www.yelp.com/biz/alisha-valverde-medical-skin-aesthetics-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "location": {
#                 "cross_streets": "Powell St & Mason St", 
#                 "city": "San Francisco", 
#                 "display_address": [
#                     "490 Post St", 
#                     "Ste 1509", 
#                     "Union Square", 
#                     "San Francisco, CA 94102"
#                 ], 
#                 "geo_accuracy": 8.0, 
#                 "neighborhoods": [
#                     "Union Square"
#                 ], 
#                 "postal_code": "94102", 
#                 "country_code": "US", 
#                 "address": [
#                     "490 Post St", 
#                     "Ste 1509"
#                 ], 
#                 "coordinate": {
#                     "latitude": 37.7884, 
#                     "longitude": -122.40975
#                 }, 
#                 "state_code": "CA"
#             }, 
#             "menu_date_updated": 1441920742, 
#             "phone": "4158473340", 
#             "snippet_text": "Went for my second visit this week! :D\n\nThe way I feel about my skin has been something I struggled with for over half my life now. An amazing truth is that...", 
#             "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/Ax0PcJC0JXhgrmInWxX0XA/ms.jpg", 
#             "categories": [
#                 [
#                     "Skin Care", 
#                     "skincare"
#                 ], 
#                 [
#                     "Cosmetics & Beauty Supply", 
#                     "cosmetics"
#                 ], 
#                 [
#                     "Hair Removal", 
#                     "hairremoval"
#                 ]
#             ], 
#             "display_phone": "+1-415-847-3340", 
#             "rating_img_url_large": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/22affc4e6c38/ico/stars/v1/stars_large_5.png", 
#             "menu_provider": "single_platform", 
#             "id": "alisha-valverde-medical-skin-aesthetics-san-francisco", 
#             "is_closed": false, 
#             "distance": 164.12271640744885
#         }, 
#         {
#             "is_claimed": true, 
#             "rating": 4.5, 
#             "mobile_url": "http://m.yelp.com/biz/follicle-hair-salon-san-francisco-3?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "rating_img_url": "https://s3-media2.fl.yelpcdn.com/assets/2/www/img/99493c12711e/ico/stars/v1/stars_4_half.png", 
#             "review_count": 201, 
#             "name": "Follicle Hair Salon", 
#             "snippet_image_url": "http://s3-media1.fl.yelpcdn.com/photo/YVhlHHgL2StMRFcvRt67Ew/ms.jpg", 
#             "rating_img_url_small": "https://s3-media2.fl.yelpcdn.com/assets/2/www/img/a5221e66bc70/ico/stars/v1/stars_small_4_half.png", 
#             "url": "http://www.yelp.com/biz/follicle-hair-salon-san-francisco-3?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "location": {
#                 "cross_streets": "Mason St & Powell St", 
#                 "city": "San Francisco", 
#                 "display_address": [
#                     "540 Sutter St", 
#                     "Union Square", 
#                     "San Francisco, CA 94102"
#                 ], 
#                 "geo_accuracy": 9.5, 
#                 "neighborhoods": [
#                     "Union Square"
#                 ], 
#                 "postal_code": "94102", 
#                 "country_code": "US", 
#                 "address": [
#                     "540 Sutter St"
#                 ], 
#                 "coordinate": {
#                     "latitude": 37.7890055687707, 
#                     "longitude": -122.409474849701
#                 }, 
#                 "state_code": "CA"
#             }, 
#             "menu_date_updated": 1471152303, 
#             "phone": "4154025277", 
#             "snippet_text": "Marc is the best! I've been getting Brazilian Blowouts/ Keratin Treatments from him for the past year and a half to two years. \nHe always takes great care...", 
#             "image_url": "https://s3-media1.fl.yelpcdn.com/bphoto/H0xJge4n-leGz2d18UKw0g/ms.jpg", 
#             "categories": [
#                 [
#                     "Hair Salons", 
#                     "hair"
#                 ]
#             ], 
#             "display_phone": "+1-415-402-5277", 
#             "rating_img_url_large": "https://s3-media4.fl.yelpcdn.com/assets/2/www/img/9f83790ff7f6/ico/stars/v1/stars_large_4_half.png", 
#             "menu_provider": "single_platform", 
#             "id": "follicle-hair-salon-san-francisco-3", 
#             "is_closed": false, 
#             "distance": 181.76515028317138
#         }, 
#         {
#             "is_claimed": true, 
#             "rating": 5.0, 
#             "mobile_url": "http://m.yelp.com/biz/studio-hix-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "rating_img_url": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/f1def11e4e79/ico/stars/v1/stars_5.png", 
#             "review_count": 27, 
#             "name": "Studio Hix", 
#             "snippet_image_url": "http://s3-media2.fl.yelpcdn.com/photo/MyCW4WLWjnLIWXMH9plm5w/ms.jpg", 
#             "rating_img_url_small": "https://s3-media1.fl.yelpcdn.com/assets/2/www/img/c7623205d5cd/ico/stars/v1/stars_small_5.png", 
#             "url": "http://www.yelp.com/biz/studio-hix-san-francisco?adjust_creative=TMTOAWftgNbJgzlOcMsNIA&utm_campaign=yelp_api&utm_medium=api_v2_search&utm_source=TMTOAWftgNbJgzlOcMsNIA", 
#             "location": {
#                 "cross_streets": "Mason St & Powell St", 
#                 "city": "San Francisco", 
#                 "display_address": [
#                     "555 Sutter St", 
#                     "Ste 401\\406", 
#                     "Union Square", 
#                     "San Francisco, CA 94102"
#                 ], 
#                 "geo_accuracy": 9.5, 
#                 "neighborhoods": [
#                     "Union Square"
#                 ], 
#                 "postal_code": "94102", 
#                 "country_code": "US", 
#                 "address": [
#                     "555 Sutter St", 
#                     "Ste 401\\406"
#                 ], 
#                 "coordinate": {
#                     "latitude": 37.7889874, 
#                     "longitude": -122.4094352
#                 }, 
#                 "state_code": "CA"
#             }, 
#             "phone": "4159896300", 
#             "snippet_text": "I got my hair cut by Meg, and she was awesome!!! I have a ton of hair, most stylists get annoyed just by touching it, b/c there's a ton of it and it takes...", 
#             "image_url": "https://s3-media3.fl.yelpcdn.com/bphoto/eKJD9HtKZOVRFeppfdfzKg/ms.jpg", 
#             "categories": [
#                 [
#                     "Hair Salons", 
#                     "hair"
#                 ]
#             ], 
#             "display_phone": "+1-415-989-6300", 
#             "rating_img_url_large": "https://s3-media3.fl.yelpcdn.com/assets/2/www/img/22affc4e6c38/ico/stars/v1/stars_large_5.png", 
#             "id": "studio-hix-san-francisco", 
#             "is_closed": false, 
#             "distance": 184.77657206019055
#         }
#     ]
# }

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000
