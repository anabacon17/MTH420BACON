# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Ana Bacon>
<MTH 420>
<04/18/2025>
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    
    A = np.array([[3, -1, 4],
                  [1, 5, -9]])
    B = np.array([[2, 6, -5,3],
                  [5, -8, 9, 7],
                  [9, -3, -2, -3]])
    C = (A@B)
    
    print(C)
    
def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([[3, 1, 4],
                 [1, 5, 9],
                 [-5, 3, 1]])
    A2 = A @ A
    A3 = A @ A2
    return -(A3) + (9*A2) - (15*A)
result = prob2()
print(result)
    


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.zeros((7, 7), dtype=np.int64) 
    A[np.triu_indices(7)]=1
    
    B = np.ones((7, 7), dtype=np.int64)
    B[np.triu_indices(7)]=5
    B[np.tril_indices(7, -1)]=-1
    
    print(A)
    print(B)
    
    C = A @ B
    
    
    return C @ A
result = prob3()
print(result)



def prob4():
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A = np.array([[-17, 16, -15, 14, -13, 12],
                [-11, 10, -9, 8, -7, 6],
                 [-5, 4, -3, 2, -1, 0]])
                    
    mask = A < 0 
    mask
    A[mask] = 0
    
    
    print(A)
    



def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    
    A = np.array([[0, 2, 4],
                  [1, 3, 5]])
    B = np.ones((3, 3), dtype=np.int64)
    B[np.triu_indices(3)]= 0
    B[np.tril_indices(3, 0)]= 3
    
    C = np.diag([-2, -2, -2])
    
    I = np.eye(3)
    
    
    print(A)
    print(B)
    print(C)
    
    A0 = np.zeros((2, 3))  
    B0 = np.zeros((3, 2))  
    C0 = np.zeros((3, 3)) 
    A1 = A.T

    row1 = np.hstack((A0, A1, I)) 
    
    row2 = np.hstack((A, A0, B0))

    row3 = np.hstack((B, C0, C))
    
    block_matrix = np.vstack((row1, row2, row3))
    
    print(block_matrix)
    
    


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
def row_stochastic(matrix):
    
    row_sums = matrix.sum(axis=1, keepdims=True)  

    stochastic_matrix = matrix / row_sums
    
    return stochastic_matrix 

    A = np.array([[1, 1, 0],
                  [0, 1, 0],
                  [1, 1, 1]])
    print(A)

    result = row_stochastic(A)
    print(result)    
    

#dont do this one
def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")
    
if __name__ == "__main__":
    prob1()
    
    prob2()
    
    prob3()
    
    prob4()
                 
    prob5()
                 
    prob6()
    
