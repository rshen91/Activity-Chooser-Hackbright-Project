import unittest
from server import app
import doctest
from selenium import webdriver

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Stuff to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        #Connect to test database
        connect_to_db(app, "postgresql:///testdb")

        #Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at the end of every test"""

        db.session.close()
        db.drop_all()

    def test_homepage_activity_types(self):
        """Want to make sure that Preference is displaying on the homepage"""
        result = self.client.get("/")
        # Sample data has a preference called Outdoor that should appear on the homepage if the def homepage() works
        self.assertIn("Outdoor", result.data)

    def test_add_trip_to_table(self):
        """Test the add_trip_to_table()"""
        result = self.client.get("/choose")
        # user lat is in the hidden value in the second page so it should appear from the sample data
        self.assertIn("37.2939421", result.data)

class TestCase(object):

    def test_homepage(self):
        """Make sure that address field appears on the homepage"""
        result = client.get('/')
        self.assertIn('address', result.data)

    def test_no_duplicates(self):
        """Make sure that the remove_duplicates removes duplicates"""
        
# this class is for a selenium test
class TestApp(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(selt):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://127.0.0.1/')
        self.assertEqual(self.browser.title, 'ActivityChooser')

    #def test_some_integration

if __name__=="__main__":
    unittest.main()

# api call {u'total': 467, u'businesses': [{u'rating': 4.0, u'review_count': 342, u'name': u'O.H.S.O. Eatery + Distillery', u'url': u'https://www.yelp.com/biz/o-h-s-o-eatery-distillery-scottsdale-5', u'price': u'$$', u'coordinates': {u'latitude': 33.6278142695705, u'longitude': -111.893512550648}, u'phone': u'+14809483159', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/dD5uOyhOnXJvIugXhptAqQ/o.jpg', u'location': {u'city': u'Scottsdale', u'address1': u'15681 N Hayden Rd', u'address2': u'Ste 112', u'address3': u'', u'state': u'AZ', u'country': u'US', u'zip_code': u'85260'}, u'id': u'o-h-s-o-eatery-distillery-scottsdale-5', u'categories': [{u'alias': u'newamerican', u'title': u'American (New)'}, {u'alias': u'distilleries', u'title': u'Distilleries'}, {u'alias': u'breakfast_brunch', u'title': u'Breakfast & Brunch'}]}, {u'rating': 4.0, u'review_count': 493, u'name': u'Four Peaks Grill & Tap', u'url': u'https://www.yelp.com/biz/four-peaks-grill-and-tap-scottsdale-4', u'price': u'$$', u'coordinates': {u'latitude': 33.6286125, u'longitude': -111.8937988}, u'phone': u'+14809911795', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/DVqmvD6UTOubZx6EIhJXuw/o.jpg', u'location': {u'city': u'Scottsdale', u'address1': u'15745 N Hayden Rd', u'address2': u'Ste D5-7', u'address3': u'', u'state': u'AZ', u'country': u'US', u'zip_code': u'85260'}, u'id': u'four-peaks-grill-and-tap-scottsdale-4', u'categories': [{u'alias': u'pubs', u'title': u'Pubs'}, {u'alias': u'breweries', u'title': u'Breweries'}, {u'alias': u'newamerican', u'title': u'American (New)'}]}, {u'rating': 4.0, u'review_count': 593, u'name': u"Tom's Thumb Fresh Market", u'url': u'https://www.yelp.com/biz/toms-thumb-fresh-market-scottsdale', u'price': u'$$', u'coordinates': {u'latitude': 33.6393699645996, u'longitude': -111.879257202148}, u'phone': u'+14805138186', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/Z8f0DA7ou0iKm_YvNwDr1g/o.jpg', u'location': {u'city': u'Scottsdale', u'address1': u'9393 E Bell Rd', u'address2': u'', u'address3': u'', u'state': u'AZ', u'country': u'US', u'zip_code': u'85260'}, u'id': u'toms-thumb-fresh-market-scottsdale', u'categories': [{u'alias': u'bbq', u'title': u'Barbeque'}, {u'alias': u'carwash', u'title': u'Car Wash'}, {u'alias': u'servicestations', u'title': u'Gas & Service Stations'}]}, {u'rating': 4.5, u'review_count': 156, u'name': u'Fired Pie', u'url': u'https://www.yelp.com/biz/fired-pie-scottsdale', u'price': u'$', u'coordinates': {u'latitude': 33.6194801, u'longitude': -111.8981934}, u'phone': u'+14804049996', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/PYZ8eSwHHUbZ_SbyPd70tw/o.jpg', u'location': {u'city': u'Scottsdale', u'address1': u'14740 N Northsight Blvd', u'address2': u'', u'address3': u'', u'state': u'AZ', u'country': u'US', u'zip_code': u'85260'}, u'id': u'fired-pie-scottsdale', u'categories': [{u'alias': u'pizza', u'title': u'Pizza'}, {u'alias': u'hotdogs', u'title': u'Fast Food'}, {u'alias': u'salad', u'title': u'Salad'}]}, {u'rating': 4.5, u'review_count': 65, u'name': u'Cafe Paris French Bistro & Catering', u'url': u'https://www.yelp.com/biz/cafe-paris-french-bistro-and-catering-scottsdale', u'price': u'$', u'coordinates': {u'latitude': 33.62303, u'longitude': -111.90309}, u'phone': u'+14809984875', u'image_url': u'http://s3-media2.fl.yelpcdn.com/bphoto/I9pqRJaSFpeiRiPF9xzBTQ/o.jpg', u'location': {u'city': u'Scottsdale', u'address1': u'15125 N Hayden Rd', u'address2': u'Ste 111', u'address3': u'', u'state': u'AZ', u'country': u'US', u'zip_code': u'85260'}, u'id': u'cafe-paris-french-bistro-and-catering-scottsdale', u'categories': [{u'alias': u'french', u'title': u'French'}, {u'alias': u'breakfast_brunch', u'title': u'Breakfast & Brunch'}, {u'alias': u'sandwiches', u'title': u'Sandwiches'}]}]}
# api call {u'total': 349, u'businesses': [{u'rating': 4.0, u'review_count': 246, u'name': u'Press Coffee Roasters', u'url': u'https://www.yelp.com/biz/press-coffee-roasters-scottsdale', u'price': u'$$', u'coordinates': {u'latitude': 33.6238997, u'longitude': -111.9249321}, u'phone': u'+14807189762', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/2UxrqWj2Pine6NkKT2JUxg/o.jpg', u'location': {u'city': u'Scottsdale', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'AZ', u'address1': u'15147 N Scottsdale Rd', u'zip_code': u'85254'}, u'id': u'press-coffee-roasters-scottsdale', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 5.0, u'review_count': 15, u'name': u'Passport Coffee & Tea', u'url': u'https://www.yelp.com/biz/passport-coffee-and-tea-scottsdale', u'price': u'$$', u'coordinates': {u'latitude': 33.612293, u'longitude': -111.91806}, u'phone': u'+14809481419', u'image_url': u'http://s3-media3.fl.yelpcdn.com/bphoto/TMzkcQ-fz2IzsloS43LZZg/o.jpg', u'location': {u'city': u'Scottsdale', u'country': u'US', u'address2': u'', u'address3': u'', u'state': u'AZ', u'address1': u'7585 E Gray Rd', u'zip_code': u'85260'}, u'id': u'passport-coffee-and-tea-scottsdale', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 4.5, u'review_count': 6, u'name': u"Erika's Coffee Dock", u'url': u'https://www.yelp.com/biz/erikas-coffee-dock-scottsdale', u'price': u'$', u'coordinates': {u'latitude': 33.637733, u'longitude': -111.881905}, u'phone': u'+16025730821', u'image_url': u'http://s3-media1.fl.yelpcdn.com/bphoto/CDU6sX4JrqdnQf5-saCaQg/o.jpg', u'location': {u'city': u'Scottsdale', u'country': u'US', u'address2': None, u'address3': u'', u'state': u'AZ', u'address1': u'9377 E Bell Rd', u'zip_code': u'85260'}, u'id': u'erikas-coffee-dock-scottsdale', u'categories': [{u'alias': u'delis', u'title': u'Delis'}, {u'alias': u'coffee', u'title': u'Coffee & Tea'}]}, {u'rating': 4.0, u'review_count': 43, u'name': u'Cream City Cafe', u'url': u'https://www.yelp.com/biz/cream-city-cafe-scottsdale', u'price': u'$$', u'coordinates': {u'latitude': 33.6269887, u'longitude': -111.8555748}, u'phone': u'+14805887008', u'image_url': u'http://s3-media4.fl.yelpcdn.com/bphoto/3T4Q6g46tuAFX4Pf3tnUtA/o.jpg', u'location': {u'city': u'Scottsdale', u'country': u'US', u'address2': u'Ste 100', u'address3': u'', u'state': u'AZ', u'address1': u'10405 E McDowell Mountain Ranch Rd', u'zip_code': u'85255'}, u'id': u'cream-city-cafe-scottsdale', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}, {u'alias': u'gelato', u'title': u'Gelato'}, {u'alias': u'icecream', u'title': u'Ice Cream & Frozen Yogurt'}]}, {u'rating': 4.0, u'review_count': 42, u'name': u'The Coffee Bean & Tea Leaf', u'url': u'https://www.yelp.com/biz/the-coffee-bean-and-tea-leaf-scottsdale-2', u'price': u'$', u'coordinates': {u'latitude': 33.634162902832, u'longitude': -111.923889160156}, u'phone': u'+14806073146', u'image_url': u'http://s3-media4.fl.yelpcdn.com/bphoto/0R7DusQCtDyWfPAA2fsedw/o.jpg', u'location': {u'city': u'Scottsdale', u'country': u'US', u'address2': u'Ste A5', u'address3': u'', u'state': u'AZ', u'address1': u'16211 N Scottsdale Rd', u'zip_code': u'85254'}, u'id': u'the-coffee-bean-and-tea-leaf-scottsdale-2', u'categories': [{u'alias': u'coffee', u'title': u'Coffee & Tea'}]}]}