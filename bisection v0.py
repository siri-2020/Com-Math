import math

def f(x):
    return 5 * math.sin(x**2) - x**5 + x - 1

a = -2
b = 3

for i in range(100):
    c = (a + b) / 2

    print(i+1, c, f(c))

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c