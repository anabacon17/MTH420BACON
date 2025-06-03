# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Ana Bacon>
<MTH 420>
<Jun 3>
"""

import numpy as np
import cvxpy as cp



def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3, nonneg=True)  # x[0] = x, x[1] = y, x[2] = z

    # Objective: 2x + y + 3z
    objective = cp.Minimize(2*x[0] + x[1] + 3*x[2])

    # Constraints
    constraints = [
        x[0] + 2*x[1] <= 3,
        x[1] - 4*x[2] <= 1,
        2*x[0] + 10*x[1] + 3*x[2] >= 12
    ]

    # Problem definition and solve
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return x.value, prob.value



# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    A = np.array(A)
    b = np.array(b)

    n = A.shape[1]
    x = cp.Variable(n)

    objective = cp.Minimize(cp.norm1(x))
    constraints = [A @ x == b]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    return x.value, prob.value




# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Variables: p1 through p6
    x = cp.Variable(6, nonneg=True)

    # Cost vector corresponding to each route
    cost = np.array([4, 7, 6, 8, 8, 9])

    # Objective: Minimize total cost
    objective = cp.Minimize(cost @ x)

    # Constraints
    constraints = [
        # Supply constraints
        x[0] + x[1] <= 7,   # from supply center 1
        x[2] + x[3] <= 2,   # from supply center 2
        x[4] + x[5] <= 4,   # from supply center 3

        # Demand constraints
        x[0] + x[2] + x[4] >= 5,  # to demand center 4
        x[1] + x[3] + x[5] >= 8   # to demand center 5
    ]

    # Define and solve the problem
    prob = cp.Problem(objective, constraints)
    prob.solve()

    return x.value, prob.value




# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    x = cp.Variable(3)

    # Q matrix from the quadratic form
    Q = np.array([
        [3, 2, 1],
        [2, 4, 2],
        [1, 2, 3]
    ])

    # c vector from the linear terms
    c = np.array([3, 0, 1])

    # Define the quadratic objective
    objective = cp.Minimize((1/2) * cp.quad_form(x, Q) + c @ x)

    # No constraints
    prob = cp.Problem(objective)
    prob.solve()

    return x.value, prob.value




# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    A = np.array(A)
    b = np.array(b)

    n = A.shape[1]
    x = cp.Variable(n, nonneg=True)

    # Objective: minimize ||Ax - b||_2
    objective = cp.Minimize(cp.norm2(A @ x - b))

    # Constraints: ||x||_1 = 1 and x >= 0
    constraints = [
        cp.sum(x) == 1
    ]

    prob = cp.Problem(objective, constraints)
    prob.solve()

    return x.value, prob.value



if __name__ == "__main__":
    print("===== Lab 16: CVXPY Intro Summary =====\n")

    # Problem 1
    print("Problem 1:")
    x1, val1 = prob1()
    print("  Optimal x:", np.round(x1, 4))
    print("  Optimal value:", round(val1, 4), "\n")

    # Problem 2
    print("Problem 2:")
    A2 = np.array([[1, 2, 1, 1],
                   [0, 3, -2, -1]], dtype=float)
    b2 = np.array([7, 4], dtype=float)
    x2, val2 = l1Min(A2, b2)
    print("  Optimal x:", np.round(x2, 4))
    print("  Optimal value:", round(val2, 4), "\n")

    # Problem 3
    print("Problem 3:")
    x3, val3 = prob3()
    print("  Optimal piano transport plan:", np.round(x3))
    print("  Minimum total cost:", round(val3), "\n")

    # Problem 4
    print("Problem 4:")
    x4, val4 = prob4()
    print("  Minimizer:", np.round(x4, 4))
    print("  Minimum value:", round(val4, 4), "\n")

    # Problem 5
    print("Problem 5:")
    x5, val5 = prob5(A2, b2)
    print("  Optimal x:", np.round(x5, 4))
    print("  Optimal value:", round(val5, 4), "\n")

    print("===== End of Lab 16 Output =====")

    
