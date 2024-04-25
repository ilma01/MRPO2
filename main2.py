from Procedures import CarProcedure, CarBrandProcedure, CarModelProcedure, ServiceProcedure, ConsumableProcedure
from Repository import CarRep, CarBrandRep, CarModelRep, ServiceRep, ConsumableRep

CarUC = CarProcedure.CarProcedure(CarRep.CarRepos())
BrandUC = CarBrandProcedure.CarBrandProcedure(CarBrandRep.CarBrandRepos())
ModelUC = CarModelProcedure.CarModelProcedure(CarModelRep.CarModelRepos())
ServiceUC = ServiceProcedure.ServiceProcedure(ServiceRep.Services())
ConsUC = ConsumableProcedure.ConsumableProcedure(ConsumableRep.ConsumableRepos())

BrandUC.add_brand('Toyota')
BrandUC.add_brand('Subaru')

ModelUC.add_model('Supra', BrandUC.get_brand('Toyota'), body_type='Sedan')
ModelUC.add_model('Impreza', BrandUC.get_brand('Subaru'))
ModelUC.update_model('Supra', body_type='Coupe')

CarUC.add_car(ModelUC.get_model('Supra'), 0, vin='XTA2105')
CarUC.add_car(ModelUC.get_model('Supra'), 0, vin='XTA2106')
CarUC.add_car(ModelUC.get_model('Supra'), 500)
CarUC.add_car(ModelUC.get_model('Impreza'), 111)
CarUC.update_car_mileage(66666, 'XTA2105')

print('---------------')
for i in CarUC.get_all_cars():
    print(f'{i.model.brand.name}\t{i.model.name}\t{i.mileage}')

ConsUC.add_consumable('Свечи', '_NGK_', 1500)
ConsUC.add_consumable('Масло', 'Лукойл', 3500)
ConsUC.add_consumable('Шаровые', 'Трек', 4000)
ConsUC.add_consumable('Шаровые', 'Трекr', 4000)

print('---------------')
for i in ConsUC.get_all_consumables():
    print(f'{i.name}\t{i.manufacturer}\t{i.cost}')

