from intricate_integer import IntricateInteger
from input_validator import inputValidator


def has_intricate_peculiar_property(n, alpha):
    inputValidator(n, alpha)
    # Iterate over integers in the range [0, n]
    for x in range(n):
        intricate_integer = IntricateInteger(x, n, alpha)
        # Check if the square of integer equals x
        if (intricate_integer * intricate_integer).object != x:
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

def has_commutative_intricate_multiplication(n, alpha):
    inputValidator(n, alpha)
    for x in range(n):
        for y in range(x+1, n):  # Avoid redundant checks by starting from x+1
            intricate_x = IntricateInteger(x, n, alpha)
            intricate_y = IntricateInteger(y, n, alpha)
            if (intricate_x * intricate_y).object != (intricate_y * intricate_x).object:
                return False
    return True

def check_commutativity_for_all_pairs():
    non_commutative_cases = []
    for n in range(1, 51):
        for alpha in range(n):
            if not has_commutative_intricate_multiplication(n, alpha):
                non_commutative_cases.append((n, alpha))
    return non_commutative_cases

def has_associative_intricate_multiplication(n, alpha):
    inputValidator(n, alpha)
    for x in range(n):
        for y in range(n):
            for z in range(n):
                xy = IntricateInteger(x, n, alpha) * IntricateInteger(y, n, alpha)
                yz = IntricateInteger(y, n, alpha) * IntricateInteger(z, n, alpha)
                left = xy * IntricateInteger(z, n, alpha)
                right = IntricateInteger(x, n, alpha) * yz
                if left.object != right.object:
                    return False
    return True

def check_associativity_for_all_pairs():
    associative_cases = []
    for n in range(1, 20):
        for alpha in range(n):
            if has_associative_intricate_multiplication(n, alpha):
                associative_cases.append((n, alpha))
    return associative_cases

if __name__ == "__main__":
    # Print whether the property holds for all pairs (n, alpha)
    print(check_property_for_all_pairs())
    print(check_commutativity_for_all_pairs())
    print(check_associativity_for_all_pairs())
