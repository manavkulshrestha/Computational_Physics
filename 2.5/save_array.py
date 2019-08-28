import numpy as np

rows = int(input("rows? "))
cols = int(input("cols? "))
array1 = np.array([[i*j for j in range(1,cols+1)] for i in range(1,rows+1)])

np.savetxt('array1.txt',array1,newline='\n')