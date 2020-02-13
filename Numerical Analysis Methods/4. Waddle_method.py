import math


def waddle_method(f, a, b, n=10):
    """ 
    The function to calculate a definite integral by the Weddle method
    
    Parameters: 
        f (function object): The integration function
        a, b (int, int): The integration segment
        n (int): The number of segments

    Returns:
        int: Returns the area of a curved trapezoid
    """

    h = (b-a) / n # Step of each segment
    z = h / 6 # Dividing a segment into 6 equal parts

    return sum([0.3*(f(a + i*h - 6*z) + 5*f(a + i*h - 5*z) + \
        f(a + i*h - 4*z) + 6*f(a + i*h - 3*z) + f(a + i*h - 2*z) + \
        5*f(a + i*h - z) + f(a + i*h)) for i in range(1, n + 1)]) * z


def integrate(f, a, b, n, eps=1e-6):
    I1, I2 = waddle_method(f, a, b, n), waddle_method(f, a, b, n + 1)
    return I2 if (abs(I1 - I2) <= eps) else integrate(f, a, b, n + 1, eps)


# f - The integration function
# a, b - The integration segment
f = lambda x: x**3 + math.sin(x)
a, b = 0.6, 1.1
eps = 1e-16

print(integrate(f, a, b, 1, eps = eps))