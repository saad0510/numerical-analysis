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
print(f"{'n':^2} | {'a':^20} | {'b':^20} | {'c':^20} | {'|f(c) - f(c*)| < e':^20}")
print(line)

n = 1  		# iteration number
c_prev = 0  # previous value of root
fa = fx(a)  # function at a

while n <= max_iterations:
    # calculate c
    c = (a + b)/2
    fc = fx(c)
    err = abs(c - c_prev)  # estimated absolute error

    # print a row in table
    print(f"{n:^2} | {a:^20} | {b:^20} | {c:^20} | {err:^20.10f} ")

    if fc == 0 or err < tolerance:  # solution is found?
        break

    # update next interval:
    if fa * fc > 0:
        a = c
        fa = fc
    else:
        b = c
    c_prev = c
    n = n + 1
else:
    print("Method failed after maximum iterations")
print(line)

# DISPLAY GRAPH:
x = np.arange(-50, 50, 0.01)
y = [fx(y) for y in x]
plt.plot(x, y)
plt.grid()
plt.show()
