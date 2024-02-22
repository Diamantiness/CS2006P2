import unittest
from intricate_integer import IntricateInteger
from intricate_manipulation import has_intricate_peculiar_property

class TestIntricateInteger(unittest.TestCase):
    def test_valid_instantiation(self):
        # Test valid instantiation of IntricateInteger objects
        x = IntricateInteger(3, 7, 2)
        self.assertEqual(str(x), "<3 mod 7 | 2>")
        print("Test valid instantiation: PASSED")
        
    def test_invalid_instantiation_out_of_range(self):
        # Test invalid instantiation: Object outside the range [0, n-1]
        with self.assertRaises(ValueError):
            IntricateInteger(10, 7, 2)
        print("Test invalid instantiation (out of range): PASSED")
        
    def test_invalid_instantiation_zero_modulus(self):
        # Test invalid instantiation: Modulus <= 0
        with self.assertRaises(ValueError):
            IntricateInteger(3, 0, 2)
        print("Test invalid instantiation (zero modulus): PASSED")
        
    def test_invalid_instantiation_out_of_range_multiplier(self):
        # Test invalid instantiation: Multiplier outside the range [0, n-1]
        with self.assertRaises(ValueError):
            IntricateInteger(3, 7, 8)
        print("Test invalid instantiation (out of range multiplier): PASSED")
        
    def test_multiply(self):
        # Test multiplication of IntricateInteger objects
        x = IntricateInteger(3, 7, 2)
        y = IntricateInteger(5, 7, 2)
        
        xy = x * y
        self.assertEqual(str(xy), "<3 mod 7 | 2>")
        
        xx = x * x
        self.assertEqual(str(xx), "<5 mod 7 | 2>")
        print("Test multiplication: PASSED")
        
    def test_incompatible_operands_different_modulus(self):
        # Test multiplication with incompatible operands: Different modulus
        x = IntricateInteger(3, 7, 2)
        z = IntricateInteger(3, 5, 2)
        
        with self.assertRaises(ValueError):
            x * z
        print("Test incompatible operands (different modulus): PASSED")
        
    def test_incompatible_operands_different_multiplier(self):
        # Test multiplication with incompatible operands: Different multiplier
        x = IntricateInteger(3, 7, 2)
        w = IntricateInteger(3, 7, 3)
        
        with self.assertRaises(ValueError):
            x * w
        print("Test incompatible operands (different multiplier): PASSED")
        
    def test_edge_cases_modulus_one(self):
        # Test edge case: Modulus is 1
        a = IntricateInteger(0, 1, 0)
        self.assertEqual(str(a), "<0 mod 1 | 0>")
        print("Test edge case (modulus 1): PASSED")
        
    def test_edge_cases_multiplier_zero(self):
        # Test edge case: Multiplier is 0
        b = IntricateInteger(3, 5, 0)
        self.assertEqual(str(b), "<3 mod 5 | 0>")
        print("Test edge case (multiplier 0): PASSED")
        
    def test_edge_cases_object_zero(self):
        # Test edge case: Object is 0
        c = IntricateInteger(0, 7, 2)
        self.assertEqual(str(c), "<0 mod 7 | 2>")
        print("Test edge case (object 0): PASSED")

class TestPeculiarProperty(unittest.TestCase):
    def test_has_intricate_peculiar_property_valid_true(self):
        # Test a valid case where the property holds true
        n = 7
        alpha = 6
        result = has_intricate_peculiar_property(n, alpha)
        self.assertTrue(result)

    def test_has_intricate_peculiar_property_valid_false(self):
        # Test a valid case where the property holds false
        n = 5
        alpha = 2
        result = has_intricate_peculiar_property(n, alpha)
        self.assertFalse(result)

    def test_has_intricate_peculiar_property_invalid_n_zero(self):
        # Test an invalid case where n is zero
        n = 0
        alpha = 3
        with self.assertRaises(ValueError):
            has_intricate_peculiar_property(n, alpha)

    def test_has_intricate_peculiar_property_invalid_alpha_out_of_range(self):
        # Test an invalid case where alpha is out of range [0, n-1]
        n = 4
        alpha = 5
        with self.assertRaises(ValueError):
            has_intricate_peculiar_property(n, alpha)

if __name__ == "__main__":
    unittest.main()
