#!/usr/bin/python3
"""data base storage"""

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

# Get values from environment variables
mysql_user = getenv("HBNB_MYSQL_USER")
mysql_pwd = getenv("HBNB_MYSQL_PWD")
mysql_host = getenv("HBNB_MYSQL_HOST")
mysql_db = getenv("HBNB_MYSQL_DB")

# Construct the database URL
db_url = f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}"

# Create the SQLAlchemy engine
class DBStorage:
    __engine = None
    __session = None
    def __init__(self):
        self.__engine = create_engine(db_url, pool_pre_ping=True)
        metadata = MetaData(bind=self.__engine)
        if getenv("HBNB_ENV") == 'test':
            metadata.drop.all()
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
    def all(self, cls=None):
        cls_dict = {}
        if cls:
            cls_list = self.__session.query(cls)
        else:
            cls_list = self.__session.query()
        for instance in cls_list:
            key = f"{instance.__classs__.__name__}.{instance.id}"
            cls_dict [key] = instance 
        return cls_dict

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    

    
