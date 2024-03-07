import unittest

import sentence


class TestSentences(unittest.TestCase):
    def test_first_sentences(self):
        test_input = "hello world! 123"
        expected = "LETTERS 10 DIGITS 3"
        self.assertEqual(expected, sentence.check_number_of_alphabet(test_input))

    def test_cases_of_sentences(self):
        my_sentence = "Hello World"
        expected = "UPPER CASE 2 LOWER CASE 8"
        self.assertEqual(expected, sentence.check_cases_in_sentence(my_sentence))
