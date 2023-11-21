#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE" == "db"):
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="states", cascade='all, delete-orphan')

    elif os.getenv("HBNB_TYPE_STORAGE" != "db"):
        @property
        def cities(self):
            cities_list = []
            for city in storage.all(City).values():
                if City.state_id == self.id:
                    cities_list.append(City)
            return cities_list
