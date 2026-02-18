import numpy as np

def f(coords):
    x, y, z = coords
    return (x+1)**2 + (y-1)**2 + (z-2)**2

def f_grad(coords):
    x, y, z = coords
    return np.array([2*(x+1), 2*(y-1), 2*(z-2)])

coords = np.array([10.0, 10.0, 10.0])  # initial point (any N-dim vector)
alpha = 0.1
max_iters = 200
eps = 0.000000001

for i in range(max_iters):
    grad = f_grad(coords)
    coords_new = coords - alpha * grad
    print(f"Step {i+1:3d}: {np.round(coords,4)}, f = {f(coords):.6f}, grad = {np.linalg.norm(grad):.6f}")
    if np.linalg.norm(coords_new - coords) < eps:
        coords = coords_new
        break
    coords = coords_new

print(f"\nMinimum found at {coords}, f = {f(coords):.8f}")