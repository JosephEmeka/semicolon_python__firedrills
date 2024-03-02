import unittest

import inputClass


class TestInputClass(unittest.TestCase):
    def test_get_input_test(self):
        sample = inputClass.inputClass()
        sample.getString("hello friends")
        self.assertEqual("HELLO FRIENDS", sample.printString)
