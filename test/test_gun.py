import unittest

from Gun import *


class TestGun(unittest.TestCase):

    def test_that_Gun_can_be_loaded(self):
        my_gun = Gun("Pistol")
        my_gun.load(10)
        expected = my_gun.get_total_number_of_bullets()
        self.assertEqual(expected, 10)

    def test_that_gun_can_be_unloaded(self):
        my_gun = Gun("Pistol")
        my_gun.load(9)
        my_gun.unload_some_bullet(4)
        expected = 5
        self.assertEqual(5, my_gun.get_total_number_of_bullets())

    def test_that_all_bullets_can_be_unloaded(self):
        my_gun = Gun("Pistol")
        my_gun.load(9)
        my_gun.unload_all_bullet()
        expected_bullets = 0
        self.assertEqual(expected_bullets, my_gun.get_total_number_of_bullets())

    def test_that_negative_bullets_cannot_be_added(self):
        my_gun = Gun("Pistol")
        with self.assertRaises(ValueError):
            my_gun.load(-9)

    def test_that_negative_bullets_cannot_be_unloaded(self):
        my_gun = Gun("Pistol")
        my_gun.load(12)
        with self.assertRaises(ValueError):
            my_gun.unload_some_bullet(-4)
