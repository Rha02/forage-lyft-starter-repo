
import unittest

from tires.carrigan_tires import CarriganTires


class TestCarriganTires(unittest.TestCase):
    def test_should_be_serviced(self):
        tire_wear = CarriganTires([0.4, 0.9, 0.1, 0.3])

        self.assertTrue(tire_wear.needs_service())

    def test_should_not_be_serviced(self):
        tire_wear = CarriganTires([0.4, 0.8, 0.1, 0.3])

        self.assertFalse(tire_wear.needs_service())