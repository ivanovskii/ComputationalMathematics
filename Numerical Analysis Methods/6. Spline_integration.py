from math import *
from scipy.misc import derivative as diff


def spline_integrate(f, a, b, n=10):
    """
    The function to calculate a definite integral using splines

    Parameters: 
        f (function object): The integration function
        a, b (int, int): The integration segment
        n (int): The number of segments

    Returns:
        int: Returns the area of a curved trapezoid
    """

    h = (b-a) / n
    w = [a + i*h for i in range(n+1)]
    M = [diff(f, x , 2) for x in w]
    
    return sum([0.5*h*(f(w[i])+f(w[i+1])) - h**3 / (24*(M[i] + M[i+1])) for i in range(n)])

# f - The integration function
# a, b - The integration segment
f = lambda x: x**3 + sin(x)
a, b = 0.6, 1.1

print(spline_integrate(f, a, b))