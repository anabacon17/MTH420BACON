# standard_library.py
"""Python Essentials: The Standard Library.
<Ana Bacon>
<MTH 420>
<04/17/2025>
"""

from math import sqrt
import calculator
from itertools import combinations


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    minimum = min(L)
    maximum = max(L)
    average = sum(L) / len(L)
    
    return minimum, maximum, average
    

# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    int_1=4
    int_2 = int_1
    int_2 +=1
    is_equal = int_1 == int_2
    print(is_equal)
    if is_equal:
        print("mutable")
    else:
        print("immutable")
        
    str_1="hello"
    str_2=str_1
    str_2 += "world"
    is_equal = str_1 == str_2
    print(is_equal)
    if is_equal:
        print("mutable")
    else:
        print("immutable")
    
    
    list_1 = [1,2,3]
    list_2 = list_1
    list_2.append(4)
    is_equal = list_1==list_2
    print(is_equal)
    if is_equal:
        print("mutable")
    else:
        print("immutable")
        
    tuple_1=(1,2,3)
    tuple_2=tuple_1
    tuple_2+=(4,)
    is_equal=tuple_1==tuple_2
    print(is_equal)
    if is_equal:
        print("mutable")
    else:
        print("immutable")
        
    set_1={1,2,3}
    set_2=set_1
    set_2.add(4)
    is_equal = set_1==set_2
    print(is_equal)
    if is_equal:
        print("mutable")
    else:
        print("immutable")
    


# Problem 3

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
    return calculator.sqrt(calculator.sum(calculator.product(a, a), calculator.product(b,b)))
    
    


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    A=list(A)
    power_set_list = []
    for i in range(len(A) + 1):
        for subsets in combinations(A,i):
            power_set_list.append(set(subsets))
    return power_set_list
    


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")

    
    
    
    
    
if __name__=="__main__":
    L=[2,4,6,8,10]
    print(prob1(L))
    
    prob2()
    
    a=6
    b=8
    print(hypot(a,b))
    
    A=['a','b','c']
    print(power_set(A))