"""Using ratings as a model for this seed.py. Making this to input some values to the 
preferences table for name and google_places_id"""
from model import Preference, Trip, TripPreference, connect_to_db, db
from server import app

# need to change the seed file to include pipes with the human readable activity 
# that is stored in the column "name"
def load_google_places_id():
    """Load google places id into the preferences table."""

    print "Google Places id Place Types"

    for i, row in enumerate(open("templates/google_places_place_types")):
        row = row.rstrip().split
        google_places_id = row

        google_places_id = Preference(google_places_id=google_places_id,
            name=name, deprecated=deprecated)

        db.session.add(google_places_id)

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
    db.create_all()

    load_google_places_id()
    set_val_user_id
