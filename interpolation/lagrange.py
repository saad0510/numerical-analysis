from math import *

# purpose: take x and y values from user
# returns: tuple of two lists corresponding to x and y values
def input_xy():
    x = []      # will hold x values
    y = []      # will hold f(x) or y values

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

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

x, y = input_xy()
n = len(x)

# equation function:
def Px(x_value):
    y_value = 0
    for k in range(0, n):
        temp = y[k]
        for i in range(0, n):
            if i != k:
                temp *= (x_value - x[i]) / (x[k] - x[i])
        y_value += temp
    return y_value

# evaluate at x0:
x0 = float(input("input the target x > "))
print(f"P{n-1}({x0}) = {Px(x0)}")
