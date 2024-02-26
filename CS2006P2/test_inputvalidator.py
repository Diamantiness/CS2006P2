import unittest
from input_validator import inputValidator

class TestInputValidator(unittest.TestCase):

    def test_valid_input(self):
        # Test with valid inputs
        self.assertTrue(inputValidator(5, 2))  # Modulus = 5, Alpha = 2
        print("Test for valid inputs passed.")

    def test_invalid_modulus(self):
        # Test with invalid modulus
        with self.assertRaises(ValueError):
            inputValidator(0, 2)  # Modulus is not positive
        print("Test for invalid modulus passed.")

    def test_invalid_alpha_range(self):
        # Test with invalid alpha range
        with self.assertRaises(ValueError):
            inputValidator(5, -1)  # Alpha is negative
        with self.assertRaises(ValueError):
            inputValidator(5, 5)   # Alpha is equal to modulus
        with self.assertRaises(ValueError):
            inputValidator(5, 6)   # Alpha is greater than modulus
        print("Test for invalid alpha range passed.")

    def test_invalid_type(self):
        # Test with invalid type for n
        with self.assertRaises(ValueError):
            inputValidator("5", 2)  # Modulus is not an integer
        # Test with invalid type for alpha
        with self.assertRaises(ValueError):
            inputValidator(5, 2.0)   # Alpha is not an integer
        print("Test for invalid types passed.")

if __name__ == '__main__':
    unittest.main()
