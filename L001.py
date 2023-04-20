import numpy as np
from math import factorial as fc
import math
from fractions import Fraction

def c (k,n):
    return Fraction(fc(n) // (fc(k)*fc(n-k)))

def a (k,n):
    return Fraction(fc(n) // fc(n-k))

def p (n):
    return fc(n)

# answer = Fraction(c(1,5)*c(2,5)*c(3,10)/c(6,20))
answer = (3**3 / fc(3)) * math.e**(-3)

# print(c(4,7)*c(1,3)/c(5,10))
# print(fc(8)/fc(3)*fc(2))
# print(c(4,13))

print(answer, "=", round(float(answer), 4))
