###### Nicolas Silva
###### Université Paris Diderot - Paris 7
###### Septembre 2019 - Projet court

#Import libraries
import numpy as np
from random import *
import sys

#Class creation to read the file containing the sequence
class File():
	def __init__(self, filename):
		"""Input : __init__(filename)"""
		self.filename = filename

	def readFile(self):
		"""Open the file containing the sequence to study"""
		fichier = open(self.filename,"r")
		return fichier.readline().rstrip('\n')

#Class création to create an array and calculate the energy of the conformation
class Array():
	def __init__(self, length):
		"""Input : __init__(length)"""
		self.length = length

	def createArray(self):
		"""Define the matrix as a square of 2 times the length of the sequences
		This function takes in argument an integer"""
		mat = np.char.array([['.']*self.length*2]*self.length*2)
		return mat

	def energy(self,matrix,seq,dic):
		"""Calculate the total energy of a conformation of amino acids
		Input : energy(matrix, sequence, dictionnary)"""
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
				e = e + 1 #As the code is counting the 'h' of all the nine positions, it is necessary to add one to the energy to count only the neighbors and not the 'h' itself
		return e

	def writeFile(self,matrix,filename):
		"""Write data in file
		Input : writeFile(matrix, filename)
		Ouput : file"""
		np.savetxt(filename, matrix, fmt='%-10.1c', delimiter='')
		return


if __name__ == '__main__':
	#Verify if nstep is a positive integer
	if (int(sys.argv[2]) < 1):
		print('Le second argument doit être un entier positif')
		sys.exit()
	nstep = int(sys.argv[2]) #Nstep as the second argument
	
	#Import the sequence
	sequence = File(sys.argv[1])
	seq = sequence.readFile()
	#print(len(seq))

	#Create a matrix of 2 times the length of the sequence
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

	#Initial Energy calculation
	Einit = matrice.energy(mat,seq,dic)
	print("L'énergie initiale de la conformation protéique est de " + str(Einit))
	
	#Monte Carlo random algorithm
	for k in range(nstep):
		newDic = dic
		a = randint(0,len(list_aa)-1) #Choose a random amino acid to move
		(i,j) = newDic[a] #Affect to i and j the coordinates of the amino acid
		d = randint(1,8) #Choose randomly a move to do
		if d==1: #Left moove
			if (mat[i][j-1] != '.'): #Verify if the move is possible
				break
			else:					
				for l in range(a,len(list_aa)): #Move the amino acid and all the amino acids after it
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
		if Enew <= Einit:
			dic = newDic
			mat = newMat
			Einit = Enew

	#print(len(mat))
	matrice.writeFile(mat,'../results/results.txt')
	print(mat)
	print("L'énergie finale de la conformation protéique est de " + str(Einit))





