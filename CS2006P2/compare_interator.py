import time
from intricate_integer import IntricateInteger, IntricateIntegers
from intricate_multiplication import check_commutativity_for_all_pairs, check_associativity_for_all_pairs, check_property_for_all_pairs
from input_validator import inputValidator

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

def iterator_has_intricate_peculiar_property(n, alpha):
    inputValidator(n, alpha)
    intricate_integers = IntricateIntegers(n, alpha)
    for element in intricate_integers:
        result = element * element
        if result.object != element.object:
            return False
    return True

def iterator_check_property_for_all_pairs():
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = iterator_has_intricate_peculiar_property(n, alpha)
            if (alpha == n - 1) != property_holds:
                return False
    return True

def iterator_has_associative_intricate_multiplication(n, alpha):
    for element_x in IntricateIntegers(n, alpha):
        for element_y in IntricateIntegers(n, alpha):
            for element_z in IntricateIntegers(n, alpha):
                xy = element_x * element_y
                yz = element_y * element_z
                left = xy * element_z
                right = element_x * yz
                if left.object != right.object:
                    return False
    return True

def iterator_check_associativity_for_all_pairs():
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if iterator_has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases

def iterator_has_commutative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for x in intricate_integers:
        for y in intricate_integers:
            if (x * y).object != (y * x).object:
                return False
    return True

def iterator_check_commutativity_for_all_pairs():
    non_commutative_cases = []
    for n in range(1, 51):
        for alpha in range(n):
            if not iterator_has_commutative_intricate_multiplication(n, alpha):
                non_commutative_cases.append((n, alpha))
    return non_commutative_cases

compareTime()
