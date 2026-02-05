import math

def gaussian_elimination_silent(A, b):
    A = [row[:] for row in A]
    b = b[:]
    n = len(A)
    
    # Forward pass of elimination
    for i in range(n-1):
        for j in range(i+1, n):
            k_temp = - A[j][i] / A[i][i]
            for k in range(n):
                A[j][k] += k_temp * A[i][k]
            b[j] += k_temp * b[i]

    x_sol = [0.0 for _ in range(n)]
    for i in range(n):
        row_idx = n - i - 1
        res = b[row_idx]
        for j in range(n - i, n):
            res -= A[row_idx][j] * x_sol[j]
        x_sol[row_idx] = res / A[row_idx][row_idx]
    return x_sol

def hilbert_matrix(n):
    return [[1.0 / (i + j + 1) for j in range(n)] for i in range(n)]

def build_rhs(A):
    n = len(A)
    x_true = [1.0]*n
    b = [sum(A[i][j]*x_true[j] for j in range(n)) for i in range(n)]
    return x_true, b

#=====================TEST========================
sizes = [5, 10, 20, 50, 100]

for n in sizes:
    A = hilbert_matrix(n)
    x_true, b = build_rhs(A)
    x_num = gaussian_elimination_silent(A, b)
    
    errors = [abs(x_num[i] - 1.0) for i in range(n)]
    print(f"n = {n:3d} -> max error = {max(errors):.2e}")