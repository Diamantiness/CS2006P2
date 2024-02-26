import unittest
from intricate_integer import IntricateInteger, IntricateIntegers
from intricate_multiplication import has_commutative_intricate_multiplication, has_associative_intricate_multiplication,has_intricate_peculiar_property


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

    def test_type_error(self):
        with self.assertRaises(TypeError):
            x = IntricateInteger(3, 7, 2)
            y = 4
            xy = x * y
        print("Test 1 tpye error: PASSED")

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


class TestIntricateIntegers(unittest.TestCase):
    def test_creation_and_size(self):
        # Test creation of IntricateIntegers and size method
        n = 5
        alpha = 2
        intricate_set = IntricateIntegers(n, alpha)
        self.assertEqual(intricate_set.size(), n)
        print("Test creation and size: PASSED")
        
    def test_string_representation(self):
        # Test string representation of IntricateIntegers
        n = 3
        alpha = 1
        intricate_set = IntricateIntegers(n, alpha)
        expected_str = "<0 mod 3 | 1>, <1 mod 3 | 1>, <2 mod 3 | 1>"
        self.assertEqual(str(intricate_set), expected_str)
        print("Test string representation: PASSED")
        
    def test_iteration(self):
        # Test iteration over IntricateIntegers
        n = 4
        alpha = 3
        intricate_set = IntricateIntegers(n, alpha)
        expected_elements = [IntricateInteger(i, n, alpha) for i in range(n)]
        for element, expected_element in zip(intricate_set, expected_elements):
            self.assertEqual(str(element), str(expected_element))
        print("Test iteration: PASSED")

if __name__ == "__main__":
    unittest.main() 
