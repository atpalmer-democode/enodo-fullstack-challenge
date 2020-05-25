from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


ModelBase = declarative_base()


class Property(ModelBase):
    __tablename__ = 'properties'

    id = Column(Integer, primary_key=True)
    full_address = Column('Full Address', String)
    class_description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class PropertySelection(ModelBase):
    __tablename__ = 'selections'

    property_id = Column(Integer, ForeignKey('properties.id'), primary_key=True)
    property = relationship('Property')

