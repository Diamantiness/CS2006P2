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
        print(f"Test valid case (n={n}, alpha={alpha}): PASSED")

    def test_has_intricate_peculiar_property_valid_false(self):
        # Test a valid case where the property holds false
        n = 5
        alpha = 2
        result = has_intricate_peculiar_property(n, alpha)
        self.assertFalse(result)
        print(f"Test valid case (n={n}, alpha={alpha}): PASSED")

        #CHECK THUS
    def test_has_intricate_peculiar_property_invalid_n_zero(self):
        # Test an invalid case where n is zero
        n = 0
        alpha = 3
        with self.assertRaises(ValueError):
            has_intricate_peculiar_property(n, alpha)
        print(f"Test invalid case (n={n}, alpha={alpha}): PASSED")

    def test_invalid_alpha_out_of_range(self):
        # Test an invalid case where alpha is out of range [0, n-1]
        n = 4
        alpha = 5
        with self.assertRaises(ValueError):
            has_intricate_peculiar_property(n, alpha)
        print(f"Test invalid case (n={n}, alpha={alpha}): PASSED")

    def test_check_property_requirements(self):
        # Test the property holds for all pairs (n, alpha)
        for n in range(1, 51):
            for alpha in range(n):
                property_holds = has_intricate_peculiar_property(n, alpha)
                # ensure property holds iff alpha = n - 1
                self.assertEqual((alpha == n - 1), property_holds)
        print("Test property holds for all pairs: PASSED")
            
# Would you rather do tests like the ones above or multiple in one like the one below?
         
    def test_has_intricate_peculiar_property_invalid(self):
        # Test multiple different invalid cases
        invalid_pairs =[(0, 0), #invalid as n is zero
                        (1, -1), #both invalid as alpha is out of range
                        (1, 1),
                        (0,-1)]  #invalid as both n and alpha are invalid
        for n, alpha in invalid_pairs:
            with self.subTest(n=n, alpha=alpha):
                with self.assertRaises(ValueError):
                    has_intricate_peculiar_property(n, alpha)
                    
class TestCommutativeMultiplication(unittest.TestCase):
    def test_commutative_property_valid_true(self):
        # Test cases where the property holds true
        commutive_pairs = [(7, 2), (5, 1),(3, 0)]
        for n, alpha in commutive_pairs:
            with self.subTest(n=n, alpha=alpha):
                self.assertTrue(has_commutative_intricate_multiplication(n, alpha), f"Commutative property failed for n={n}, alpha={alpha}")

    #Cannot test cases where property holds false as no combination can result false

    def test_commutative_property_invalid(self):
        # Test cases where values are invalid
        invalid_pairs = [(0, 0), #invalid as n is zero
                         (1, -1), #both invalid as alpha is out of range
                         (1, 1),
                         (0,-1)]  #invalid as both n and alpha are invalid
        for n, alpha in invalid_pairs:
            with self.subTest(n=n, alpha=alpha):
                with self.assertRaises(ValueError):
                    has_commutative_intricate_multiplication(n, alpha)
                
    def test_commutative_property_for_edge_cases(self):
        # Tests edge cases
        edge_cases = [(1, 0),(2, 1)]
        for n, alpha in edge_cases:
            with self.subTest(n=n, alpha=alpha):
                self.assertTrue(has_commutative_intricate_multiplication(n, alpha), f"Commutative property edge case failed for n={n}, alpha={alpha}")
    
class TestAssociativeMultiplication(unittest.TestCase):
    def test_associative_property_valid_true(self):
        # Test cases where the property is expected to hold true
        associative_pairs = [(1, 0), (14, 7), (8, 4)]
        for n, alpha in associative_pairs:
            with self.subTest(n=n, alpha=alpha):
                self.assertTrue(has_associative_intricate_multiplication(n, alpha), f"Associative property failed for n={n}, alpha={alpha}")
                
    def test_associative_property_valid_false(self):
        # Test cases where the property is expected to hold false
        non_associative_pairs = [(3, 1), (4, 1), (5, 1)]
        for n, alpha in non_associative_pairs:
            with self.subTest(n=n, alpha=alpha):
                self.assertFalse(has_associative_intricate_multiplication(n, alpha), f"Associative property unexpectedly held for n={n}, alpha={alpha}")

    def test_associative_property_invalid(self):
        # Test cases where values are invalid
        invalid_pairs = [(0, 0),  # invalid as n is zero
                         (1, -1),  # both invalid as alpha is out of range
                         (1, 1),
                         (0, -1)]  # invalid as both n and alpha are invalid
        for n, alpha in invalid_pairs:
            with self.subTest(n=n, alpha=alpha):
                with self.assertRaises(ValueError):
                    has_associative_intricate_multiplication(n, alpha)

    def test_associative_property_for_edge_cases(self):
        # Tests edge cases
        edge_cases = [(1, 0), (2, 1)]
        for n, alpha in edge_cases:
            with self.subTest(n=n, alpha=alpha):
                self.assertTrue(has_associative_intricate_multiplication(n, alpha), f"Associative property edge case failed for n={n}, alpha={alpha}")

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
