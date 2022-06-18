
from tires.tires import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires):
        self.tires = tires
    
    def needs_service(self) -> bool:
        return sum(self.tires) >= 3