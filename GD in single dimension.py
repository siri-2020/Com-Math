def f(x):
    return (4 * (x**2)) - 4*x + 4

def f_prime(x):
    return (8 * x) - 4

prev_x = 10.0
alpha = 0.1
max_iters = 50
eps = 0.00001

x = prev_x
for i in range(max_iters):
    grad = f_prime(x)
    x_new = x - alpha * grad
    print(f"Step {i+1:2d}: x = {x:.6f}, f(x) = {f(x):.6f}, grad = {grad:.6f}")
    if abs(x_new - x) < eps:
        x = x_new
        break
    x = x_new

print(f"\nMinimum found at x = {x:.6f}, f(x) = {f(x):.6f}")