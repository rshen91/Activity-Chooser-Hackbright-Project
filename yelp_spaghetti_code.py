a = {u'businesses': [{u'categories': [{u'alias': u'coffee',
                                   u'title': u'Coffee & Tea'}],
                  u'coordinates': {u'latitude': 37.782352,
                                   u'longitude': -122.407697},
                  u'id': u'blue-bottle-coffee-co-san-francisco-7',
                  u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/YKoMObZPbtVi1l7f3g4xwg/o.jpg',
                  u'location': {u'address1': u'66 Mint St',
                                u'address2': u'',
                                u'address3': u'',
                                u'city': u'San Francisco',
                                u'country': u'US',
                                u'state': u'CA',
                                u'zip_code': u'94103'},
                  u'name': u'Blue Bottle Coffee Co',
                  u'phone': u'+15106533394',
                  u'price': u'$$',
                  u'rating': 4.0,
                  u'review_count': 1857,
                  u'url': u'https://www.yelp.com/biz/blue-bottle-coffee-co-san-francisco-7'},
                 
                 {u'categories': [{u'alias': u'coffee',
                                   u'title': u'Coffee & Tea'},
                                  {u'alias': u'sandwiches',
                                   u'title': u'Sandwiches'},
                                  {u'alias': u'bagels',
                                   u'title': u'Bagels'}],
                  u'coordinates': {u'latitude': 37.7901517599821,
                                   u'longitude': -122.409288436174},
                  u'id': u'beanstalk-cafe-san-francisco-2',
                  u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/yvw6fgMum8gpS4b4WIFrEA/o.jpg',
                  u'location': {u'address1': u'724 Bush St',
                                u'address2': u'',
                                u'address3': u'',
                                u'city': u'San Francisco',
                                u'country': u'US',
                                u'state': u'CA',
                                u'zip_code': u'94108'},
                  u'name': u'Beanstalk Cafe',
                  u'phone': u'+14155761966',
                  u'price': u'$',
                  u'rating': 4.5,
                  u'review_count': 509,
                  u'url': u'https://www.yelp.com/biz/beanstalk-cafe-san-francisco-2'},
                 
                 {u'categories': [{u'alias': u'coffee',
                                   u'title': u'Coffee & Tea'},
                                  {u'alias': u'sandwiches',
                                   u'title': u'Sandwiches'},
                                  {u'alias': u'vietnamese',
                                   u'title': u'Vietnamese'}],
                  u'coordinates': {u'latitude': 37.79001,
                                   u'longitude': -122.41177},
                  u'id': u'fresh-brew-coffee-san-francisco',
                  u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/G0xDrpOQyXxrrKnQrYm7iQ/o.jpg',
                  u'location': {u'address1': u'882 Bush St',
                                u'address2': u'',
                                u'address3': u'',
                                u'city': u'San Francisco',
                                u'country': u'US',
                                u'state': u'CA',
                                u'zip_code': u'94108'},
                  u'name': u'Fresh Brew Coffee',
                  u'phone': u'+14155670915',
                  u'price': u'$',
                  u'rating': 4.5,
                  u'review_count': 347,
                  u'url': u'https://www.yelp.com/biz/fresh-brew-coffee-san-francisco'},
                 
                 {u'categories': [{u'alias': u'coffee',
                                   u'title': u'Coffee & Tea'}],
                  u'coordinates': {u'latitude': 37.791405,
                                   u'longitude': -122.419327},
                  u'id': u'contraband-coffee-bar-san-francisco',
                  u'image_url': u'http://s3-media4.fl.yelpcdn.com/bphoto/42V-yDiNZcfLFT743jxmPA/o.jpg',
                  u'location': {u'address1': u'1415 Larkin St',
                                u'address2': u'',
                                u'address3': u'',
                                u'city': u'San Francisco',
                                u'country': u'US',
                                u'state': u'CA',
                                u'zip_code': u'94109'},
                  u'name': u'Contraband Coffee Bar',
                  u'phone': u'+14158397388',
                  u'price': u'$$',
                  u'rating': 4.0,
                  u'review_count': 593,
                  u'url': u'https://www.yelp.com/biz/contraband-coffee-bar-san-francisco'},
                 
                 {u'categories': [{u'alias': u'coffee',
                                   u'title': u'Coffee & Tea'}],
                  u'coordinates': {u'latitude': 37.7882923185825,
                                   u'longitude': -122.404029965401},
                  u'id': u'iron-horse-coffee-bar-san-francisco',
                  u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/_eMt3Li_B5DdeAkHFsxIJA/o.jpg',
                  u'location': {u'address1': u'25 Maiden Ln',
                                u'address2': None,
                                u'address3': u'',
                                u'city': u'San Francisco',
                                u'country': u'US',
                                u'state': u'CA',
                                u'zip_code': u'94108'},
                  u'name': u'Iron Horse Coffee Bar',
                  u'price': u'$',
                  u'rating': 4.5,
                  u'review_count': 60,
                  u'url': u'https://www.yelp.com/biz/iron-horse-coffee-bar-san-francisco'}],
 u'total': 4458}

storing_yelp_values= {}
    #Returns 5 of the first things in the first activity type FIXME: VARIETY
    
    # loop over the r.json() to build up the yelp_response dictionary
    for yelp_request in activity_types:
            r = requests.get("https://api.yelp.com/v3/businesses/search?location={}cll={},{}&limit=5&sort=1&term={}&category_filter={}".format(end_location, end_lat, end_lng, yelp_request, yelp_request), headers=payload)
            print "\n\n\n\n this the yelp get request \n\n\n", r.json()
            yelp_values = r.json()['businesses'] #getting to the key/values with the good stuff

            for business in yelp_values:  #go through each business in the json response
                #nesting dictionaries
                storing_yelp_values[name] =  {}
                #setting the key in big dict to the name of the business 
                name = business['name']
                
                # setting the values in name key in big dict
                storing_yelp_values[name]['address'] = business['location']
                storing_yelp_values[name]['coordinates'] = {'lat': business['coordinates']['latitude'], 
                                                            'lng': business['coordinates']['longitude']}
                storing_yelp_values[name]['phone'] = business['phone']

hard coded sort = 1
{'activity': {u'total': 4458, u'businesses': 
[{u'rating': 4.0, u'review_count': 1856, u'name': u'Blue Bottle Coffee Co', u'url': u'https://www.yelp.com/biz/blue-bottle-coffee-co-san-francisco-7', u'price': u'$$', 
u'coordinates': {u'latitude': 37.782352, u'longitude': -122.407697}, u'phone': u'+15106533394', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/YKoMObZPbtVi1l7f3g4xwg/o.jpg', 
u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'66 Mint St', u'zip_code': u'94103'}, u'id': u'blue-bottle-coffee-co-san-francisco-7', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 4.5, u'review_count': 509, u'name': u'Beanstalk Cafe', u'url': u'https://www.yelp.com/biz/beanstalk-cafe-san-francisco-2', u'price': u'$', u'coordinates': {u'latitude': 37.7901517599821, u'longitude': -122.409288436174}, u'phone': u'+14155761966', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/yvw6fgMum8gpS4b4WIFrEA/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'724 Bush St', u'zip_code': u'94108'}, u'id': u'beanstalk-cafe-san-francisco-2', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}, {u'alias': u'bagels', u'title': u'Bagels'}]}, {u'rating': 4.5, u'review_count': 347, u'name': u'Fresh Brew Coffee', u'url': u'https://www.yelp.com/biz/fresh-brew-coffee-san-francisco', u'price': u'$', u'coordinates': {u'latitude': 37.79001, u'longitude': -122.41177}, u'phone': u'+14155670915', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/G0xDrpOQyXxrrKnQrYm7iQ/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'882 Bush St', u'zip_code': u'94108'}, u'id': u'fresh-brew-coffee-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}, {u'alias': u'vietnamese', u'title': u'Vietnamese'}]}, {u'rating': 4.0, u'review_count': 593, u'name': u'Contraband Coffee Bar', u'url': u'https://www.yelp.com/biz/contraband-coffee-bar-san-francisco', u'price': u'$$', u'coordinates': {u'latitude': 37.791405, u'longitude': -122.419327}, u'phone': u'+14158397388', u'image_url': u'http://s3-media4.fl.yelpcdn.com/bphoto/42V-yDiNZcfLFT743jxmPA/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'1415 Larkin St', u'zip_code': u'94109'}, u'id': u'contraband-coffee-bar-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, 
{u'rating': 4.5, u'review_count': 60, u'name': u'Iron Horse Coffee Bar', u'url': u'https://www.yelp.com/biz/iron-horse-coffee-bar-san-francisco', u'price': u'$', u'coordinates': {u'latitude': 37.7882923185825, u'longitude': -122.404029965401}, u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/_eMt3Li_B5DdeAkHFsxIJA/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': None, u'address3': u'', u'state': u'CA', u'address1': u'25 Maiden Ln', u'zip_code': u'94108'}, u'id': u'iron-horse-coffee-bar-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}]}}

changing term to category_filter
{'activity': 
    {u'total': 24875, u'businesses': 
        [{u'rating': 4.5, u'review_count': 337, 
          u'name': u'Tadu Ethiopian Kitchen', u'url': u'https://www.yelp.com/biz/tadu-ethiopian-kitchen-san-francisco-3', u'price': u'$$', 
          u'coordinates': {u'latitude': 37.7847934, u'longitude': -122.4141884}, u'phone': u'+14154096649', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/EapkmG5rpJuy7u8tu01GYA/o.jpg', 
          u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'484 Ellis St', u'zip_code': u'94102'}, u'id': u'tadu-ethiopian-kitchen-san-francisco-3', u'categories': [{u'alias': u'ethiopian', u'title': u'Ethiopian'}]}, {u'rating': 4.5, u'review_count': 938, u'name': u'Liholiho Yacht Club', u'url': u'https://www.yelp.com/biz/liholiho-yacht-club-san-francisco-2', u'price': u'$$$', u'coordinates': {u'latitude': 37.7883678084094, u'longitude': -122.414625026286}, u'phone': u'+14154405446', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/uUkGwA2rrwd24RUjIzWmsw/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'871 Sutter St', u'zip_code': u'94109'}, u'id': u'liholiho-yacht-club-san-francisco-2', u'categories': [{u'alias': u'asianfusion', u'title': u'Asian Fusion'}, {u'alias': u'newamerican', u'title': u'American (New)'}, {u'alias': u'seafood', u'title': u'Seafood'}]}, {u'rating': 4.5, u'review_count': 347, u'name': u'Fresh Brew Coffee', u'url': u'https://www.yelp.com/biz/fresh-brew-coffee-san-francisco', u'price': u'$', u'coordinates': {u'latitude': 37.79001, u'longitude': -122.41177}, u'phone': u'+14155670915', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/G0xDrpOQyXxrrKnQrYm7iQ/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'882 Bush St', u'zip_code': u'94108'}, u'id': u'fresh-brew-coffee-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}, {u'alias': u'vietnamese', u'title': u'Vietnamese'}]}, {u'rating': 4.5, u'review_count': 254, u'name': u"Hooker's Sweet Treats", u'url': u'https://www.yelp.com/biz/hookers-sweet-treats-san-francisco', u'price': u'$$', u'coordinates': {u'latitude': 37.7852285, u'longitude': -122.4160527}, u'phone': u'+14154414628', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/izW5V7ghPnQSf6HCIxvS4Q/o.jpg', u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'442 Hyde St', u'zip_code': u'94109'}, u'id': u'hookers-sweet-treats-san-francisco', u'categories': [{u'alias': u'chocolate', u'title': u'Chocolatiers & Shops'}, {u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 4.5, u'review_count': 153, u'name': u'Tacorea', u'url': u'https://www.yelp.com/biz/tacorea-san-francisco', u'price': u'$', u'coordinates': {u'latitude': 37.7897959388507, u'longitude': -122.410720065236}, u'phone': u'+14158851325', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/TNkHvAH9s6ctXYHG-gNViw/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': None, u'state': u'CA', u'address1': u'809 Bush St', u'zip_code': u'94108'}, u'id': u'tacorea-san-francisco', u'categories': [{u'alias': u'asianfusion', u'title': u'Asian Fusion'}, {u'alias': u'mexican', u'title': u'Mexican'}, {u'alias': u'korean', u'title': u'Korean'}]}]}}

term not category_filter
{'activity': 
    {u'total': 4458, u'businesses': 
            [{u'rating': 4.0, u'review_count': 1855, 
              u'name': u'Blue Bottle Coffee Co', u'url': u'https://www.yelp.com/biz/blue-bottle-coffee-co-san-francisco-7', u'price': u'$$', 
              u'coordinates': {u'latitude': 37.782352, u'longitude': -122.407697}, 
              u'phone': u'+15106533394', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/YKoMObZPbtVi1l7f3g4xwg/o.jpg', 
              u'location': {u'city': u'San Francisco', u'address1': u'66 Mint St', u'address2': u'', u'address3': u'', u'state': u'CA', u'country': u'US', u'zip_code': u'94103'}, 
              u'id': u'blue-bottle-coffee-co-san-francisco-7', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, 

            {u'rating': 4.5, u'review_count': 509, 
            u'name': u'Beanstalk Cafe', u'url': u'https://www.yelp.com/biz/beanstalk-cafe-san-francisco-2', u'price': u'$', 
            u'coordinates': {u'latitude': 37.7901517599821, u'longitude': -122.409288436174}, 
            u'phone': u'+14155761966', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/yvw6fgMum8gpS4b4WIFrEA/o.jpg', 
            u'location': {u'city': u'San Francisco', u'address1': u'724 Bush St', u'address2': u'', u'address3': u'', u'state': u'CA', u'country': u'US', u'zip_code': u'94108'}, 
            u'id': u'beanstalk-cafe-san-francisco-2', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}, {u'alias': u'bagels', u'title': u'Bagels'}]}, 

           {u'rating': 4.5, u'review_count': 347, u'name': u'Fresh Brew Coffee', u'url': u'https://www.yelp.com/biz/fresh-brew-coffee-san-francisco', u'price': u'$', 
            u'coordinates': {u'latitude': 37.79001, u'longitude': -122.41177}, 
            u'phone': u'+14155670915', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/G0xDrpOQyXxrrKnQrYm7iQ/o.jpg', 
            u'location': {u'city': u'San Francisco', u'address1': u'882 Bush St', u'address2': u'', u'address3': u'', u'state': u'CA', u'country': u'US', u'zip_code': u'94108'}, 
            u'id': u'fresh-brew-coffee-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}, {u'alias': u'vietnamese', u'title': u'Vietnamese'}]}, 

           {u'rating': 4.0, u'review_count': 593, u'name': u'Contraband Coffee Bar', u'url': u'https://www.yelp.com/biz/contraband-coffee-bar-san-francisco', u'price': u'$$', 
            u'coordinates': {u'latitude': 37.791405, u'longitude': -122.419327}, u'phone': u'+14158397388', u'image_url': u'http://s3-media4.fl.yelpcdn.com/bphoto/42V-yDiNZcfLFT743jxmPA/o.jpg', u'location': {u'city': u'San Francisco', u'address1': u'1415 Larkin St', u'address2': u'', u'address3': u'', u'state': u'CA', u'country': u'US', u'zip_code': u'94109'}, u'id': u'contraband-coffee-bar-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 4.5, u'review_count': 60, u'name': u'Iron Horse Coffee Bar', u'url': u'https://www.yelp.com/biz/iron-horse-coffee-bar-san-francisco', u'price': u'$', u'coordinates': {u'latitude': 37.7882923185825, u'longitude': -122.404029965401}, u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/_eMt3Li_B5DdeAkHFsxIJA/o.jpg', u'location': {u'city': u'San Francisco', u'address1': u'25 Maiden Ln', u'address2': None, u'address3': u'', u'state': u'CA', u'country': u'US', u'zip_code': u'94108'}, u'id': u'iron-horse-coffee-bar-san-francisco', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}]}}






{u'total': 3747, 
u'businesses': 
    [{u'rating': 4.0, u'review_count': 439, 
    u'name': u'Union Square Plaza', u'url': u'https://www.yelp.com/biz/union-square-plaza-san-francisco', 
    u'coordinates': {u'latitude': 37.7879384, u'longitude': -122.4075056}, 
    u'phone': u'+14158315500', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/OB2NDnPEVscQfT3VWW6Jxg/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'333 Post St', u'zip_code': u'94108'}, 
    u'id': u'union-square-plaza-san-francisco', u'categories': 
    [{u'alias': u'parks', u'title': u'Parks'}]}, 

    {u'rating': 4.5, u'review_count': 350, 
    u'name': u'Yerba Buena Gardens', u'url': u'https://www.yelp.com/biz/yerba-buena-gardens-san-francisco', 
    u'coordinates': {u'latitude': 37.7848643788333, u'longitude': -122.402581932663}, 
    u'phone': u'+14158203550', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/OxPlqMtfR71Z7r_xmBnWqg/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'CA', u'address1': u'745 Mission St', u'zip_code': u'94103'}, 
    u'id': u'yerba-buena-gardens-san-francisco', u'categories': [{u'alias': u'parks', u'title': u'Parks'}]}, 

    {u'rating': 4.5, u'review_count': 29, u'name': u'One Kearny', u'url': u'https://www.yelp.com/biz/one-kearny-san-francisco', 
    u'coordinates': {u'latitude': 37.7877464, u'longitude': -122.4039383}, 
    u'phone': u'+14157881133', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/EyFQlNfjt9BzMqO63p-x9w/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'Ste 510', u'address3': u'', u'state': u'CA', u'address1': u'23 Geary St', u'zip_code': u'94108'}, 
    u'id': u'one-kearny-san-francisco', u'categories': [{u'alias': u'parks', u'title': u'Parks'}]}, 

    {u'rating': 5.0, u'review_count': 296, u'name': u"Captain Kirk's San Francisco Sailing", u'url': u'https://www.yelp.com/biz/captain-kirks-san-francisco-sailing-san-francisco', 
    u'coordinates': {u'latitude': 37.78138, u'longitude': -122.4214}, 
    u'phone': u'+16509300740', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/n47k_neGs2uWUu_jlH_csA/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': u'Ste E-736', u'address3': u'', u'state': u'CA', u'address1': u'601 Van Ness Ave', u'zip_code': u'94102'}, 
    u'id': u'captain-kirks-san-francisco-sailing-san-francisco', u'categories': [{u'alias': u'boating', u'title': u'Boating'}, {u'alias': u'boatcharters', u'title': u'Boat Charters'}]}, 

    {u'rating': 4.5, u'review_count': 114, u'name': u'EscapeSF', u'url': u'https://www.yelp.com/biz/escapesf-san-francisco', 
    u'coordinates': {u'latitude': 37.7937546372414, u'longitude': -122.404572442174}, 
    u'phone': u'+14152941718', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/qJ2jt4WRyI47jo7Z5rAUbw/o.jpg', 
    u'location': {u'city': u'San Francisco', u'country': u'US', u'address2': None, u'address3': u'', u'state': u'CA', u'address1': u'602 Kearny St', u'zip_code': u'94108'}, 
    u'id': u'escapesf-san-francisco', u'categories': [{u'alias': u'escapegames', u'title': u'Escape Games'}]}]}

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

# def whats_near(end_lat, end_lng, activity_types):
#     """Makes a call to Google Places API and returns a json object of the results"""
#     key = os.environ.get('KEY_KEY')
#     places_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json" #&key=SERVER_KEY
#     radar_places_url = "https://maps.googleapis.com/maps/api/place/radarsearch/json" #have to add radius, this is producing an invalid request check the docs 

    
#     activity_feedback = []

#     # for loop to go through each activity and add it as a request to the Google Places API
#     for a in activity_types:
#         # have the type specific to the iterating variable 
#         r = requests.post("https://maps.googleapis.com/maps/api/place/nearbysearch/json?key=%s&location=%s,%s&open_now=True&types=%s" % (key, end_lat, end_lng, a))
#         json_activity = r.json()
#         activity_feedback.append(json_activity)
#         import pdb; pdb.set_trace()

#     # return the compiled API calls for the activities the user requested
#     return activity_feedback 

# # Make a function to get the place details from the place ids still doesn't include the name of the place 
# def retrieve_place_details(place_id):
#     """Given json results, find the place details"""

#     key = os.environ.get('KEY_KEY')
#     retrieve_place_details = ("https://maps.googleapis.com/maps/api/place/details/json?placeid=%s&key=%s" % (place_id, key))

# # Have the user choose a place to visit from the json
# def parse_activity_feedback(place_id):
#     """Input parameter is the json object and this function parses out the name and lat lng of the place in a dict"""
    
#     activity_feedback_details = {}
#     activity_feedback.split()

#     # Use .values()
#     place_location = ["results"][0] # location has the keys lat lng
#     place_name = ["results"][3] # check that this is the location name
#     place_activity_type = ["results"][10] # check that this is the activity_type

#     #add to the dictionary THIS MIGHT BE REPETITIVE
#     activity_feedback["activity_place"] = place_name, place_location, place_activity_type
#     # will want to present to the user place details along their route
#     # might need to filter this to be inbetween their start and end latlngs

# # geocoding by place name from Google Maps lecture 


# # #waypoints are stops between two destinations!
# # https://maps.googleapis.com/maps/api/directions/json?origin=Boston,MA&destination=Concord,MA&waypoints=Charlestown,MA|Lexington,MA&key=YOUR_API_KEY

# # #need to find code for the user's current location 

# # # function that takes the json dictionary and takes the

if __name__ == "__main__":
    DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0', port=5000) #vagrant requires port to be 5000
