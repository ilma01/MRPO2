from Repository.Repos import FakeRepos
from sqlalchemy.orm import sessionmaker
from Models.Car import Car as OldCar
from Models.CarBrand import CarBrand as OldCarBrand
from Models.CarModel import CarModel as OldCarModel
from Models.Consumable import Consumable as OldConsumable
from Models.Service import Service as OldService
from ModelsBD import CarBrand, CarModel, Car, Consumable, Service, ServiceConsumable, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class CarBrandRepos(FakeRepos):
    def to_new_car_brand(self, old_car_brand: OldCarBrand) -> CarBrand:
        return CarBrand(
            name=old_car_brand.name,
            country=old_car_brand.country,
            founding_year=old_car_brand.founding_year
        )

    def to_old_car_brand(self, new_car_brand: CarBrand) -> OldCarBrand:
        if new_car_brand:
            return OldCarBrand(
                name=new_car_brand.name,
                country=new_car_brand.country,
                founding_year=new_car_brand.founding_year
            )
        return None

    def add(self, brand):
        self.session.add(self.to_new_car_brand(brand))
        self.session.commit()

    def remove(self, brand):
        self.session.delete(self.session.query(CarBrand).filter_by(name=brand.name).first())
        self.session.commit()

    def update(self, brand):
        self.session.merge(self.to_new_car_brand(brand))
        self.session.commit()

    def get_all(self):
        return list(map(self.to_old_car_brand, self.session.query(CarBrand).all()))

    def get(self, name):
        ret = self.to_old_car_brand(self.session.query(CarBrand).filter_by(name=name).first())
        if ret:
            return ret
        return None

class CarModelRepos(FakeRepos):
    def to_new_car_model(self, old_car_model: OldCarModel) -> CarModel:
        return CarModel(
            name=old_car_model.name,
            brand=self.session.query(CarBrand).filter_by(name=old_car_model.brand.name).first(),
            year=old_car_model.year,
            body_type=old_car_model.body_type,
            engine_volume=old_car_model.engine_volume
        )

    def to_old_car_model(self, new_car_model: CarModel) -> OldCarModel:
        if new_car_model:
            return OldCarModel(
                name=new_car_model.name,
                brand=self.to_old_car_brand(new_car_model.brand),
                year=new_car_model.year,
                body_type=new_car_model.body_type,
                engine_volume=new_car_model.engine_volume
            )
        return None

    def to_old_car_brand(self, new_car_brand: CarBrand) -> OldCarBrand:
        if new_car_brand:
            return OldCarBrand(
                name=new_car_brand.name,
                country=new_car_brand.country,
                founding_year=new_car_brand.founding_year
            )
        return None

    def add(self, model):
        self.session.add(self.to_new_car_model(model))
        self.session.commit()

    def remove(self, model):
        self.session.delete(self.session.query(CarModel).filter_by(name=model.name).first())
        self.session.commit()

    def update(self, model):
        self.session.merge(self.to_new_car_model(model))
        self.session.commit()

    def get_all(self):
        return list(map(self.to_old_car_model, self.session.query(CarModel).all()))

    def get(self, name):
        ret = self.to_old_car_model(self.session.query(CarModel).filter_by(name=name).first())
        if ret:
            return ret
        return None

class CarRepos(FakeRepos):
    def to_new_car(self, old_car: OldCar) -> Car:
        return Car(
            model=self.session.query(CarModel).filter_by(name=old_car.model.name).first(),
            mileage=old_car.mileage,
            year=old_car.year,
            vin=old_car.vin,
            last_service_mileage=old_car.last_service_mileage,
            last_service_date=old_car.last_service_date
        )

    def to_old_car(self, new_car: Car) -> OldCar:
        if new_car:
            return OldCar(
                model=self.to_old_car_model(new_car.model),
                mileage=new_car.mileage,
                year=new_car.year,
                vin=new_car.vin,
                last_service_mileage=new_car.last_service_mileage,
                last_service_date=new_car.last_service_date
            )
        return None

    def to_old_car_model(self, new_car_model: CarModel) -> OldCarModel:
        if new_car_model:
            return OldCarModel(
                name=new_car_model.name,
                brand=self.to_old_car_brand(new_car_model.brand),
                year=new_car_model.year,
                body_type=new_car_model.body_type,
                engine_volume=new_car_model.engine_volume
            )
        return None

    def to_old_car_brand(self, new_car_brand: CarBrand) -> OldCarBrand:
        if new_car_brand:
            return OldCarBrand(
                name=new_car_brand.name,
                country=new_car_brand.country,
                founding_year=new_car_brand.founding_year
            )
        return None


    def add(self, car):
        self.session.add(self.to_new_car(car))
        self.session.commit()

    def remove(self, car):
        self.session.delete(self.session.query(Car).filter_by(vin=car.vin).first())
        self.session.commit()

    def update(self, car):
        self.session.merge(self.to_new_car(car))
        self.session.commit()

    def get_all(self):
        return list(map(self.to_old_car, self.session.query(Car).all()))

    def get(self, vin):
        ret = self.to_old_car(self.session.query(Car).filter_by(vin=vin).first())
        if ret:
            return ret
        return None

class ConsumableRepos(FakeRepos):
    def to_new_consumable(self, old_consumable: OldConsumable) -> Consumable:
        return Consumable(
            name=old_consumable.name,
            manufacturer=old_consumable.manufacturer,
            cost=old_consumable.cost
        )

    def to_old_consumable(self, new_consumable: Consumable) -> OldConsumable:
         if new_consumable:
            return OldConsumable(
                name=new_consumable.name,
                manufacturer=new_consumable.manufacturer,
                cost=new_consumable.cost
            )
         return None

    def add(self, consumable):
        self.session.add(self.to_new_consumable(consumable))
        self.session.commit()

    def remove(self, consumable):
        self.session.delete(self.session.query(Consumable).filter_by(name=consumable.name).first())
        self.session.commit()

    def update(self, consumable):
        self.session.merge(self.to_new_consumable(consumable))
        self.session.commit()

    def get_all(self):
        return list(map(self.to_old_consumable,self.session.query(Consumable).all()))

    def get(self, name):
        ret = self.to_old_consumable(self.session.query(Consumable).filter_by(name=name).first())
        if ret:
            return ret
        return None

class ServiceRepos(FakeRepos):
    def to_new_service(self, old_service: OldService) -> Service:
        return Service(
            id=old_service.id,
            date=old_service.date,
            service_type=old_service.service_type,
            cost=old_service.cost,
            car_vin=old_service.car.vin,
            tasks=old_service.tasks,
            mileage=old_service.mileage
        )

    def to_old_service(self, new_service: Service) -> OldService:
        if new_service:
            old_service = OldService(
                id=new_service.id,
                date=new_service.date,
                service_type=new_service.service_type,
                cost=new_service.cost,
                car=self.to_old_car(self.session.query(Car).filter_by(vin=new_service.car_vin).first()),
                tasks=new_service.tasks
            )
            old_service.mileage = new_service.mileage
            return old_service
        return None

    def to_old_car(self, new_car: Car) -> OldCar:
        if new_car:
            return OldCar(
                model=self.to_old_car_model(new_car.model),
                mileage=new_car.mileage,
                year=new_car.year,
                vin=new_car.vin,
                last_service_mileage=new_car.last_service_mileage,
                last_service_date=new_car.last_service_date
            )
        return None

    def to_old_car_model(self, new_car_model: CarModel) -> OldCarModel:
        if new_car_model:
            return OldCarModel(
                name=new_car_model.name,
                brand=self.to_old_car_brand(new_car_model.brand),
                year=new_car_model.year,
                body_type=new_car_model.body_type,
                engine_volume=new_car_model.engine_volume
            )
        return None

    def to_old_car_brand(self, new_car_brand: CarBrand) -> OldCarBrand:
        if new_car_brand:
            return OldCarBrand(
                name=new_car_brand.name,
                country=new_car_brand.country,
                founding_year=new_car_brand.founding_year
            )
        return None

    def add(self, service):
        self.session.add(self.to_new_service(service))
        self.session.commit()

    def remove(self, service):
        self.session.delete(self.session.query(Service).filter_by(id=service.id).first())
        self.session.commit()

    def update(self, service):
        self.session.merge(self.to_new_service(service))
        self.session.commit()

    def get_all(self):
        return list(map(self.to_old_service,self.session.query(Service).all()))

    def get(self, service_id):
        ret = self.session.query(Service).filter_by(id=service_id).first()
        if ret:
            return ret
        return None