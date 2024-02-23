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

def has_commutative_intricate_multiplication(n, alpha):
    inputValidator(n, alpha)
    for x in range(n):
        for y in range(x+1, n):  # Avoid redundant checks by starting from x+1
            intricate_x = IntricateInteger(x, n, alpha)
            intricate_y = IntricateInteger(y, n, alpha)
            if (intricate_x * intricate_y).object != (intricate_y * intricate_x).object:
                return False
    return True

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
