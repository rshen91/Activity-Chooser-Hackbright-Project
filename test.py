def setUp(self):
    """Stuff to do before every test"""

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
    self.assertIn("", results.data)