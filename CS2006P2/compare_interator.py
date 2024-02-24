import time
from intricate_multiplication import *
from iterator_intricate_multiplication import *
def compareTime():
    start_time_old = time.time()
    old_associative_result = check_associativity_for_all_pairs()
    old_commutative_result = check_commutativity_for_all_pairs()
    old_property_result = check_property_for_all_pairs()
    old_time = time.time() - start_time_old

    start_time_new = time.time()
    new_associative_result = iterator_check_associativity_for_all_pairs()
    new_commutative_result = iterator_check_commutativity_for_all_pairs()
    new_property_result = iterator_check_property_for_all_pairs()
    new_time = time.time() - start_time_new

    print("Old Associative Check Result:", old_associative_result)
    print("New Associative Check Result:", new_associative_result)
    print("Old Commutative Check Result:", old_commutative_result)
    print("New Commutative Check Result:", new_commutative_result)
    print("Old Property Check Result:", old_property_result)
    print("New Property Check Result:", new_property_result)

    print("Time taken by old functions:", old_time)
    print("Time taken by new functions:", new_time)

    print("Finding roots of one...")
    check_nr_roots_of_one()


def iterator_check_property_for_all_pairs():
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = iterator_has_intricate_peculiar_property(n, alpha)
            if (alpha == n - 1) != property_holds:
                return False
    return True



def iterator_check_associativity_for_all_pairs():
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if iterator_has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases



def iterator_check_commutativity_for_all_pairs():
    non_commutative_cases = []
    for n in range(1, 51):
        for alpha in range(n):
            if not iterator_has_commutative_intricate_multiplication(n, alpha):
                return False
    return True


def check_property_for_all_pairs():
    # Iterate over all pairs (n, alpha)
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = has_intricate_peculiar_property(n, alpha)
            # Ensure property holds iff alpha = n - 1
            if (alpha == n - 1) != property_holds:
                return False
    return True


def check_commutativity_for_all_pairs():
    for n in range(1, 51):
        for alpha in range(n):
            if not has_commutative_intricate_multiplication(n, alpha):
                return False
    return True


def check_associativity_for_all_pairs():
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases

def check_nr_roots_of_one():
    for n in range(1, 25):
        for alpha in range(n):
           nr_count_cases = intricate_roots_of_one(n, alpha)
           print(nr_count_cases)
compareTime()
