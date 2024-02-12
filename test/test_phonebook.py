import unittest
from unittest import TestCase, result

import phonebook
from phonebook import *


class TestPhonebook(unittest.TestCase):
    def setUp(self):
        phonebook.add_contact("joseph", "07062599764")
        phonebook.add_contact("Samuel", "09081234563")

    def tearDown(self):
        contacts.clear()

    def test_that_contact_is_added_to_phonebook_contact(self):
        phonebook.add_contact("daniel", "08179120472")
        self.assertEqual(3, len(phonebook.contacts))

    def test_that_function_returns_list_of_contacts(self):
        expected_contacts = {'John': ['09087654321', '08176543210'], 'Hannah': ['07065771212'],
                             'jumoke': ['09099888776', '08111223333']}
        actual_contacts = phonebook.list_contacts()

        self.assertEqual(actual_contacts, expected_contacts)
