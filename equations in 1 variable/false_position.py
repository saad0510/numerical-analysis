from math import *
import matplotlib.pyplot as plt
import numpy as np

# INPUT PARAMATERS:
eqn_str = input("equation for y=f(x) > ")
a = float(input("lower limit (a) > "))
b = float(input("upper limit (b) > "))
tolerance = float(input("tolerance value > "))
max_iterations = float(input("maximum number of iterations > "))

fx = eval("lambda x: " + eqn_str)  # function representing our equation
line = f"{'':-^3}|{'':-^22}|{'':-^22}|{'':-^22}|{'':-^21}"

# print table headers:
print(line)
print(f"{'n':^2} | {'a':^20} | {'b':^20} | {'c':^20} | {'|f(c)| < e':^20}")
print(line)

n = 1  		# iteration number
fa = fx(a)  # function at a
fb = fx(b)  # function at b

while n <= max_iterations:
    # -- calculate c --
    c = ((a*fb)-(b*fa))/(fb-fa)
    fc = fx(c)
    err = abs(fc)  # estimated absolute error

    # print a row in table
    print(f"{n:^2} | {a:^20} | {b:^20} | {c:^20} | {err:^20.10f} ")

    if fc == 0 or err < tolerance:  # solution is found?
        break

    # update next interval:
    if fa * fc > 0:
        a = c
        fa=fc
    else:
        b = c
        fb=fc
        
    n = n + 1
else:
    print("Method failed after maximum iterations")
print(line)

# DISPLAY GRAPH:
x = np.arange(-11, 11, 0.001)
y = [fx(xx) for xx in x]
plt.plot(x, y)
plt.grid()
plt.show()
