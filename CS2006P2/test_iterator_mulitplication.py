import unittest
from iterator_intricate_multiplication import *

class TestCommutativeProperty(unittest.TestCase):
    def test_has_commutative_intricate_multiplication(self):
        # Test for n = 4, alpha = 3
        self.assertTrue(iterator_has_commutative_intricate_multiplication(4, 3))
        print("Test for commutative property with n = 4 and alpha = 3 passed.")

    def test_has_commutative_intricate_multiplication_edge_cases(self):
        # Test for n = 1, alpha = 0
        self.assertTrue(iterator_has_commutative_intricate_multiplication(1, 0))
        print("Test for commutative property with n = 1 and alpha = 0 passed.")
        # Test for n = 2, alpha = 0
        self.assertTrue(iterator_has_commutative_intricate_multiplication(2, 0))
        print("Test for commutative property with n = 2 and alpha = 0 passed.")
        # Test for n = 3, alpha = 1
        self.assertTrue(iterator_has_commutative_intricate_multiplication(3, 1))
        print("Test for commutative property with n = 3 and alpha = 1 passed.")
    
    def test_has_commutative_intricate_multiplication_large_values(self):
        # Test for large values of n and alpha
        # Test for n = 1000, alpha = 500
        self.assertTrue(iterator_has_commutative_intricate_multiplication(1000, 500))
        print("Test for commutative property with n = 1000 and alpha = 500 passed.")

    def test_associative_property(self):
        # Test for n = 4, alpha = 3
        self.assertTrue(iterator_has_associative_intricate_multiplication(4, 3))
        print("Test for associative property with n = 4 and alpha = 3 passed.")

    def test_non_associative_property(self):
        # Test for n = 5, alpha = 2
        self.assertFalse(iterator_has_associative_intricate_multiplication(5, 2))
        print("Test for non-associative property with n = 5 and alpha = 2 passed.")

    def test_has_intricate_peculiar_property(self):
    # Test for n = 4, alpha = 3
        self.assertTrue(iterator_has_intricate_peculiar_property(4, 3))
        print("Test for peculiar property with n = 4 and alpha = 3 passed.")

    def test_1_0_edge_case(self):
    # Test for n = 1, alpha = 0
        self.assertTrue(iterator_has_intricate_peculiar_property(1, 0))
        print("Test for peculiar property with n = 1 and alpha = 0 passed.")

    def test_5_0_edge_np_prop(self):
    # Test for n = 5, alpha = 0
        self.assertFalse(iterator_has_intricate_peculiar_property(5, 0))
        print("Test for peculiar property with n = 5 and alpha = 0 passed.")

    def test_no_pec_prop_normal(self):
    # Test for n = 7, alpha = 5 (where alpha != n - 1)
        self.assertFalse(iterator_has_intricate_peculiar_property(7, 5))
        print("Test for peculiar property with n = 7 and alpha = 5 passed.")


if __name__ == '__main__':
    unittest.main()
