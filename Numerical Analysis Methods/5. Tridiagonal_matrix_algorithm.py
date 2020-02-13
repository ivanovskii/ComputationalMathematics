import numpy as np


def tridiagonal_mat_alg(above_diag, main_diag, under_diag, f):
    """
    The function to solve a system of linear equations Ax=f by a tridiagonal matrix algorithm

    Parameters:
        under_diag (list): Coefficients under the main diagonal of the matrix A
        main_diag (list): Coefficients of the main diagonal of the matrix A
        above_diag (list): Coefficients over the main diagonal of the matrix A
        f (list): Right side of the equation
    
    Returns:
        list: a system of linear equations solution

    """

    alpha, beta = [0], [0]
    n = len(f)
    x = [0]*n

    for i in range(n - 1):
        alpha.append(-above_diag[i] / (under_diag[i]*alpha[i] + main_diag[i]))
        beta.append((f[i] - under_diag[i]*beta[i]) / (under_diag[i]*alpha[i] + main_diag[i]))


    x[n-1] = (f[n-1] - under_diag[n-2]*beta[n-1]) / (main_diag[n-1] + under_diag[n-2]*alpha[n-1])
    
    for i in reversed(range(n - 1)):
        x[i] = alpha[i+1]*x[i+1] + beta[i+1]

    return x


a, b, c, f = [2,1], [6,5,8], [3,3], [10,16,30]
print(tridiagonal_mat_alg(a, b, c, f))