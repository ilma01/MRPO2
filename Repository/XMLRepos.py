from Repository.Repos import FakeRepos as XMLRepos
import xml.etree.ElementTree as ET
from Models.Car import Car
from Models.CarBrand import CarBrand
from Models.CarModel import CarModel
from Models.Consumable import Consumable
from Models.Service import Service
from datetime import datetime

class CarBrandXMLRepos(XMLRepos):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get(self, name):
        for brand_element in self.root.findall(".//brands/brand"):
            if brand_element.find("name").text == name:
                return self._xml_to_car_brand(brand_element)
        return None

    def add(self, brand):
        brands_element = self.root.find(".//brands")
        if brands_element is None:
            brands_element = ET.SubElement(self.root, "brands")
        new_brand_element = ET.SubElement(brands_element, "brand")
        self._car_brand_to_xml(brand, new_brand_element)
        self._save_xml()

    def remove(self, brand):
        brand_element = self.root.find(".//brands/brand[name='{}']".format(brand.name))
        if brand_element is not None:
            self.root.find(".//brands").remove(brand_element)
            self._save_xml()

    def update(self, brand):
        brand_element = self.get(brand.name)
        if brand_element is not None:
            self.add(brand)
            self.remove(brand_element)
            self._save_xml()

    def get_all(self):
        brands = []
        for brand_element in self.root.findall(".//brands/brand"):
            brands.append(self._xml_to_car_brand(brand_element))
        return brands

    def _xml_to_car_brand(self, brand_element):
        name = brand_element.find("name").text
        country_text = brand_element.find("country").text
        country = country_text if country_text != "None" else None
        founding_year_text = brand_element.find("founding_year").text
        founding_year = int(founding_year_text) if founding_year_text != "None" else None
        return CarBrand(name=name, country=country, founding_year=founding_year)

    def _car_brand_to_xml(self, brand, brand_element):
        name_element = brand_element.find("name")
        if name_element is not None:
            name_element.text = brand.name
        else:
            name_element = ET.SubElement(brand_element, "name")
            name_element.text = brand.name

        country_element = brand_element.find("country")
        if country_element is not None:
            country_element.text = brand.country
        else:
            country_element = ET.SubElement(brand_element, "country")
            country_element.text = str(brand.country)

        founding_year_element = brand_element.find("founding_year")
        if founding_year_element is not None:
            founding_year_element.text = str(brand.founding_year)
        else:
            founding_year_element = ET.SubElement(brand_element, "founding_year")
            founding_year_element.text = str(brand.founding_year)

class CarModelXMLRepos(XMLRepos):
    def __init__(self, file_path, car_brand_repository: CarBrandXMLRepos):
        super().__init__(file_path)
        self.root = self._load_xml()
        self.car_brand_repository = car_brand_repository

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get(self, name):
        for model_element in self.root.findall(".//models/model"):
            if model_element.find("name").text == name:
                return self._xml_to_car_model(model_element)
        return None

    def add(self, model):
        models_element = self.root.find(".//models")
        if models_element is None:
            models_element = ET.SubElement(self.root, "models")
        new_model_element = ET.SubElement(models_element, "model")
        self._car_model_to_xml(model, new_model_element)
        self._save_xml()

    def remove(self, model):
        model_element = self.root.find(".//models/model[name='{}']".format(model.name))
        if model_element is not None:
            self.root.find(".//models").remove(model_element)
            self._save_xml()

    def update(self, model):
        model_element = self.get(model.name)
        if model_element is not None:
            self.add(model)
            self.remove(model_element)
            self._save_xml()

    def get_all(self):
        models = []
        for model_element in self.root.findall(".//models/model"):
            models.append(self._xml_to_car_model(model_element))
        return models

    def _xml_to_car_model(self, model_element):
        name = model_element.find("name").text
        brand_name = model_element.find("brand").text
        year = int(model_element.find("year").text)
        body_type_text = model_element.find("body_type").text
        body_type = str(body_type_text) if body_type_text != "None" else None
        engine_volume_text = model_element.find("engine_volume").text
        engine_volume = float(engine_volume_text) if engine_volume_text != "None" else None

        brand = self.car_brand_repository.get(brand_name)

        return CarModel(name=name, brand=brand, year=year, body_type=body_type, engine_volume=engine_volume)

    def _car_model_to_xml(self, model, model_element):
        name_element = model_element.find("name")
        if name_element is not None:
            name_element.text = model.name
        else:
            name_element = ET.SubElement(model_element, "name")
            name_element.text = model.name

        brand_element = model_element.find("brand")
        if brand_element is not None:
            brand_element.text = model.brand.name
        else:
            brand_element = ET.SubElement(model_element, "brand")
            brand_element.text = model.brand.name

        year_element = model_element.find("year")
        if year_element is not None:
            year_element.text = str(model.year)
        else:
            year_element = ET.SubElement(model_element, "year")
            year_element.text = str(model.year)

        body_type_element = model_element.find("body_type")
        if body_type_element is not None:
            body_type_element.text = model.body_type if model.body_type is not None else "None"
        else:
            body_type_element = ET.SubElement(model_element, "body_type")
            body_type_element.text = model.body_type if model.body_type is not None else "None"

        engine_volume_element = model_element.find("engine_volume")
        if engine_volume_element is not None:
            engine_volume_element.text = str(model.engine_volume) if model.engine_volume is not None else "None"
        else:
            engine_volume_element = ET.SubElement(model_element, "engine_volume")
            engine_volume_element.text = str(model.engine_volume) if model.engine_volume is not None else "None"

class CarXMLRepos(XMLRepos):
    def __init__(self, file_path, car_model_repository: CarModelXMLRepos):
        super().__init__(file_path)
        self.root = self._load_xml()
        self.car_model_repository = car_model_repository

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get(self, vin):
        for car_element in self.root.findall(".//cars/car"):
            if car_element.find("vin").text == vin:
                return self._xml_to_car(car_element)
        return None

    def add(self, car):
        cars_element = self.root.find(".//cars")
        if cars_element is None:
            cars_element = ET.SubElement(self.root, "cars")
        new_car_element = ET.SubElement(cars_element, "car")
        self._car_to_xml(car, new_car_element)
        self._save_xml()

    def remove(self, car):
        car_element = self.root.find(".//cars/car[vin='{}']".format(car.vin))
        if car_element is not None:
            self.root.find(".//cars").remove(car_element)
            self._save_xml()

    def update(self, car):
        car_element = self.get(car.vin)
        if car_element is not None:
            self.add(car)
            self.remove(car_element)
            self._save_xml()

    def get_all(self):
        cars = []
        for car_element in self.root.findall(".//cars/car"):
            cars.append(self._xml_to_car(car_element))
        return cars

    def _xml_to_car(self, car_element):
        vin_text = car_element.find("vin").text
        vin = str(vin_text) if vin_text != "None" else None
        model_name = car_element.find("model").text
        mileage = int(car_element.find("mileage").text)
        year = int(car_element.find("year").text)
        model = self.car_model_repository.get(model_name)
        car = Car(model=model, mileage=mileage, year=year, vin=vin)
        car.last_service_mileage = int(car_element.find("last_service_mileage").text)
        car.last_service_date = datetime.strptime(car_element.find("last_service_date").text, "%Y-%m-%d")
        return car

    def _car_to_xml(self, car, car_element):
        vin_element = car_element.find("vin")
        if vin_element is not None:
            vin_element.text = car.vin
        else:
            vin_element = ET.SubElement(car_element, "vin")
            vin_element.text = car.vin

        model_element = car_element.find("model")
        if model_element is not None:
            model_element.text = car.model.name
        else:
            model_element = ET.SubElement(car_element, "model")
            model_element.text = car.model.name

        mileage_element = car_element.find("mileage")
        if mileage_element is not None:
            mileage_element.text = str(car.mileage)
        else:
            mileage_element = ET.SubElement(car_element, "mileage")
            mileage_element.text = str(car.mileage)

        year_element = car_element.find("year")
        if year_element is not None:
            year_element.text = str(car.year)
        else:
            year_element = ET.SubElement(car_element, "year")
            year_element.text = str(car.year)

        last_service_mileage_element = car_element.find("last_service_mileage")
        if last_service_mileage_element is not None:
            last_service_mileage_element.text = str(car.last_service_mileage)
        else:
            last_service_mileage_element = ET.SubElement(car_element, "last_service_mileage")
            last_service_mileage_element.text = str(car.last_service_mileage)

        last_service_date_element = car_element.find("last_service_date")
        if last_service_date_element is not None:
            last_service_date_element.text = str(car.last_service_date)
        else:
            last_service_date_element = ET.SubElement(car_element, "last_service_date")
            last_service_date_element.text = str(car.last_service_date)

class ConsumableXMLRepos(XMLRepos):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get(self, name, manufacturer):
        for consumable_element in self.root.findall(".//consumables/consumable"):
            if (consumable_element.find("name").text == name and
                consumable_element.find("manufacturer").text == manufacturer):
                return self._xml_to_consumable(consumable_element)
        return None

    def add(self, consumable):
        consumables_element = self.root.find(".//consumables")
        if consumables_element is None:
            consumables_element = ET.SubElement(self.root, "consumables")
        new_consumable_element = ET.SubElement(consumables_element, "consumable")
        self._consumable_to_xml(consumable, new_consumable_element)
        self._save_xml()

    def remove(self, consumable):
        consumable_element = self.get(consumable.name, consumable.manufacturer)
        if consumable_element is not None:
            self.root.remove(consumable_element)
            self._save_xml()

    def update(self, consumable):
        consumable_element = self.get(consumable.name, consumable.manufacturer)
        if consumable_element is not None:
            self._consumable_to_xml(consumable, consumable_element)
            self._save_xml()

    def get_all(self):
        consumables = []
        for consumable_element in self.root.findall(".//consumable"):
            consumables.append(self._xml_to_consumable(consumable_element))
        return consumables

    def _xml_to_consumable(self, consumable_element):
        name = consumable_element.find("name").text
        manufacturer = consumable_element.find("manufacturer").text
        cost = float(consumable_element.find("cost").text)
        return Consumable(name=name, manufacturer=manufacturer, cost=cost)

    def _consumable_to_xml(self, consumable, consumable_element):
        consumable_element.find("name").text = consumable.name
        consumable_element.find("manufacturer").text = consumable.manufacturer
        consumable_element.find("cost").text = str(consumable.cost)

class ServiceXMLRepos(XMLRepos):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.root = self._load_xml()

    def _load_xml(self):
        try:
            tree = ET.parse(self.file_path)
        except FileNotFoundError:
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.file_path)
        else:
            root = tree.getroot()
        return root

    def _indent(self, elem, level=0):
        i = "\n" + level * "\t"
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "\t"
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                self._indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def _save_xml(self):
        self._indent(self.root)
        xml_string = ET.tostring(self.root, encoding="utf-8", method="xml")
        with open(self.file_path, "wb") as file:
            file.write(xml_string)

    def get(self, service_id):
        for service_element in self.root.findall(".//services/service"):
            if int(service_element.find("id").text) == service_id:
                return self._xml_to_service(service_element)
        return None

    def add(self, service):
        services_element = self.root.find(".//services")
        if services_element is None:
            services_element = ET.SubElement(self.root, "services")
        new_service_element = ET.SubElement(services_element, "service")
        self._service_to_xml(service, new_service_element)
        self._save_xml()

    def remove(self, service):
        service_element = self.get(service.id)
        if service_element is not None:
            self.root.remove(service_element)
            self._save_xml()

    def update(self, service):
        service_element = self.get(service.id)
        if service_element is not None:
            self._service_to_xml(service, service_element)
            self._save_xml()

    def get_all(self):
        services = []
        for service_element in self.root.findall(".//service"):
            services.append(self._xml_to_service(service_element))
        return services

    def _xml_to_service(self, service_element):
        service_id = int(service_element.find("id").text)
        date = datetime.datetime.fromisoformat(service_element.find("date").text)
        service_type = service_element.find("type").text
        cost = float(service_element.find("cost").text)
        car = CarXMLRepos("").get(service_element.find("car").text)
        mileage = int(service_element.find("mileage").text)
        tasks = service_element.find("tasks").text if service_element.find("tasks") is not None else None
        consumables = []
        for consumable_element in service_element.findall("consumables/consumable"):
            consumable = self._xml_to_consumable(consumable_element)
            consumables.append(consumable)
        return Service(service_id, date, service_type, cost, car, tasks, consumables)

    def _service_to_xml(self, service, service_element):
        service_element.find("id").text = str(service.id)
        service_element.find("date").text = service.date.isoformat()
        service_element.find("type").text = service.service_type
        service_element.find("cost").text = str(service.cost)
        service_element.find("car").text = service.car.vin
        service_element.find("mileage").text = str(service.mileage)
        if service.tasks:
            tasks_element = service_element.find("tasks")
            if tasks_element is None:
                tasks_element = ET.SubElement(service_element, "tasks")
            tasks_element.text = service.tasks
        else:
            tasks_element = service_element.find("tasks")
            if tasks_element is not None:
                service_element.remove(tasks_element)
        consumables_element = service_element.find("consumables")
        if consumables_element is not None:
            service_element.remove(consumables_element)
        if service.consumables:
            consumables_element = ET.SubElement(service_element, "consumables")
            for consumable in service.consumables:
                consumable_element = ET.SubElement(consumables_element, "consumable")
                self._consumable_to_xml(consumable, consumable_element)

    def _consumable_to_xml(self, consumable, consumable_element):
        name_element = ET.SubElement(consumable_element, "name")
        name_element.text = consumable.name
        manufacturer_element = ET.SubElement(consumable_element, "manufacturer")
        manufacturer_element.text = consumable.manufacturer
        cost_element = ET.SubElement(consumable_element, "cost")
        cost_element.text = str(consumable.cost)