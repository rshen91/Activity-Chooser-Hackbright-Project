"""Using ratings as a model for this seed.py. Making this to input some values to the 
preferences table for name and yelp_id"""
from model import Preference, Trip, TripPreference, connect_to_db, db
from server import app

# need to change the seed file to include pipes with the human readable activity 
# that is stored in the column "name"
def load_yelp_id():
    """Load google places id into the preferences table."""

    print "Yelp API Place Types"

    for i, row in enumerate(open("yelp_api_places")):
        row = row.rstrip()
        print row

        yelp_id, name= row.split("|")
        
        # if the len(deprecated) > 0:
        #   the row is deprecated and NULL should be false

        # changed so that the value is 0s and 1s now 

        yelp_place = Preference(name=name,
                                yelp_id=yelp_id)

        db.session.add(yelp_place)

        if i % 100 == 0:
            print i

    db.session.commit()

#adapted from ratings
def set_val_user_id(): 
    """Set value for the next trip_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(Trip.trip_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('trips_trip_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()

if __name__ == "__main__":
    connect_to_db(app)

    load_yelp_id()
    # set_val_user_id
