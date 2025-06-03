# drazin.py
"""Volume 1: The Drazin Inverse.
Ana Bacon
MTH 420
Jun 3
"""

import numpy as np
from scipy import linalg as la
from scipy.linalg import schur, inv


# Helper function for problems 1 and 2.
def index(A, tol=1e-5):
    """Compute the index of the matrix A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
        k (int): The index of A.
    """

    # test for non-singularity
    if not np.isclose(la.det(A), 0):
        return 0

    n = len(A)
    k = 1
    Ak = A.copy()
    while k <= n:
        r1 = np.linalg.matrix_rank(Ak)
        r2 = np.linalg.matrix_rank(np.dot(A,Ak))
        if r1 == r2:
            return k
        Ak = np.dot(A,Ak)
        k += 1

    return k


# Problem 1
def is_drazin(A, Ad, k):
    """Verify that a matrix Ad is the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.
        Ad ((n,n) ndarray): A candidate for the Drazin inverse of A.
        k (int): The index of A.

    Returns:
        (bool) True of Ad is the Drazin inverse of A, False otherwise.
    """
    cond1 = np.allclose(np.linalg.matrix_power(A, k+1) @ Ad, np.linalg.matrix_power(A,k))
    cond2 = np.allclose(Ad @ A @ Ad, Ad)
    cond3 = np.allclose(A @ Ad, Ad @ A)
    return cond1 and cond2 and cond3
    


# Problem 2
def drazin_inverse(A, tol=1e-4):
    """Compute the Drazin inverse of A.

    Parameters:
        A ((n,n) ndarray): An nxn matrix.

    Returns:
       ((n,n) ndarray) The Drazin inverse of A.
    """
    n = A.shape[0]
    T, Q = schur(A)
    U = np.zeros((n, n))
    U[:, :] = Q[:, :]
    
    eigenvals = np.diag(T)
    k = 0
    for i in range(n):
        if abs (eigenvals[i]) > tol:
            k +=1
            
    T, Q, _ = schur(A, sort=lambda x: abs(x) > tol)
    U = Q
    
    S = np.zeros_like(T)
    for i in range(k):
        S[i, i] = 1 / T[i, i] 
        
    AD = U @ S @ inv(U)
    return AD

    A = np.array([
    [1, 3, 0, 0],
    [0, 1, 3, 0],
    [0, 0, 1, 3],
    [0, 0, 0, 0]], dtype=float)

    AD = drazin_inverse(A)
    print(is_drazin(A, AD, 1)) 



# Problem 3
def laplacian(A):
    D = np.diag(A.sum(axis=1))
    return D-A

def effective_resistance(A):
    """Compute the effective resistance for each node in a graph.

    Parameters:
        A ((n,n) ndarray): The adjacency matrix of an undirected graph.

    Returns:
        ((n,n) ndarray) The matrix where the ijth entry is the effective
        resistance from node i to node j.
    """
    n = A.shape[0]
    L = laplacian(A)
    LD = drazin_inverse(L)
    
    R = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            R[i,j] = LD[i , i] + LD[j, j] - 2 * LD[i, j]
    return R

    A = np.array([
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]], dtype=float)

    R = effective_resistance(A)
    print(np.round(R, 4))

                                  
                                  
if __name__ == "__main__":
    # Problem 1: Test is_drazin
    A1 = np.array([
        [1, 3, 0, 0],
        [0, 1, 3, 0],
        [0, 0, 1, 3],
        [0, 0, 0, 0]
    ], dtype=float)

    AD1 = np.array([
        [1, -3, 9, 81],
        [0, 1, -3, -18],
        [0, 0, 1, 3],
        [0, 0, 0, 0]
    ], dtype=float)

    print("Problem 1:")
    print("A1 Drazin Check:", is_drazin(A1, AD1, 1))

    # Problem 2: Compute Drazin inverse and verify with Problem 1
    A2 = A1.copy()
    AD2 = drazin_inverse(A2)
    print("Problem 2:")
    print("A2 Drazin Check (should be True):", is_drazin(A2, AD2, 1))

    # Problem 3: Compute effective resistance for triangle graph
    A3 = np.array([
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ], dtype=float)

    print("Problem 3:")
    R = effective_resistance(A3)
    print("Effective Resistance Matrix:\n", np.round(R, 4))
                                  