from Procedures import CarProcedure, CarBrandProcedure, CarModelProcedure, ServiceProcedure, ConsumableProcedure
from Repository.SQLAlchRepos import *
from Models import CarBrand, CarModel, Car, Consumable, Service
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mydatabase.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

BrandRepos = CarBrandRepos(session)
ModelRepos = CarModelRepos(session)
#CarRepos = CarRepos(session)
#ServiceRepos = ServiceRepos(session)
#ConsRepos = ConsumableRepos(session)

CarUC = CarProcedure.CarProcedure(CarRepos)
BrandUC = CarBrandProcedure.CarBrandProcedure(BrandRepos)

BrandUC.update_brand('Toyota', founding_year=1995)

#BrandUC.remove_brand('Toyota')

#CarUC.add_car(ModelUC.get_model('Supra'), vin='XTA342141')

#ModelUC.add_model('Supra', BrandUC.get_brand('Toyota'), body_type='Sedan')
#ModelUC.add_model('Impreza', BrandUC.get_brand('Subaru'))
#ModelUC.update_model('Supra', body_type='Coupe')