def f(x, y, z):
    """
    test intro
    """
    return (x + y) / z
a = 5
b = 6
c = 7.5


def dn(a, b):
    """
    Divide two numbers.
 
    Parameters
    ----------
    a : float
        The dividend.
    b : float
        The divisor.
 
    Returns
    -------
    float
        The quotient of the division.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
print(dn(3,6))

result = f(a, b, c)