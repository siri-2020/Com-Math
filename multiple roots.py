import math

def f(x):
    return x**4 + 3*x**3 + x**2 - 2*x - 0.5

def bisection(a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return None

    for _ in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol or (b - a)/2 < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return (a + b) / 2

a, b = -3, 2
N = 10000
h = (b - a) / N

roots = []

x_left = a
for i in range(N):
    x_right = x_left + h
    if f(x_left) * f(x_right) < 0:
        root = bisection(x_left, x_right)
        if root is not None:
            if not any(abs(root - r) < 1e-4 for r in roots):
                roots.append(root)
    x_left = x_right

print("Roots: ", roots)