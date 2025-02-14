import math
x,y,z = 1,2,3
t = 60
t = math.radians(t)
y_new = y*math.cos(t)-z*math.sin(t)
z_new = y*math.sin(t)+z*math.cos(t)
x_new = x
print(f"Rotated point: ({x_new:.2f},{y_new:2f},{z_new:.2f})")
