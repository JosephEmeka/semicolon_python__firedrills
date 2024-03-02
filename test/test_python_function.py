import unittest
from unittest import TestCase

import main


class TestMyFunction(unittest.TestCase):
    def test_arrange_list(self):
        self.assertIsNotNone(main.arrange_list)

    def test_arrange_list_in_ascending_order_works(self):
        my_list = [9, 2, 6, 4, 5]
        my_list_output = [2, 4, 5, 6, 9]

        self.assertEqual(my_list_output, main.arrange_list_in_ascending_order(my_list))

    def test_arrange_list_in_descending_order_works(self):
        my_list = [9, 2, 6, 4, 5]
        my_list_output = [9, 6, 5, 4, 2]

        self.assertEqual(my_list_output, main.arrange_list_in_descending_order(my_list))

    class TestThatKeyIsPresentFunction(unittest.TestCase):
        def test_that_function_is_not_none(self):
            self.assertIsNotNone(main.searck_key)
