#these are codes for trigonometric functions 

import math
x,y,z = 1,2,3
theta = 45
theta = math.radians(theta)
y_new = y*math.cos(theta_rad)-z*math.sin(theta_rad)
z_new = y*math.sin(theta_rad)+z*math.cos(theta_rad)
x_new = x
print(f"Rotated point: ({x_new:.2f},{y_new:.2f},{x_new:.2f}")
