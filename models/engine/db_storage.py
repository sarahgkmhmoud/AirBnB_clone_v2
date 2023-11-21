#!/usr/bin/python3
"""data base storage"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine()
        