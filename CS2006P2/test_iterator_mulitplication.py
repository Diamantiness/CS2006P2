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
        # Test for n = 6, alpha = 3
        self.assertTrue(iterator_has_associative_intricate_multiplication(6, 3))
        print("Test for associative property with n = 6 and alpha = 3 passed.")

    def test_non_associative_property(self):
        # Test for n = 5, alpha = 2
        self.assertFalse(iterator_has_associative_intricate_multiplication(5, 2))
        print("Test for non-associative property with n = 5 and alpha = 2 passed.")
        # Test for n = 5, alpha = 4
        self.assertFalse(iterator_has_associative_intricate_multiplication(5, 4))
        print("Test for non-associative property with n = 5 and alpha = 4 passed.")

    def test_has_intricate_peculiar_property(self):
        # Test for n = 4, alpha = 3
        self.assertTrue(iterator_has_intricate_peculiar_property(4, 3))
        print("Test for peculiar property with n = 4 and alpha = 3 passed.")
        # Test for n = 6, alpha = 5
        self.assertTrue(iterator_has_intricate_peculiar_property(6, 5))
        print("Test for peculiar property with n = 6 and alpha = 5 passed.")

    def test_1_0_edge_case(self):
        # Test for n = 1, alpha = 0
        self.assertTrue(iterator_has_intricate_peculiar_property(1, 0))
        print("Test for peculiar property with n = 1 and alpha = 0 passed.")

    def test_5_0_edge_np_prop(self):
        # Test for n = 5, alpha = 0
        self.assertFalse(iterator_has_intricate_peculiar_property(5, 0))
        print("Test for peculiar property with n = 5 and alpha = 0 passed.")
         # Test for n = 8, alpha = 1
        self.assertFalse(iterator_has_intricate_peculiar_property(8, 1))
        print("Test for peculiar property with n = 8 and alpha = 1 passed.")

    def test_no_pec_prop_normal(self):
        # Test for n = 7, alpha = 5 (where alpha != n - 1)
        self.assertFalse(iterator_has_intricate_peculiar_property(7, 5))
        print("Test for peculiar property with n = 7 and alpha = 5 passed.")
        # Test for n = 9, alpha = 7 (where alpha != n - 1)
        self.assertFalse(iterator_has_intricate_peculiar_property(9, 7))
        print("Test for peculiar property with n = 9 and alpha = 7 passed.")


    def test_intricate_roots_of_one(self):
        # Test for n = 4, alpha = 3
        roots1 = intricate_roots_of_one(4, 3)
        expected_roots1 = [1]
        self.assertEqual(roots1, expected_roots1)
        # Test for n = 7, alpha = 3
        roots2 = intricate_roots_of_one(7, 3)
        expected_roots2 = [3]
        self.assertEqual(roots2, expected_roots2)
        print("Test for intricate roots of one passed.")

    def test_intricate_roots_of_one_no_result(self):
        # Test for n = 8, alpha = 2
        roots1 = intricate_roots_of_one(8, 2)
        expected_roots1 = []
        self.assertEqual(roots1, expected_roots1)
        # Test for n = 6, alpha = 1
        roots2 = intricate_roots_of_one(6, 1)
        expected_roots2 = []
        self.assertEqual(roots2, expected_roots2)
        print("Test for intricate roots of one with no result passed.")

    def test_intricate_roots_for_each_pair(self):
        # Test for correctness with specific (n, alpha) pairs
        expected_results_specific = {
            1: [(0, 1)],  # For n=1, expecting one case of 0 roots (if considering Z1 = {0})
            2: [(0, 1), (1, 1)],
        }
        
        # Run tests for n = 1, 2, 3 as examples
        for n, expected in expected_results_specific.items():
            result = intricate_roots_for_each_pair(n)
            # Convert result to count form
            result_count = Counter([res[0] for res in result])
            expected_count = Counter(dict(expected))
            assert result_count == expected_count, f"Failed for n={n}. Expected {expected_count}, got {result_count}"
        
        print("Test for specific cases of intricate roots for each pair passed.")

if __name__ == '__main__':
    unittest.main()
