import unittest
import server

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

def test_activity_in_database(self):
    """Make sure that activity on homepage is from the Preference table"""

    result = client.post(, data={})

def test_no_duplicates(self):
    """Make sure that the remove_duplicates removes duplicates"""

def remove_duplicate_businesses(storing_yelp_values):
    """Helper function to remove duplicate businesses from start_oAuth"""
    
    unique_results = []

    for business in storing_yelp_values:
        if business not in unique_results:
            unique_results.append(business)

    return unique_results  

if __name__=="__main__":
    unittest.main()