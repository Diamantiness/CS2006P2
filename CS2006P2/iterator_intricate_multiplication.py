from intricate_integer import IntricateIntegers, IntricateInteger
from input_validator import inputValidator
from itertools import product

def iterator_has_commutative_intricate_multiplication(n, alpha):
    intricate_integers = IntricateIntegers(n, alpha)
    for x in intricate_integers:
        for y in intricate_integers:
            if (x * y).object != (y * x).object:
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


def iterator_has_intricate_peculiar_property(n, alpha):
    inputValidator(n, alpha)
    intricate_integers = IntricateIntegers(n, alpha)
    for element in intricate_integers:
        result = element * element
        if result.object != element.object:
            return False
    return True

def intricate_roots_of_one(n, alpha):
    root_cases = []
    inputValidator(n, alpha)
    intricate_integers = IntricateIntegers(n, alpha)
    for element in intricate_integers:
        result = element * element
        if result.object == 1:
            root_cases.append(element.object)
    return root_cases


#https://blog.enterprisedna.co/how-to-generate-all-combinations-of-a-list-in-python/
def generator_multi(S):
    result = set()

    for i in range(1, len(S) + 1):
        combinations = [[]]  # Initialize with an empty subset
        
        # Loop through each element of S to add to existing subsets
        for element in S:
            # For each existing combination, create a new combination that includes the current element
            for sub_set in list(combinations):  # Convert combinations to list to avoid unexpected behavior
                new_sub_set = sub_set + [element]
                combinations.append(new_sub_set)
                print(new_sub_set)
                print()

        # Remove the empty subset from the combinations list
        combinations.pop(0)


        # Iterate over generated combinations and calculate product
        for combo in combinations:
            product_result = combo[0]  # Initialize with the first element
            for element in combo[1:]:
                product_result *= element  # Multiply subsequent elements

            # Check if product_result is not already present in result based on the .object attribute
            if all(product_result.object != intricate.object for intricate in result):
                result.add(product_result)
    return result
