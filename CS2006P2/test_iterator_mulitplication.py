import unittest
from iterator_intricate_multiplication import *
from intricate_integer import IntricateInteger

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

    def test_intricate_roots_for_each_pair_small_n(self):
        # Test for a small value of n to ensure function correctly counts pairs
        results = intricate_roots_for_each_pair(4)
        expected_results = [(0, 3), (1, 3)]
        self.assertEqual(results, expected_results)
        print("Test for the count of intricate roots for n=4 are passed.")
    
    def test_intricate_roots_for_each_pair_larger_n(self):
        # Test for a larger value of n to check for correct counts in more complex scenarios
        results = intricate_roots_for_each_pair(10)
        expected_results = [(0, 18), (1, 27)]
        self.assertEqual(results, expected_results)
        print("Test for the count of intricate roots for n=10 passed.")
    
    def test_intricate_roots_for_each_pair_no_roots(self):
        # Specifically test cases expected to have no roots for any pair
        results = intricate_roots_for_each_pair(5)
        # Most pairs yield no roots
        expected_results = [(0, 5), (1, 5)] 
        self.assertEqual(results, expected_results)
        print("Test for the count of pairs with no roots for n=5 passed.")

    def setUp(self):
        # Setup intricate integers for following tests
        self.obj1 = IntricateInteger(1, 5, 1)
        self.obj2 = IntricateInteger(2, 5, 1)
        self.obj3 = IntricateInteger(3, 5, 2) # Has different alpha value
        self.obj4 = IntricateInteger(3, 6, 1) # Has different n value

    def test_generator_multi_simple(self):
        # Test with a simple list of IntricateIntegers
        S = [self.obj1, self.obj2]
        result = generator_multi(S)
        # Verify the result contains the expected products
        expected_products = {self.obj1 * self.obj2, self.obj1, self.obj2}
        self.assertEqual(len(result), len(expected_products))
        for product in expected_products:
            self.assertTrue(any(product.object == res.object for res in result))

    def test_generator_multi_single_element(self):
        # Test with a single element list
        S = [self.obj1]
        result = generator_multi(S)
        self.assertTrue(len(result) == 1 and next(iter(result)).object == self.obj1.object)

    def test_generator_multi_empty_input(self):
        # Test with an empty list
        S = []
        result = generator_multi(S)
        self.assertEqual(len(result), 0)

    def test_generator_multi_different_alpha(self):
        # Test with elements having different n or alpha
        S = [self.obj1, self.obj3]  # Different alpha
        result = generator_multi(S)
        self.assertEqual(len(result), 0)

    def test_generator_multi_different_n(self):
        # Test with elements having different n or alpha
        S = [self.obj1, self.obj4]  # Different alpha
        result = generator_multi(S)
        self.assertEqual(len(result), 0)



if __name__ == '__main__':
    unittest.main()