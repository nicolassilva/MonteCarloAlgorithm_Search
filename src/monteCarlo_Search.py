import numpy as np
from random import *
import sys


class File():
	def __init__(self, filename):
		self.filename = filename

	def readFile(self):
		"""Open the file containing the sequence to study"""
		fichier = open(self.filename,"r")
		return fichier.read()

class Array():
	def __init__(self, length):
		self.length = length

	def createArray(self):
		"""Define the matrix as a square of 2 times the length of the sequences"""
		mat = np.char.array([['.']*self.length*2]*self.length*2)
		return mat


if __name__ == '__main__':
	#Import the sequence
	sequence = File(sys.argv[1])
	seq = sequence.readFile()
	#print(len(seq))

	matrice = Array(len(seq))
	mat = matrice.createArray()

	j=int(len(seq)/2)
	#Rentre la sequence au milieu de la matrice
	for k in range(len(seq)):
	    mat[len(seq)][j]=seq[k]
	    j=j+1
	#print(mat)

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
