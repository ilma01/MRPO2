from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, DateTime, String, Float, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class CarBrand(Base):
    __tablename__ = 'car_brands'
    name = Column(String, primary_key=True)
    country = Column(String)
    founding_year = Column(Integer)

class CarModel(Base):
    __tablename__ = 'car_models'
    name = Column(String, primary_key=True)
    brand_name = Column(String, ForeignKey('car_brands.name'), nullable=False)
    year = Column(Integer)
    body_type = Column(String)
    engine_volume = Column(Float)
    brand = relationship("CarBrand", foreign_keys=[brand_name])
class Car(Base):
    __tablename__ = 'cars'
    vin = Column(String, primary_key=True)
    model_name = Column(String, ForeignKey('car_models.name'), nullable=False)
    mileage = Column(Integer)
    year = Column(Integer)
    last_service_mileage = Column(Integer)
    last_service_date = Column(DateTime)
    model = relationship("CarModel", backref="cars")
    services = relationship("Service", backref="car")

class Consumable(Base):
    __tablename__ = 'consumables'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    manufacturer = Column(String)
    cost = Column(Float)

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    car_vin = Column(String, ForeignKey('cars.vin'), nullable=False)
    date = Column(DateTime)
    service_type = Column(String)
    mileage = Column(Integer)
    cost = Column(Float)
    tasks = Column(String)
    consumables = relationship("Consumable", secondary='service_consumables')

class ServiceConsumable(Base):
    __tablename__ = 'service_consumables'
    id = Column(Integer, primary_key=True)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    consumable_id = Column(Integer, ForeignKey('consumables.id'), nullable=False)