from intricate_integer import IntricateIntegers
from input_validator import inputValidator
from itertools import permutations
from collections import Counter


def iterator_has_commutative_intricate_multiplication(n, alpha):
    """
    Checks if the IntricateIntegers iterator has commutative multiplication.

    Parameters:
    - n (int): The modulus.
    - alpha (int): The multiplier.

    Returns:
    - bool: True if the multiplication is commutative, False otherwise.
    """
    inputValidator(n, alpha)

    intricate_integers = IntricateIntegers(n, alpha)
    for x in intricate_integers:
        for y in intricate_integers:
            if (x * y).object != (y * x).object:
                return False
    return True

def iterator_has_associative_intricate_multiplication(n, alpha):
    """
    Checks if the IntricateIntegers iterator has associative multiplication.

    Parameters:
    - n (int): The modulus.
    - alpha (int): The multiplier.

    Returns:
    - bool: True if the multiplication is associative, False otherwise.
    """
        
        
    inputValidator(n, alpha)

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
    """
    Checks if the IntricateIntegers iterator has the peculiar property.

    Parameters:
    - n (int): The modulus.
    - alpha (int): The multiplier.

    Returns:
    - bool: True if the IntricateIntegers iterator has the peculiar property, False otherwise.
    """
    inputValidator(n, alpha)
    intricate_integers = IntricateIntegers(n, alpha)
    for element in intricate_integers:
        result = element * element
        if result.object != element.object:
            return False
    return True

def intricate_roots_of_one(n, alpha):
    """
    Finds intricate roots of one.

    Parameters:
    - n (int): The modulus.
    - alpha (int): The multiplier.

    Returns:
    - list: List of intricate integers whose square equals one.
    """
    inputValidator(n, alpha)

    root_cases = []
    inputValidator(n, alpha)
    intricate_integers = IntricateIntegers(n, alpha)
    for element in intricate_integers:
        result = element * element
        if result.object == 1:
            root_cases.append(element.object)
    return root_cases


def intricate_roots_for_each_pair(n):
    results = []
    for n in range(0, n):
        for alpha in range(n):
            roots_count = len(intricate_roots_of_one(n, alpha))
            results.append((roots_count, (n, alpha)))

    # Count how many times each number of roots occurs for different pairs
    results_counter = Counter([result[0] for result in results])
    # Format results as list of tuples (number_of_roots, count)
    formatted_results = sorted([(key, value) for key, value in results_counter.items()])

    return formatted_results



def generator_multi(S):
    """
    Generates all possible multiplications of intricate integers from a given list.

    Parameters:
    - S (list): A list of IntricateIntegers.

    Returns:
    - set: Set containing all possible multiplications of intricate integers.
    """
    result = set()

    s_list = list(S)
    alpha = s_list[0].alpha
    n = s_list[0].n

    inputValidator(n, alpha)
        
    # Check if all elements in S have the same alpha and n

    if all(obj.alpha == alpha and obj.n == n for obj in s_list[1:]):
        for i in range(1, len(S) + 1):
            for perm in permutations(S, i):
                # Calculate the product of the elements in the permutation
                product_result = perm[0] 
                for element in perm[1:]:
                    product_result *= element  
                # Check if product_result is not already present in result based on the .object attribute
                if all(product_result.object != intricate.object for intricate in result):
                    result.add(product_result)

    return result
