import unittest
from unittest import TestCase
import listTask
from listTask import *




class TestlistTask(unittest.TestCase):
    def test_function_create_list_from_numbers_ranging_from_One_to_fifteen_function(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.assertEqual(my_list, this_list())

    def test_function_that_duplicate_list_item(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                           14, 15]
        self.assertEqual(expected_result, duplicate_list(my_list))

    def test_function_that_eliminates_duplicates_in_list_item(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 12, 13, 14, 15, 16, 17]
        expected_result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
        self.assertEqual(expected_result, eliminate_duplicates(my_list))

    def test_function_that_add_every_third_element(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(18, add_every_third_element(my_list))

    def test_function_that_calculate_sum_of_first_middle_and_last_number_in_a_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(16.5, sum_first_middle_and_last_element(my_list))

