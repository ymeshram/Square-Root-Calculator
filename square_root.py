import math
def square_root(num):
    if num < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    return math.sqrt(num)
