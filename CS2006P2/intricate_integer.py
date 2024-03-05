import math

class IntricateInteger:
    def __init__(self, obj, n, alpha):
        """
        Initializes an intricate integer object.

        Parameters:
        - obj (int): The integer value.
        - n (int): The modulus.
        - alpha (int): The multiplier.

        Raises:
        - ValueError: If modulus, multiplier, or integer are invalid.
        """
        if not isinstance(n, int) or n <= 0:  
            raise ValueError("Modulus must be positive")
        if not isinstance(alpha, int) or alpha < 0 or alpha >= n:  
            raise ValueError("Multiplier must be in the range [0, n-1]")
        if not isinstance(obj, int) or obj < 0 or obj >= n:  
            raise ValueError("Input integer must be in the range [0, n-1] (For modulus)")
        
        self.object = obj
        self.n = n
        self.alpha = alpha
    
    def __str__(self):
        """
        Returns a string representation of the intricate integer.

        Returns:
        - str: A string representing the intricate integer in the format "<obj mod n | alpha>".
        """
        return f"<{self.object} mod {self.n} | {self.alpha}>"
    
    def __mul__(self, other):
        """
        Performs multiplication operation between two intricate integers.

        Parameters:
        - other (IntricateInteger): The other intricate integer to multiply with.

        Returns:
        - IntricateInteger: A new intricate integer as a result of the operation.

        Raises:
        - TypeError: If the other argument is not an IntricateInteger.
        - ValueError: If the IntricateIntegers do not share the same modulus and alpha.
        """
        if not isinstance(other, IntricateInteger):
            raise TypeError("Multiplication needs to be between 2 Intricate Integers")
        if self.n != other.n or self.alpha != other.alpha:
            raise ValueError("Intricate Integers need the same modulus and alpha")
        
        lcm = math.lcm(self.object, other.object)
        result = (self.object + other.object + (self.alpha * lcm)) % self.n
        return IntricateInteger(result, self.n, self.alpha)

class IntricateIntegers:
    def __init__(self, n, alpha):
        """
        Initializes a collection of intricate integers.

        Parameters:
        - n (int): The modulus.
        - alpha (int): The multiplier.
        """
        self.n = n
        self.alpha = alpha
        self.elements = [IntricateInteger(i, n, alpha) for i in range(n)]
    
    def __str__(self):
        """
        Returns a string representation of the collection of intricate integers.

        Returns:
        - str: A string representing the collection of intricate integers.
        """
        return ", ".join(str(e) for e in self.elements)
    
    def size(self):
        """
        Returns the number of intricate integers in the collection.

        Returns:
        - int: The number of intricate integers.
        """
        return len(self.elements)
    
    def __iter__(self):
        """
        Initializes the iterator for the collection of intricate integers.

        Returns:
        - Iterator: An iterator object.
        """
        self.index = 0
        return self
    
    def __next__(self):
        """
        Iterates through the collection of intricate integers.

        Returns:
        - IntricateInteger: The next intricate integer in the collection.

        Raises:
        - StopIteration: If there are no more elements to iterate over.
        """
        if self.index < self.size():
            result = self.elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration
