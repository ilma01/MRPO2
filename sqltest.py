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
CarRepos = CarRepos(session)
ConsRepos = ConsumableRepos(session)
ServiceRepos = ServiceRepos(session)

BrandUC = CarBrandProcedure.CarBrandProcedure(BrandRepos)
ModelUC = CarModelProcedure.CarModelProcedure(ModelRepos)
CarUC = CarProcedure.CarProcedure(CarRepos)
ConsUC = ConsumableProcedure.ConsumableProcedure(ConsRepos)
ServiceUC = ServiceProcedure.ServiceProcedure(ServiceRepos)