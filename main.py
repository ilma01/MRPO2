import datetime

import Car
import CarBrand
import CarModel
import Consumable
import Service
from Repository import CarRep, ServiceRep

brand1 = CarBrand.CarBrand('Toyota', 'Japan')
brand2 = CarBrand.CarBrand('Nissan', 'Japan')
brand3 = CarBrand.CarBrand('BMW', 'Germany')
brand4 = CarBrand.CarBrand('LADA', 'Russia')

model1 = CarModel.CarModel('Supra', brand1, 1992, 'Coupe', 2.5)
model2 = CarModel.CarModel('200sx', brand2, 1992, 'Coupe', 2.0)
model3 = CarModel.CarModel('M3', brand3, 2006, 'Sedan', 3.0)
model4 = CarModel.CarModel('Tundra', brand1, 2015, 'OffRoad', 5.0)
model5 = CarModel.CarModel('21054', brand4, 2006, 'Sedan', 1.6)

car1 = Car.Car(model1, 200000, 1993, "XTA10532")
car2 = Car.Car(model2, 250000, 1995, "XTA10533")
car3 = Car.Car(model3, 352000, 2009, "XTA10534")
car4 = Car.Car(model4, 100500, 2016, "XTA10535")
car5 = Car.Car(model5, 106600, 2008, "XTA21054")

cons1 = Consumable.Consumable('Свеча', 'NGK', 2000)
cons2 = Consumable.Consumable('Масло', 'Motul', 4000)
cons3 = Consumable.Consumable('Сцепление', 'Toyota', 5500)
cons4 = Consumable.Consumable('Реактивные тяги', 'Ситек', 4500)

ser1 = Service.Service(1, datetime.datetime.now(), 'Замена масла', 50000, 2000, car1)
ser1 = Service.Service(1, datetime.datetime.now(), 'Замена масла', 245000, 2000, car2)
ser2 = Service.Service(2, datetime.datetime.now(), 'Замена сцепления', 60000, 5000, car3)
ser3 = Service.Service(3, datetime.datetime.now(), 'Замена свечей', 70000, 1000, car4)
ser4 = Service.Service(4, datetime.datetime.now(), 'Замена реактивных тяг', 80000, 2000, car5)

sRep = ServiceRep.Services()
cRep = CarRep.CarRepos()

sRep.add(ser1)
sRep.add(ser2)
sRep.add(ser3)
sRep.add(ser4)

cRep.add(car1)
cRep.add(car2)
cRep.add(car3)
cRep.add(car4)

for s in sRep.get_all():
    print('\n')
    print(f'Дата: {s.date}')
    print(f'Пробег на момент обслуживания: {s.mileage}')
    print(f'Список работ: {s.tasks}')
    print(f'Стоимость: {s.cost}')
    print(f'Тип обслуживания: {s.service_type}')
    print(f'Марка: {s.car.model.brand.name}')
    print(f'Модель: {s.car.model.name}')
    print(f'Пробег авто: {s.car.mileage}')

sRep.remove(ser4)

for s in sRep.get_all():
    print('\n')
    print(f'Тип обслуживания: {s.service_type}')
    print(f'Марка: {s.car.model.brand.name}')
    print(f'Модель: {s.car.model.name}')

print()
print(cRep.get('XTA10532').model.brand.name, cRep.get('XTA10532').model.name)