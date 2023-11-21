#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship ('Review', backref="place", cascade='all, delete-orphan')

    elif getenv("HBNB_TYPE_STORAGE") != "db": 
        @property
        def reviews(self):
            reviews_list = []
            for review in list(models.storage.all(Review).values()):
                if Review.place_id == self.id:
                    reviews_list.append(Review)
            return reviews_list
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

