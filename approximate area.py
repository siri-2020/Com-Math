import math

def is_inside(x, y, radius):
    return x**2 + y**2 <= radius**2

def approximate_area(radius, step):
    inside_count = 0

    x = -radius
    while x <= radius:
        y = -radius
        while y <= radius:
            center_x = x + step / 2
            center_y = y + step / 2
            if is_inside(center_x, center_y, radius):
                inside_count += 1
            y += step
        x += step
    return inside_count * (step**2)
# ==============================================
# different steps for the unit circle
radius = 1.0
for step in [0.5, 0.25, 0.1, 0.05, 0.001]:
    area = approximate_area(radius, step)
    print(f"step={step} approx={area}")

# different radiuses for step=0.001
for radius in [0.5, 1.0, 1.5, 2.0, 3.0]:
    area = approximate_area(radius, 0.001)
    print(f"radius={radius} approx={area}")