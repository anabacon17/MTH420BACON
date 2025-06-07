# oneD_optimization.py
"""Volume 2: One-Dimensional Optimization.
<Ana Bacon>
<MTH 420>
<June 6>
"""

import numpy as np
import scipy.linalg as la
from matplotlib import pyplot as plt

# Problem 1
def newton(f, x0, Df, tol=1e-5, maxiter=15):
    """Use Newton's method to approximate a zero of the function f.

    Parameters:
        f (function): a function from R^n to R^n (assume n=1 until Problem 5).
        x0 (float or ndarray): The initial guess for the zero of f.
        Df (function): The derivative of f, a function from R^n to R^(nxn).
        tol (float): Convergence tolerance. The function should returns when
            the difference between successive approximations is less than tol.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float or ndarray): The approximation for a zero of f.
        (bool): Whether or not Newton's method converged.
        (int): The number of iterations computed.
    """
    x_prev = x0
    for k in range(1, maxiter + 1):
        fx = f(x_prev)
        dfx = Df(x_prev)
        if dfx == 0:
            return x_prev, False, k
        x_next = x_prev - fx / dfx
        if abs(x_next - x_prev) < tol:
            return x_next, True, k
        x_prev = x_next
    return x_prev, False, maxiter


# Problem 2
def plot_basins(f, Df, zeros, domain, res=1000, iters=15):
    """Plot the basins of attraction of f on the complex plane.

    Parameters:
        f (function): A function from C to C.
        Df (function): The derivative of f, a function from C to C.
        zeros (ndarray): A 1-D array of the zeros of f.
        domain ([r_min, r_max, i_min, i_max]): A list of scalars that define
            the window limits and grid domain for the plot.
        res (int): A scalar that determines the resolution of the plot.
            The visualized grid has shape (res, res).
        iters (int): The exact number of times to iterate Newton's method.
    """
    r_min, r_max, i_min, i_max = domain
    x = np.linspace(r_min, r_max, res)
    y = np.linspace(i_min, i_max, res)
    X0, Y0 = np.meshgrid(x, y)
    Z = X0 + 1j * Y0

    for _ in range(iters):
        Z -= f(Z) / Df(Z)

    result = np.zeros(Z.shape, dtype=int)
    for i in range(res):
        for j in range(res):
            distances = [abs(Z[i, j] - z) for z in zeros]
            result[i, j] = np.argmin(distances)

    plt.pcolormesh(X0, Y0, result, shading="auto", cmap="brg")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.title("Basins of Attraction")
    plt.show()


# Problem 3
def secant1d(df, x0, x1, tol=1e-5, maxiter=100):
    """Use the secant method to minimize a function f:R->R.

    Parameters:
        df (function): The first derivative of f.
        x0 (float): An initial guess for the minimizer of f.
        x1 (float): Another guess for the minimizer of f.
        tol (float): The stopping tolerance.
        maxiter (int): The maximum number of iterations to compute.

    Returns:
        (float): The approximate minimizer of f.
        (bool): Whether or not the algorithm converged.
        (int): The number of iterations computed.
    """
    for k in range(maxiter):
        f0 = df(x0)
        f1 = df(x1)
        if f1 - f0 == 0:
            return x1, False, k
        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        if abs(x2 - x1) < tol:
            return x2, True, k + 1
        x0, x1 = x1, x2
    return x1, False, maxiter


# Problem 4
def backtracking(f, Df, x, p, alpha=1, rho=.9, c=1e-4):
    """Implement the backtracking line search to find a step size that
    satisfies the Armijo condition.

    Parameters:
        f (function): A function f:R^n->R.
        Df (function): The first derivative (gradient) of f.
        x (float): The current approximation to the minimizer.
        p (float): The current search direction.
        alpha (float): A large initial step length.
        rho (float): Parameter in (0, 1).
        c (float): Parameter in (0, 1).

    Returns:
        alpha (float): Optimal step size.
    """
    while f(x + alpha * p) > f(x) + c * alpha * np.dot(Df(x), p):
        alpha *= rho
    return alpha


if __name__ == "__main__":
    # Problem 1 test
    f = lambda x: np.exp(x) - 2
    Df = lambda x: np.exp(x)
    root, converged, iters = newton(f, 1.0, Df)
    print(f"Newton method: root = {root}, converged = {converged}, iterations = {iters}")

    # Problem 2 test
    f_c = lambda z: z**3 - 1
    Df_c = lambda z: 3*z**2
    zeros = np.array([1, -0.5 + 0.866j, -0.5 - 0.866j])
    plot_basins(f_c, Df_c, zeros, [-2, 2, -2, 2], res=300, iters=20)

    # Problem 3 test
    df = lambda x: 2*x + np.cos(x) + 10*np.cos(10*x)
    x_min, converged, iters = secant1d(df, 0, -1)
    print(f"Secant method: x_min = {x_min}, converged = {converged}, iterations = {iters}")

    # Problem 4 test
    f_m = lambda x: x[0]**2 + x[1]**2 + x[2]**2
    Df_m = lambda x: np.array([2*x[0], 2*x[1], 2*x[2]])
    xk = np.array([150., .03, 40.])
    pk = np.array([-.5, -100., -4.5])
    alpha = backtracking(f_m, Df_m, xk, pk)
    print(f"Backtracking line search step size: alpha = {alpha}")

