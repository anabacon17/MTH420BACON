# standard_library.py
"""Python Essentials: The Standard Library.
<Ana Bacon>
<MTH 420>
<04/17/2025>
"""

from math import sqrt


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    minimum = min(L)
    maximum = max(L)
    average = sum(L) / len(L)
    
    return f"{minimum}, {maximum}, {average}"
    
    raise NotImplementedError("Problem 1 Incomplete")


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    test_objects = {
        "integer": 42,
        "string": "hello",
        "list": [1, 2, 3],
        "tuple": (1, 2, 3),
        "set": {1, 2, 3}
    }
    
    for obj_name, obj in test_objects.items():
        try:
            obj[0]
            mutable = False
        except TypeError:
            mutable = True
            
        print(f"{obj_name.capitalize()} is {'mutabel' if mutable else 'immutable'}.")
        
    
    raise NotImplementedError("Problem 2 Incomplete")


# Problem 3

from calculator import sum, product, sqrt

def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    return sqrt(sum([product(a, a), product(b,b)]))
    
    raise NotImplementedError("Problem 3 Incomplete")


# Problem 4
import itertools

def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    power_set_list = []
    for i in range(len(A) + 1):
        subsets = itertools.combinations(A, i)
        power_set_list.extend(set(subset) for subset in subsets)
    return power_set_list
    
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")

    
    
    
    
    
     return f"{minimum}, {maximum}, {average}"
    
    
    print(f"{obj_name.capitalize()} is {'mutabel' if mutable else 'immutable'}.")
    
    
    return sqrt(sum([product(a, a), product(b,b)]))


     return power_set_list

    