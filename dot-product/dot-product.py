import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code here
    prod=0
    for i in range(0,len(x)):
        prod+=x[i]*y[i]

    return float(prod)