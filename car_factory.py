
from abc import ABC
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire_wear = CarriganTires(tires)

        return Car(engine, battery, tire_wear)
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire_wear = CarriganTires(tires)

        return Car(engine, battery, tire_wear)
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on, tires) -> Car:
        engine = SternmanEngine(warning_light_is_on)
        battery = NubbinBattery(last_service_date, current_date)
        tire_wear = CarriganTires(tires)

        return Car(engine, battery, tire_wear)
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire_wear = OctoprimeTires(tires)

        return Car(engine, battery, tire_wear)
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire_wear = OctoprimeTires(tires)

        return Car(engine, battery, tire_wear)