import math

# INPUT: read as strings, then convert to numbers
a_str = input("Write the left endpoint of the interval: ")
if "pi" in a_str:
    a = eval(a_str.replace("pi", "math.pi"))
else:
    a = float(a_str)

b_str = input("Write the right endpoint of the interval: ")
if "pi" in b_str:
    b = eval(b_str.replace("pi", "math.pi"))
else:
    b = float(b_str)

f_x = input("Write the function to integrate: ")
method = input("Select integration method (LRM/RRM/MPM/TM): ")

# PROCESS
area = 0.0
n = 1000
h = (b - a) / n
shift = 0
constant = 0.0

if method == "RRM":
    shift = 1
elif method == "MPM":
    constant = h / 2

if method == "TM":
    # Trapezoid method (correct)
    for i in range(0, n + 1):
        xi = a + i * h
        x = xi
        height = eval(f_x)
        if i == 0 or i == n:
            area += height
        else:
            area += 2 * height
    area = area * h / 2
else:
    # Rectangle methods (LRM, RRM, MPM)
    for i in range(0 + shift, n + shift):
        xi = a + i * h + constant
        x = xi
        height = eval(f_x)
        area += height * h

# OUTPUT
print(f"The integration of {f_x} is {area:.3f}")
