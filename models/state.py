#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(City, cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """getter attribute that returns the list of City instances"""
        city_vals = storage.all(City)
        city_lists = []

        for city in city_vals:
            if City.state_id == self.id:
                city_list.append(city)

        return city_list
