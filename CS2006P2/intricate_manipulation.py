from intricate_integer import IntricateInteger

def has_intricate_peculiar_property(n, alpha):
    # Iterate over integers in the range [0, n)
    for x in range(n):
        intricate_integer = IntricateInteger(x, n, alpha)
        # Check if the square of integer equals x
        if (intricate_integer * intricate_integer).object != x:
            return False
    return True

def has_commutative_intricate_multiplication(n, alpha):
    # Iterate over integers in the range [0, n)
    for x in range(n):
        for y in range(n):
        intricate_integerX = IntricateInteger(x, n, alpha)
        intricate_integerY = IntricateInteger(y,n,alpha)
        # Check if the square of integer equals x
        if (intricate_integerX * intricate_integerY).object != (intricate_integerY * intricate_integerX).object:
            return False
    return True

def check_commutativity_for_all_pairs():
    non_commutative_pairs = []
    # iterate over all pairs (n, alpha)
    for n in range(1, 51):
        for alpha in range(n):
            if not has_commutative_intricate_multiplication(n, alpha):
                non_commutative_pairs.append((n, alpha))
    return non_commutative_pairs

if __name__ == "__main__":
    # Print whether the property holds for all pairs (n, alpha)
    print(check_property_for_all_pairs())
