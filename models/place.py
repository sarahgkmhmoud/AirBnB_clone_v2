#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import relationship
from os import getenv
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = column(String(60), nullable=False, ForeignKey("cities.id"))
        user_id = column(String(60), nullable=False, ForeignKey("users.id"))
        name = column(String(128), nullable=False)
        description = column(String(1024), nullable=False)
        number_rooms = column(Integer, nullable=False, default=0)
        number_bathrooms = column(Integer, nullable=False, default=0)
        max_guest = column(Integer, nullable=False, default=0)
        price_by_night = column(Integer, nullable=False, default=0)
        latitude = column(Float, nullable=False)
        longitude = column(Float, nullable=False)
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

