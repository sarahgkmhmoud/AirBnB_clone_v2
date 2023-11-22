#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy.orm import relationship

Associal_table = Table("place_amenity", Base.metadata, 
                       Column("place_id", String(60), ForeignKey("places.id"), Primary_key=True, nullable=False),
                       Column("amenity_id", String(60), ForeignKey("amenities.id"), Primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False,)
        number_bathrooms = Column(Integer,default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship ('Review', backref="place", cascade="delete")
        amenities = relationship('Amenity', secondary="place_amenity", viewonly=False)

    elif getenv("HBNB_TYPE_STORAGE") != "db": 

        @property
        def reviews(self):
            reviews_list = []
            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    reviews_list.append(Review)
            return reviews_list

        @property
        def amenities(self):
            amenities_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.place_id == self.id:
                    amenities_list.append(Amenity)
            return  amenities_list

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                    self.amenity_ids.append(value.id)

            
        