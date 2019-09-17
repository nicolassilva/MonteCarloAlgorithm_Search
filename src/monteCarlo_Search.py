import numpy as np
from random import *
import sys


class File():
	def __init__(self, filename):
		self.filename = filename

	def readFile(self):
		"""Open the file containing the sequence to study"""
		fichier = open(self.filename,"r")
		return fichier.readline().rstrip('\n')

class Array():
	def __init__(self, length):
		self.length = length

	def createArray(self):
		"""Define the matrix as a square of 2 times the length of the sequences
		This function takes in argument an integer"""
		mat = np.char.array([['.']*self.length*2]*self.length*2)
		return mat

	def energy(self,matrix,seq,dic):
		"""Calculate the total energy of a conformation of amino acids"""
		e = 0
		for a in range(0,len(seq)):
			if seq[a] != 'h':
				e = e
			else:
				(i,j) = dic[a]
				for k in range(i-1,i+2):
					for l in range(j-1,j+2):
						if matrix[k][l] == 'h':
							e = e - 1
				e = e + 1
		return e


if __name__ == '__main__':
	
	nstep = 100
	
	#Import the sequence
	sequence = File(sys.argv[1])
	seq = sequence.readFile()
	#print(len(seq))

	matrice = Array(len(seq))
	mat = matrice.createArray()

	j=int(len(seq)/2)
	#Put the sequence in the middle of the matrix
	for k in range(len(seq)):
		mat[len(seq)][j]=seq[k]
		j=j+1
	#print(mat)

	#Create a list of the order of the amino acids and a dictionnary containing all the coordinates
	list_aa = range(len(seq))
	dic = {}
	j=int(len(seq)/2)
	for i in range(len(seq)):
		dic[list_aa[i]] = (len(seq),j)
		j=j+1
	#print(dic)
	#print(mat)

	#Initial Energy calculation
	Einit = matrice.energy(mat,seq,dic)
	
	#Monte Carlo random algorithm
	for k in range(nstep):
		newDic = dic
		a = randint(0,len(list_aa)-1)
		(i,j) = newDic[a]
		#print(i,j)
		d = randint(1,8)
		if d==1: #Left moove
			if (mat[i][j-1] != '.'):
				break
			else:					
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i,j-1)
		elif d==2: #Right moove
			if (mat[i][j+1] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i,j+1)
		elif d==3: #Up moove
			if (mat[i-1][j] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i-1,j)
		elif d==4: #Down moove
			if (mat[i+1][j] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i+1,j)
		elif d==5: #Up/Left moove
			if (mat[i][j-1] != '.'):
				break
			else:					
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i-1,j-1)
		elif d==6: #Up/Right moove
			if (mat[i][j+1] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i-1,j+1)
		elif d==7: #Down/Left moove
			if (mat[i-1][j] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i+1,j-1)
		elif d==8: #Down/Right moove
			if (mat[i+1][j] != '.'):
				break
			else:
				for l in range(a,len(list_aa)):
					(i,j) = newDic[l]
					newDic[l] = (i+1,j+1)
		#print(newDic)

		#Put the new sequence in the middle of the matrix
		newMat = matrice.createArray()
		for k in range(len(seq)):
			(i,j) = newDic[k]
			newMat[i][j]=seq[k]

		#Determination of the relevance of the moove through energy calculation
		Enew = matrice.energy(newMat,seq,newDic)
		if Enew < Einit:
			dic = newDic
			mat = newMat


	print(mat)





