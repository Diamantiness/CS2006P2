def inputValidator(n, alpha):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Modulus must be positive")
    if not isinstance(alpha, int) or alpha < 0 or alpha >= n:
        raise ValueError("Multiplier  must be in the range [0, n-1]")
    return True
