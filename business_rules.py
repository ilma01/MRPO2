from datetime import datetime, timedelta

#Обслуживание автомобиля должно проводиться только после достижения определенного пробега или истечения определенного времени с последнего обслуживания
def check_service_due(car, current_date):
    service_interval_mileage = 5000  # Интервал обслуживания по пробегу
    service_interval_months = 6    # Интервал обслуживания в месяцах

    if car.mileage - car.last_service_mileage >= service_interval_mileage:
        print('Достиг достаточный пробег для обслуживания автомобиля')
        return True
    elif current_date - car.last_service_date >= timedelta(days=30 * service_interval_months):
        print ('Прошло достаточно времени для обслуживания автомобиля')
        return True
    else:
        print(f'Автомобиль {car.model.brand.name} {car.model.name} еще не достиг пробега для обслуживания или прошло мало времени с момента последнего обслуживания')
        return False

#При обслуживании автомобиля должны использоваться только рекомендованные производителем расходные материалы
def check_recommended_consumables(service):
    for consumable in service.consumables:
        if consumable not in service.car.model.recommended_parts:
            print (f'При обслуживании использовался расходник {consumable.name}, которого нет в списке рекомендованных производителем {service.car.model.brand.name} {service.car.model.name}')
            return False
    print ('Все расходники, использованные при обслуживании автомобиля рекомендованы для использования производителем')
    return True
#Для каждого обслуживания должен быть предоставлен полный список затраченных материалов
def check_service_consumables(service):
    if not service.consumables:
        print (f'При ТО {service.date.strftime("%Y.%m.%d")} не был представлен список затраченных материалов')
        return False
    else:
        print (f'Список затраченных материалов у ТО {service.date.strftime("%Y.%m.%d")}:')
        for con in service.consumables:
            print (f'{con.name} - {con.manufacturer}')
        return True
#Пробег автомобиля не может быть отрицательным
def check_mileage_non_negative(car):
    if car.mileage >= 0:
        print (f'Пробег {car.model.brand.name} {car.model.name} не отрицательный')
        return True
    print(f'Пробег {car.model.brand.name} {car.model.name} отрицательный')
    return False

