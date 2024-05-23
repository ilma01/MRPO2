from Procedures import CarProcedure, CarBrandProcedure, CarModelProcedure, ServiceProcedure, ConsumableProcedure
from Repository.XMLRepos import CarBrandXMLRepos, CarModelXMLRepos, CarXMLRepos, ConsumableXMLRepos, ServiceXMLRepos

file = 'file.xml'

BrandRepos = CarBrandXMLRepos(file)
ModelRepos = CarModelXMLRepos(file, BrandRepos)
CarRepos = CarXMLRepos(file, ModelRepos)
ServiceRepos = ServiceXMLRepos(file)
ConsRepos = ConsumableXMLRepos(file)

CarUC = CarProcedure.CarProcedure(CarRepos)
BrandUC = CarBrandProcedure.CarBrandProcedure(BrandRepos)
ModelUC = CarModelProcedure.CarModelProcedure(ModelRepos)
ServiceUC = ServiceProcedure.ServiceProcedure(ServiceRepos)
ConsUC = ConsumableProcedure.ConsumableProcedure(ConsRepos)

#CarUC.update_car_mileage(512000, 'VIN534250')

#ModelUC.add_model('Supra', BrandUC.get_brand('Toyota'), body_type='Sedan')
# ModelUC.add_model('Impreza', BrandUC.get_brand('Subaru'))
# ModelUC.update_model('Supra', body_type='Coupe')
#
# CarUC.add_car(ModelUC.get_model('Supra'), 0, vin='XTA2105')
# CarUC.add_car(ModelUC.get_model('Supra'), 0, vin='XTA2106')
# CarUC.add_car(ModelUC.get_model('Supra'), 500)
# CarUC.add_car(ModelUC.get_model('Impreza'), 111)
CarUC.update_car_mileage(666666, 'XTA21654305')
#
# print('---------------')
# for i in CarUC.get_all_cars():
#     print(f'{i.model.brand.name}\t{i.model.name}\t{i.mileage}')
#
# ConsUC.add_consumable('Свечи', '_NGK_', 1500)
# ConsUC.add_consumable('Масло', 'Лукойл', 3500)
# ConsUC.add_consumable('Шаровые', 'Трек', 4000)
# ConsUC.add_consumable('Шаровые', 'Трекr', 4000)
#
# print('---------------')
# for i in ConsUC.get_all_consumables():
#     print(f'{i.name}\t{i.manufacturer}\t{i.cost}')

