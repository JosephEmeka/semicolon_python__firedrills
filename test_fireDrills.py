import unittest
from unittest import TestCase

import fireDrills


class TestMyFunction(unittest.TestCase):
    def test_function_get_length_of_list_without_using_length_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        self.assertEqual(10, fireDrills.get_length_of_list_without_using_length_function(my_list))


class Test(TestCase):
    def sum_of_items_in_even_positions_of_list_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        outcome = 50
        self.assertEqual(46, fireDrills.sum_of_items_in_even_positions_of_list_function(my_list))


class Test(TestCase):
    def test_function_get_average_of_number_in_list_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        self.assertEqual(130, fireDrills.function_get_average_of_number_in_list_function(my_list))


class Test(TestCase):
    def test_sum_of_items_in_odd_positions_of_list_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        outcome = 50
        self.assertEqual(outcome, fireDrills.sum_of_items_in_odd_positions_of_list_function(my_list))


class Test(TestCase):
    def test_get_the_smallest_element_in_list_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        outcome = 50
        self.assertEqual(outcome, fireDrills.get_the_smallest_element_in_list_function(my_list))


class Test(TestCase):
    def test_get_the_largest_element_in_list_function(self):
        my_list = [1, 6, 11, 16, 21, 26, 31, 36, 41, 46]
        outcome = 50
        self.assertEqual(outcome, fireDrills.get_the_largest_element_in_list_function(my_list))
