import math
import string
import unittest
from unittest.mock import patch

from src.main_oop import (  # Replace 'main' with the actual module name
    MemorablePasswordGenerator, PinCodeGenerator, RandomPasswordGenerator)


class TestPasswordGenerators(unittest.TestCase):

    def test_pin_code_generator(self):
        length = 6
        pin_generator = PinCodeGenerator(length)
        password = pin_generator.generate_password()
        
        # Check length of the generated password
        self.assertEqual(len(password), length)
        # Check if the generated password contains only digits
        self.assertTrue(all(char in string.digits for char in password))

    def test_random_password_generator(self):
        length = 10
        random_generator = RandomPasswordGenerator(length, True, True)
        password = random_generator.generate_password()
        
        # Check length of the generated password
        self.assertEqual(len(password), length)
        
        # Check if the generated password contains allowed characters
        character_set = string.ascii_letters + string.digits + string.punctuation
        self.assertTrue(all(char in character_set for char in password))

    @patch('random.sample')
    def test_memorable_password_generator(self, mock_sample):
        num_words = 4
        separator = '-'
        words_list = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
        
        # Mocking random.sample to return a predictable output
        mock_sample.return_value = words_list[:num_words]
        
        memorable_generator = MemorablePasswordGenerator(num_words, separator, vocabulary=words_list)
        password = memorable_generator.generate_password()
        
        expected_password = 'apple-banana-cherry-date'
        self.assertEqual(password, expected_password)

    def test_calculate_entropy(self):
        length = 6
        pin_generator = PinCodeGenerator(length)
        password = pin_generator.generate_password()
        
        entropy = pin_generator.calculate_entropy(password)
        
        # Expected entropy for a 6-digit PIN (10 possible digits)
        expected_entropy = math.log2(10 ** length)
        self.assertAlmostEqual(entropy, expected_entropy, delta=0.01)


if __name__ == '__main__':
    unittest.main()
