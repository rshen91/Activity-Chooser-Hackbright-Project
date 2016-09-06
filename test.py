import unittest
from server import app
import doctest
from selenium import webdriver
from model import connect_to_db, db, example_data, Trip

class TestDatabase(unittest.TestCase):

    def setUp(self):
        """Stuff to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        #Connect to test database
        connect_to_db(app, "postgresql:///test")
        print "setUp"
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
        print "test_homepage_activity_types"
        # Sample data has a preference called Outdoor that should appear on the homepage if the def homepage() works
        self.assertIn("Outdoor", result.data)

    # def test_add_trip_to_table(self):
    #     """Test the add_trip_to_table()"""

    #     result = self.client.post("/activity_time",
    #                             data={"user_lat": "37.2939421"})

    #     print "\n\n\n\n\n\n result", result
    #     # user lat is in the hidden value in the second page so it should appear from the sample data
    #     self.assertIn("37.2939421", result.data)

class TestRoutes(unittest.TestCase):

    def setUp(self):
        """Stuff to do before every test"""

        self.client = app.test_client()
        app.config['TESTING'] = True
        #Connect to test database
        connect_to_db(app, "postgresql:///test")
        print "setUp"
        #Create tables and add sample data
        db.create_all()
        example_data()

    def tearDown(self):
        """Do at the end of every test"""

        db.session.close()
        db.drop_all()

    def test_homepage(self):
        """Make sure that address field appears on the homepage"""
        result = self.client.get('/')
        print "test_homepage"
        self.assertEqual(result.status_code, 200)
        self.assertIn('address', result.data)

    def test_next_page(self):
        """Make sure that the choose activity page loads once values are submitted"""
        result = self.client.post('/activity_time',
                                  data={'user_lat': '37.788668',
                                        'user_lng': '-122.411499',
                                        'end_location': '683 Sutter St San Francisco',
                                        'arrival_time': '12:00',
                                        'activity_type': [u'Bakeries'],
                                        'activity_location_preference': 'near_end_location' }) 
        self.assertIn("Please choose one business to visit.", result.data) 

    # def test_next_final_page(self):
    #     """Make sure the final page loads once values are submitted"""
    #     result = self.client.post('/choose',
    #                             data={'chosen_phone': '+15107871827',
    #                                   'business_name': 'Warehouse Cafe',
    #                                   'business_rating': '4.0',
    #                                   'activity_lat': '38.0464450751',
    #                                   'activity_lng': '-122.183320586',
    #                                   'business_image': 'http://s3-media1.fl.yelpcdn.com/bphoto/PcCGEmB-iARgxnCbb9ckSA/o.jpg',
    #                                   'business_url': 'https://www.yelp.com/biz/warehouse-cafe-port-costa-3?adjust_creative=HzOGErjEzRrxoumZf-xlTA&utm_campaign=yelp_api_v3&utm_medium=api_v3_business_search&utm_source=HzOGErjEzRrxoumZf-xlTA',
    #                                   'business_street':'5 Canyon Lake Dr',
    #                                   'business_city': 'Port Costa',
    #                                   'business_zipcode': '',
    #                                   'user_lat': '37.7886625',
    #                                   'user_lng': '-122.4115566',
    #                                   'end_lat':'37.7960282',
    #                                   'end_lng': '-122.4308668',
    #                                   'end_location': '2030 Vallejo Street San Francisco',
    #                                   'start_location': '695 Sutter St, San Francisco, CA 94102, USA'}) 
    #     self.assertIn("Here is the", result.data)


if __name__=="__main__":
    unittest.main()
