import numpy as np

# Tehtävä 1
a = 2.493  # rad
print(np.degrees(a))

b = 0.911  # rad
print(np.degrees(b))

degrees = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for deg in degrees:
    print(np.radians(deg))

# Tehtävä 2
x = 1.6
y = 2.3
z = np.hypot(x, y)
print(z, 'Hypotenuusa')