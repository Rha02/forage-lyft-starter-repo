
import unittest
from tires.octoprime_tires import OctoprimeTires


class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tire_wear = OctoprimeTires([0, 1, 1, 1])

        self.assertTrue(tire_wear.needs_service())

    def test_should_not_be_serviced(self):
        tire_wear = OctoprimeTires([0.5, 0.9, 0.1, 0.5])

        self.assertFalse(tire_wear.needs_service())