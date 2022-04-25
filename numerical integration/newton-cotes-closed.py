from math import *  
import numpy as np  
import matplotlib.pyplot as plt

# ----------------- functions ------------------- #
def trapezoid(_x, _y):
    h = _x[1] - _x[0]
    return (h/2) * (_y[0] + _y[1])

def simpson(_x, _y):
    h = x[1] - x[0]
    return (h/3) * (_y[0] + 4*_y[1] + _y[2])

def simpson_3x8(_x, _y):
    h = x[1] - x[0]
    return (3*h/8) * (_y[0] + 3*_y[1] + 3*_y[2] + _y[3])

def n_4(_x, _y):
    h = x[1] - x[0]
    return (2*h/45) * (7*_y[0] + 32*_y[1] + 12*_y[2] + 32*_y[3] + 7*_y[4])

def input_xy():
    x = []      
    y = []

    # input x values:
    x_str = input("input x values > ").split();  # strings of x values 
    x = [float(x) for x in x_str]                # convert strings to floats
    
    # input y values: 
    y_str = input("input y values (f to enter a function) > ").split(); 

    if 'f' in y_str:
        # calculate y from a function:
        fx_str = input("enter a function for y=f(x) > ")
        fx = eval("lambda x: " + fx_str)
        y = [fx(x) for x in x]
    else:
        # calculate y from given values:
        y = [float(y) for y in y_str]
        
    if len(y) != len(x):    # unequal x and y values?
        print("ERROR: number of y values must match the number of x values\n")
        return ([], [])
    return (x, y)
# ----------------------------------------------- #

x, y = input_xy()
n = len(x) - 1
result = 0
actual_value = float(input("enter the true value of integral > "))

if n == 1:
    result = trapezoid(x, y)
elif n == 2:
    result = simpson(x, y)
elif n == 3:
    result = simpson_3x8(x, y)
elif n == 4:
    result = n_4(x, y)
else:
    print("open newton-cotes formula only supports upto 5 inputs")

print("result =", round(result, 5))
print("absolute error:", round(abs(actual_value - result), 5))

# Display Graph:
xx = np.arange(-100, 100, 0.01)
yy = [Px(xin) for xin in xx]

plt.plot(xx, yy)
plt.grid()
plt.show()
