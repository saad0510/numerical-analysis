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

# purpose: evenly space the given 2D table across its column
# returns: 2D list of evenly spaced table
def space_table(list):
    table_with_spaces = []
    for i in range(0, len(table)):
        # insert leading spaces of each column:
        table_with_spaces.append(['space' for x in range(0, n - len(table[i]))])

        # insert space after each value:
        for j in range(0, len(table[i])):
            table_with_spaces[i].append(table[i][j])
            table_with_spaces[i].append('space')
            
        # insert trailing spaces of each column:
        for j in range(0, n - len(table[i])):
            table_with_spaces[i].append('space')
    return table_with_spaces

# --------------------------------------------------------------------
# --------------------------------------------------------------------
# --------------------------------------------------------------------

x, y = input_xy()
n = len(x)

dd = []             # 2D list of divide differences
dd.append(y)        # 1st column is y values

# calculate all divided differences:
for i in range(1, n): 
    dd.append([])
    for j in range(0, len(dd[i-1])-1):
        dd[i].append((dd[i-1][j+1] - dd[i-1][j]))

# table = n | x | divided differences 
table = [ [i for i in range(0, n)], x]
table.extend(dd)

# print table headers:
header = f"{'n':>3} | {'x':^7} |"
for i in range(0, len(dd)):
    header += f" {'DD' + str(i) :^17} |"
print(header)
print()

# evenly space the table:
table_with_spaces = space_table(table)

# print final table:
for i in range(0, 2*n):
    row = ""

    # print n column:
    if table_with_spaces[0][i] == 'space':
        row += f"{'' :>3} |"
    else: 
        row += f"{table_with_spaces[0][i] :>3} |"

    # print x column:
    if table_with_spaces[1][i] == 'space':
        row += f" {'' :^7} |"
    else: 
        row += f" {table_with_spaces[1][i] :^7} |"

    # print all divided differences:
    for j in range(2, len(table)):
        if table_with_spaces[j][i] == 'space':
            row += f" {'' :^17} |"
        else:
            row += f" {table_with_spaces[j][i] :^17.10f} |"
    print(row)

# extract all constants:
constants = []
for d in dd:
    constants.append(d[0])

# equation function:
def Px(x_value):
    y = 0
    p = (x_value-x[0]) / (x[1]-x[0])
    for i in range(0, len(constants)):
        a = constants[i]
        for j in range(0, i):
            a *= (p-j)
        a /= factorial(i)
        y += a
    return y

# evaluate at x0:
x0 = float(input("input the target x > "))
print(f"P{n-1}({x0:.3f}) = {Px(x0)}")
