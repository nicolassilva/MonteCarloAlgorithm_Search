import numpy as np
from random import *

#Define the sequence
seq = "hhhpphhh"

#Define the matrix as a square of 2 times the length of the sequences
mat = np.char.array([['.']*len(seq)*2]*len(seq)*2)
#Define energy
e = 0

j=len(seq)/2
#Rentre la sequence au milieu de la matrice
for k in range(len(seq)):
    mat[len(seq)][j]=seq[k]
    j=j+1
print(mat)

for nb in range(1):
    for i in range(len(mat)):
        for j in range(len(mat)):
            if (mat[i][j] != '.') :
                a = randint(1,4)
                if a==1:
                    if mat[i-1][j+1] != '.':
                        break
                    else:
                        mat[i-1][j+1] = mat[i][j]
                        mat[i][j] = '.'
                elif a==2:
                    if mat[i-1][j-1] != '.':
                        break
                    else:
                        mat[i-1][j-1] = mat[i][j]
                        mat[i][j] = '.'
                elif a==3:
                    if mat[i+1][j+1] != '.':
                        break
                    else:
                        mat[i+1][j+1] = mat[i][j]
                        mat[i][j] = '.'
                elif a==4:
                    if mat[i+1][j-1] != '.':
                        break
                    else:
                        mat[i+1][j-1] = mat[i][j]
                        mat[i][j] = '.'
print(mat)
