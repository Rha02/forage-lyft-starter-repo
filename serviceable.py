
from abc import ABC


class Serviceable(ABC):
    def needs_service() -> bool:
        pass