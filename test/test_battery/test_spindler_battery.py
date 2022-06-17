
import datetime
import unittest

from battery.nubbin_battery import NubbinBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        today = datetime.datetime.today()
        last_service_date = today.replace(year=today.year-3)
        battery = NubbinBattery(last_service_date, today)

        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        today = datetime.datetime.today()
        last_service_date = today.replace(year=today.year-1)
        battery = NubbinBattery(last_service_date, today)

        self.assertFalse(battery.needs_service())