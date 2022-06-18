
from tires.tires import Tires


class CarriganTires(Tires):
    def __init__(self, tires):
        self.tires = tires
    
    def needs_service(self) -> bool:
        for tire in self.tires:
            if tire >= 0.9:
                return True
        return False