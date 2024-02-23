import math

class IntricateInteger:
    def __init__(self, obj, n, alpha):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("Modulus must be positive")
        if not isinstance(alpha, int) or alpha < 0 or alpha >= n:
            raise ValueError("Multiplier  must be in the range [0, n-1]")
        if not isinstance(obj, int) or obj < 0 or obj >= n:
            raise ValueError("Input integer must be in the range [0, n-1] (For modulus)")
        
        self.object = obj
        self.n = n
        self.alpha = alpha
    
    def __str__(self):
        return f"<{self.object} mod {self.n} | {self.alpha}>"
    
    def __mul__(self, other):
        if not isinstance(other, IntricateInteger):
            raise TypeError("Multiplication needs to be between 2 Intricate Integers")
        if self.n != other.n or self.alpha != other.alpha:
            raise ValueError("Intricate Integers mneed the same modulus and alpha")
        
        lcm = math.lcm(self.object, other.object)
        result = (self.object + other.object + self.alpha * lcm) % self.n
        return IntricateInteger(result, self.n, self.alpha)
    
class IntricateIntegers:
    def __init__(self, n, alpha):
        self.n = n
        self.alpha = alpha
        self.elements = [IntricateInteger(i, n, alpha) for i in range(n)]
    
    def __str__(self):
        return ", ".join(str(e) for e in self.elements)
    
    def size(self):
        return len(self.elements)
    
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index < self.size():
            result = self.elements[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

