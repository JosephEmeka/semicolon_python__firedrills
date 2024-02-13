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

    def test_function_that_takes_a_set_and_returns_element_sum(self):
        my_set = {1, 2, 3, 4, 5, 6}
        self.assertEqual(21, sum_collection(my_set))

    def test_function_that_takes_a_set_and_removes_element_set(self):
        my_set = {1, 2, 3, 4, 5, 6}
        number = 3
        self.assertEqual(3, remove_item(my_set, number))

    def test_function_that_takes_two_sets_and_returns_new_set_intersection(self):
        my_first_set = {1, 2, 3, 4, 5, 6}
        my_second_set = {3, 5, 7, 8, 9}
        expected_intersection = {3, 5}
        self.assertEqual(expected_intersection, find_intersection(my_first_set, my_second_set))

    def test_function_to_replace_first_two_string_elements(self):
        my_string = "abc"
        my_sec_string = "xyz"
        more_string = "abcde"
        much_more_string = "vwxyz"
        result = "xyc abz"
        more_result = "vwcde abxyz"
        self.assertEqual(result, find_intersection_set(my_string, my_sec_string))
        self.assertEqual(more_result, find_intersection_set(more_string, much_more_string))