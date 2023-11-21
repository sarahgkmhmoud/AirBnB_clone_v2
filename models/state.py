#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade='all, delete-orphan')

    elif getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if City.state_id == self.id:
                    cities_list.append(City)
            return cities_list
