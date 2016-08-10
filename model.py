from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

#Model definitions

class Trip(db.Model):
    """The trip"""

    __tablename__ = "trips" 
    #seems weird to make this plural since it's a one to many relationship

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False) #need datetime for this
    start_location = db.Column(db.String(100), nullable=False) #not provided by the user but found using HTML5 Geolocation
    arrival_time = db.Column(db.DateTime, nullable=False) #need datetime for this
    end_location = db.Column(db.String(100), nullable=False)
    #take the string and convert to lat-long using google map directions api

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Trip id =%s Start Time =%s Start Location =%s Arrival Time =%s End Location =%s>" %(self.trip_id, self.start_time, self.start_location, self.arrival_time, self.end_location)

class TripPreference(db.Model):
    """A trip can have multiple activity preferences"""

    __tablename__ = "trip_preferences"

    trip_preference_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    preference_id = db.Column(db.String(100), db.ForeignKey('preferences.preference_id'), autoincrement=True, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Trip Preferences id =%s Preferences id =%s Trip id =%s>" %(self.trip_preference_id, self.preferences_id, self.trip_id)

class Preference(db.Model): #lookup table
    """To ensure referential integrity amongst trip preferences (think BookGenre) """

    __tablename__ = "preferences"
    
    preference_id = db.Column(db.String(5), primary_key=True) 
    name = db.Column(db.String(100), nullable=False) #human readable activity
    google_places_id = db.Column(db.String(100), nullable=False)
    deprecated = db.Column(db.Boolean, default=False) #if that preference is still available on google places, supermarkets
    
    trips = db.relationship('Trip', backref='preferences', secondary='trip_preferences')


    def __repr__(self):
        """Provide helpful representation when printed"""

        return "<Preferences id =%s Name =%s Google Places id = %s Deprecated =%s>" %(self.preference_id, self.name, self.google_places_id, self.deprecated)


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///project'
#    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

if __name__== "__main__":
    from server import app
    connect_to_db(app)

