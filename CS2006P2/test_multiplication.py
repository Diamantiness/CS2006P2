import unittest
from intricate_multiplication import *

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
#Lets jut do as many as possible lol        
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
                result = has_associative_intricate_multiplication(n, alpha)
                self.assertTrue(result, f"Associative property failed for n={n}, alpha={alpha}")
                print(f"Test case for n={n}, alpha={alpha}: PASSED (Associative property holds)")

    def test_associative_property_valid_false(self):
        # Test cases where the property is expected to hold false
        non_associative_pairs = [(3, 1), (4, 1), (5, 1)]
        for n, alpha in non_associative_pairs:
            with self.subTest(n=n, alpha=alpha):
                result = has_associative_intricate_multiplication(n, alpha)
                self.assertFalse(result, f"Associative property unexpectedly held for n={n}, alpha={alpha}")
                print(f"Test case for n={n}, alpha={alpha}: PASSED (Associative property does not hold)")

    def test_associative_property_invalid(self):
        # Test cases where values are invalid
        invalid_pairs = [(0, 0), (1, -1), (1, 1), (0, -1)]
        for n, alpha in invalid_pairs:
            with self.subTest(n=n, alpha=alpha):
                with self.assertRaises(ValueError):
                    has_associative_intricate_multiplication(n, alpha)
                print(f"Test case for n={n}, alpha={alpha}: PASSED (ValueError raised)")

    def test_associative_property_for_edge_cases(self):
        # Tests edge cases
        edge_cases = [(1, 0), (2, 1)]
        for n, alpha in edge_cases:
            with self.subTest(n=n, alpha=alpha):
                result = has_associative_intricate_multiplication(n, alpha)
                self.assertTrue(result, f"Associative property edge case failed for n={n}, alpha={alpha}")
                print(f"Test case for n={n}, alpha={alpha}: PASSED (Associative property holds)")

if __name__ == "__main__":
    unittest.main() 
