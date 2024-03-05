import time
import math
from intricate_multiplication import *
from iterator_intricate_multiplication import *

def compareTime():
       
    """
    Compares the execution time of old and new functions for checking intricate integer properties.

    Prints the results of various checks and the time taken by each operation.
    """
    # Time taken by old functions
    start_time_old = time.time()
    old_associative_result = check_associativity_for_all_pairs()
    old_associative_time = time.time() - start_time_old

    start_time_old = time.time()
    old_commutative_result = check_commutativity_for_all_pairs()
    old_commutative_time = time.time() - start_time_old

    start_time_old = time.time()
    old_property_result = check_property_for_all_pairs()
    old_property_time = time.time() - start_time_old

    # Time taken by new functions
    start_time_new = time.time()
    new_associative_result = iterator_check_associativity_for_all_pairs()
    new_associative_time = time.time() - start_time_new

    start_time_new = time.time()
    new_commutative_result = iterator_check_commutativity_for_all_pairs()
    new_commutative_time = time.time() - start_time_new

    start_time_new = time.time()
    new_property_result = iterator_check_property_for_all_pairs()
    new_property_time = time.time() - start_time_new

    # Print results
    print("== Old Function Results ==")
    print("Associative Check Result:", old_associative_result)
    print("Time taken for Associative Check:", old_associative_time)
    print("Commutative Check Result:", old_commutative_result)
    print("Time taken for Commutative Check:", old_commutative_time)
    print("Property Check Result:", old_property_result)
    print("Time taken for Property Check:", old_property_time)

    print("\n== New Function Results ==")
    print("Associative Check Result:", new_associative_result)
    print("Time taken for Associative Check:", new_associative_time)
    print("Commutative Check Result:", new_commutative_result)
    print("Time taken for Commutative Check:", new_commutative_time)
    print("Property Check Result:", new_property_result)
    print("Time taken for Property Check:", new_property_time)

    # Finding roots of one
    print("\nFinding roots of one...")
    start_time_roots = time.time()
    check_nr_roots_of_one()
    roots_time = time.time() - start_time_roots
    print("Time taken to find roots of one:", roots_time)

    # Finding counterexample
    print('\nFinding counterexample...')
    start_time_counterexample = time.time()
    find_counterexample()
    counterexample_time = time.time() - start_time_counterexample
    print("Time taken to find counterexample:", counterexample_time)

    # Generating intricate integers using generator_multi
    print("\nGenerated intricate integers using generator_multi:")
    start_time_generator = time.time()
    for integer in generator_multi({IntricateInteger(2, 7, 1), IntricateInteger(3, 7, 1), IntricateInteger(5, 7, 1)}):
        print(integer)
    generator_time = time.time() - start_time_generator
    print("Time taken to generate intricate integers using generator_multi:", generator_time)

    # Overall time
    overall_time = old_associative_time + old_commutative_time + old_property_time + new_associative_time + new_commutative_time + new_property_time + roots_time + counterexample_time + generator_time
    print("\nOverall time:", overall_time)
def iterator_check_associativity_for_all_pairs():
    """
    Checks if the iterator of intricate integers has associative multiplication for all pairs (n, alpha).

    Returns:
    - list: List of pairs (n, alpha) for which the multiplication is associative.
    """
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if iterator_has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases

def iterator_check_commutativity_for_all_pairs():
    """
    Checks if the iterator of intricate integers has commutative multiplication for all pairs (n, alpha).

    Returns:
    - bool: True if the multiplication is commutative for all pairs, False otherwise.
    """
    for n in range(1, 51):
        for alpha in range(n):
            if not iterator_has_commutative_intricate_multiplication(n, alpha):
                return False
    return True

def check_property_for_all_pairs():
    """
    Checks if the intricate integer property holds for all pairs (n, alpha).

    Returns:
    - bool: True if the property holds for all pairs, False otherwise.
    """
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = has_intricate_peculiar_property(n, alpha)
            if (alpha == n - 1) != property_holds:
                return False
    return True

def iterator_check_property_for_all_pairs():
    """
    Checks if the iterator of intricate integers has the intricate integer property for all pairs (n, alpha).

    Returns:
    - bool: True if the property holds for all pairs, False otherwise.
    """
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = iterator_has_intricate_peculiar_property(n, alpha)
            if (alpha == n - 1) != property_holds:
                return False
    return True
    
def check_commutativity_for_all_pairs():
    """
    Checks if the intricate integer multiplication is commutative for all pairs (n, alpha).

    Returns:
    - bool: True if the multiplication is commutative for all pairs, False otherwise.
    """
    for n in range(1, 51):
        for alpha in range(n):
            if not has_commutative_intricate_multiplication(n, alpha):
                return False
    return True

def check_associativity_for_all_pairs():
    """
    Checks if the intricate integer multiplication is associative for all pairs (n, alpha).

    Returns:
    - list: List of pairs (n, alpha) for which the multiplication is associative.
    """
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases

def check_nr_roots_of_one():
    """
    Checks the number of roots of one for each pair (n, alpha) within a certain range.

    Prints the number of roots of one and their values for each pair (n, alpha).
    """
    for n in range(1, 26):
        for alpha in range(n):
            roots = intricate_roots_of_one(n, alpha)
            print(f"For n={n}, alpha={alpha}: Number of roots = {len(roots)}, Roots = {roots}")

def find_counterexample():
    """
    Finds a counterexample where intricate roots of one exist for pairs (n, alpha) that violate certain conditions.
    """
    for n in range(1, 100):
        for alpha in range(1, n, 2): 
            if math.gcd(n, alpha) != 1:
                roots = intricate_roots_of_one(n, alpha)
                if len(roots) > 0:
                    print(f"Counterexample found! n = {n}, alpha = {alpha}")
                    return

compareTime()
