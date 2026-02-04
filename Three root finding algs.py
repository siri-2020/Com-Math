import math

def f(x):
    return x**2 - 4          # root = 2

def df(x):
    return 2*x              # derivative of f

# ---------- Relaxation Method ----------
def relaxation(a, b, x0, alpha, eps, max_iter=50):
    x = x0
    for i in range(1, max_iter+1):
        x_new = x + alpha * f(x)
        print(i, x_new, f(x_new))
        if abs(x_new - x) < eps:
            break
        x = x_new


# ---------- Newton Method ----------
def newton(a, b, x0, eps, max_iter=50):
    x = x0
    for i in range(1, max_iter+1):
        x_new = x - f(x) / df(x)
        print(i, x_new, f(x_new))
        if abs(x_new - x) < eps:
            break
        x = x_new


# ---------- Bisection Method ----------
def bisection(a, b, eps, max_iter=50):
    for i in range(1, max_iter+1):
        c = (a + b) / 2
        print(i, c, f(c))
        if abs(b - a) < eps:
            break
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

a = 0
b = 3

eps = 1e-6
x0 = 2.5     
alpha = -0.25

print("Relaxation Method:")
relaxation(a, b, x0, alpha, eps, 50)
print("\nNewton Method:")
newton(a, b, x0, eps, 50)
print("\nBisection Method:")
bisection(a, b, eps, 50)
