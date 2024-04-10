import unittest
from datetime import datetime, timedelta
import Car
import CarBrand
import CarModel
import Consumable
import Service
from business_rules import check_service_due, check_recommended_consumables, check_service_consumables, check_mileage_non_negative

class TestBusinessRules(unittest.TestCase):
    def setUp(self):
        self.brand = CarBrand.CarBrand('Toyota', 'Japan')
        self.model = CarModel.CarModel('Supra', self.brand, 1992, 'Coupe', 2.5)
        self.car = Car.Car(self.model, 200000, 1993, "XTA10532")
        self.current_date = datetime.now()
        self.cons = Consumable.Consumable('Масло', 'Motul', 4000)
        self.cons_rec = Consumable.Consumable('Сцепление', 'Toyota', 5500)
        self.service = Service.Service(1, datetime(year=2024, month=4, day=1), 'Замена масла', 50000, self.car)

    def test_check_service_due(self):
        # Проверка, что автомобиль требует обслуживания по пробегу и времени
        self.assertFalse(check_service_due(self.car, self.current_date))
        self.car.mileage = self.car.last_service_mileage + 5001
        self.assertTrue(check_service_due(self.car, self.current_date))
        self.car.mileage = self.car.last_service_mileage
        self.car.last_service_date = self.current_date - timedelta(days=185)
        self.assertTrue(check_service_due(self.car, self.current_date))


    def test_check_recommended_consumables(self):
        # Проверка, что все расходные материалы рекомендованные
        self.model.recommended_parts.append(self.cons_rec)
        self.service.consumables.append(self.cons_rec)
        self.assertTrue(check_recommended_consumables(self.service))
        self.service.consumables.append(self.cons)
        self.assertFalse(check_recommended_consumables(self.service))

    def test_check_service_consumables(self):
        # Проверка наличия списка затраченных материалов при обслуживании
        self.service.consumables = [Consumable.Consumable(name='Масло', manufacturer='Shell', cost=1), Consumable.Consumable(name='Фильтр масляный', manufacturer='Bosch', cost=1)]
        self.assertTrue(check_service_consumables(self.service))

    def test_check_service_consumables_none(self):
        # Проверка отсутствия списка затраченных материалов при обслуживании
        self.service.consumables = []
        self.assertFalse(check_service_consumables(self.service))

    def test_check_mileage_non_negative(self):
        # Проверка, что пробег неотрицательный
        self.car.mileage = 10000
        self.assertTrue(check_mileage_non_negative(self.car))

        self.car.mileage = -500  # Отрицательный пробег
        self.assertFalse(check_mileage_non_negative(self.car))

if __name__ == '__main__':
    unittest.main()