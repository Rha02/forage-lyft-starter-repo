
from serviceable import Serviceable


class Car(Serviceable):
    def __init__(self, engine, battery, tire_wear):
        self.engine = engine
        self.battery = battery
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tire_wear.needs_service()
