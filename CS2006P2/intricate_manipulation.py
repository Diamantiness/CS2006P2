from intricate_integer import IntricateInteger

def has_intricate_peculiar_property(n, alpha):
    # Iterate over integers in the range [0, n)
    for x in range(n):
        intricate_integer = IntricateInteger(x, n, alpha)
        # Check if the square of intricate_integer equals x
        if (intricate_integer * intricate_integer).object != x:
            return False
    return True

def check_property_for_all_pairs():
    # iterate over all pairs (n, alpha)
    for n in range(1, 51):
        for alpha in range(n):
            property_holds = has_intricate_peculiar_property(n, alpha)
            # ensure property holds iff alpha = n - 1
            if (alpha == n - 1) != property_holds:
                return False
    return True

if __name__ == "__main__":
    # Print whether the property holds for all pairs (n, alpha)
    print(check_property_for_all_pairs())
