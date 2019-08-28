import numpy as np
from numpy.random import randint as dice

rows = int(input("rows? "))
cols = int(input("cols? "))
array = np.array([[i*j for j in range(1,cols+1)] for i in range(1,rows+1)])
print(f'Array:\n{array}')

random_col = dice(0,cols-1)
print(f'Column index {random_col}:\n{array[:,random_col]}')

random_row = dice(0,rows-1)
print(f'Row index {random_row}:\n{array[random_row,:]}')

#rows and columns need to be larger than 3
print(f'Upper left:\n{array[:3,:3]}')
print(f'Upper right:\n{array[:3,-3:]}')

print(f'Transpose:\n{np.transpose(array)}')