import unittest

from logistics_calculator import LogisticsCalculator


class TestLogisticsCalculator(unittest.TestCase):
    def test_logistics_calculator(self):
        my_logistics_calculator = LogisticsCalculator()
        self.assertEqual(45_000, my_logistics_calculator.calculate_delivery(80))
        self.assertEqual(22_000, my_logistics_calculator.calculate_delivery(68))
        self.assertEqual(16_000, my_logistics_calculator.calculate_delivery(55))
        self.assertEqual(9_000, my_logistics_calculator.calculate_delivery(25))


