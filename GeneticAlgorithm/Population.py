import sys
import random
import math
from Chromosome import *

#Class that will be the object to represent what an expression is.
class Population:
	#Initialize Population Object
	def __init__(self, newExpression):
		self.theExpression = newExpression
		self.clauseReturnValueslist = []
		self.fitnessscore = 0
		self.totalclauses = 0
		self.numberofclauses = 0
		self.dictionary = {'a': 1, 'b': 0, 'c': 1, 'd': 0}
		self.theSelectedMembers = []
		self.theOffspring = ""
		self.theparentlist = []
		self.theEvaluatedClauses = []
		self.theExpressionReference = []
		self.__EvaluateOnInit()
		
	#Get the current population
	def getPopulation(self):
		return self.theExpression
	
	#Set the population to its new changed state
	def changePopulation(self):
		#The index to swap
		offspringIndex = 0
		#Store the location of parent 1
		parent1index = 0
		#Store the location of parent 2
		parent2index = 0
		
		#Put in a mutation rate - We are only changing the value of 0 or 1
		#Do not touch the operators
		randomnum1 = random.randint(0, len(self.theOffspring)-1)
		randomnum2 = random.randint(0, len(self.theOffspring)-1)
		
		#Mutation chance
		mutationRate1 = randomnum1 / 3
		mutationRate2 = randomnum2 / 3
		
		#convert to list to prepare for mutation
		self.theOffspring = list(self.theOffspring)
		
		#Store each of the parents as a list so 
		#the values can be changed with the correct
		#sibling values
		par1 = list(self.theparentlist[0])
		par2 = list(self.theparentlist[1])

		print("\n")
		print("parent1")
		print(par1)
		print("parent2")
		print(par2)
		
		#Loop through and find the parents in the list
		#Store the index for future changes
		for i in range(len(self.theEvaluatedClauses)):
			print("The clause list")
			print(self.theEvaluatedClauses[i])
			if self.theEvaluatedClauses[i] == self.theparentlist[0]:
				print("Found parent1")
				print(self.theparentlist[0])
				parent1index = i
			elif self.theEvaluatedClauses[i] == self.theparentlist[1]:
				print("Found parent2")
				print(self.theparentlist[1])
				parent2index = i
			else:
				self.theEvaluatedClauses[i] = self.theExpressionReference[i]
				
		self.theExpressionReference = []
		
		
		c1 = Chromosome(self.theparentlist[0])
		print(c1.EvaluateClause())
		c2 = Chromosome(self.theparentlist[1])
		print(c2.EvaluateClause())
		
		#The chance of mutating the first sibling at
		#the given index
		if mutationRate1 > 0:
			if self.theOffspring[mutationRate1] == '1':
				self.theOffspring[mutationRate1] = '0'
			else:
				self.theOffspring[mutationRate1] = '1'
		
		#The chance of mutating the second sibling at
		#the given index
		if mutationRate2 > 0:
			if self.theOffspring[mutationRate2] == '1':
				self.theOffspring[mutationRate2] = '0'
			else:
				self.theOffspring[mutationRate2] = '1'

		
		#Loop through the list and change parent1 accordingly to offspring
		for i in range(len(par1)):
			if par1[i] == "1":
				par1[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
			elif par1[i] == "0":
				par1[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
		
		#Loop through the list and change parent2 accordingly to offspring
		for i in range(len(par2)):
			if par2[i] == "1":
				par2[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
			elif par2[i] == "0":
				par2[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
		
		#print("Pre index")
		#print(self.theEvaluatedClauses)
		
		#Loop through the list of changed values and make them literals
		for i in range(len(par1)):
			if par1[i] == "1":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					par1[i] = "a"
				else:
					par1[i] = "c"
			elif par1[i] == "0":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					par1[i] = "b"
				else:
					par1[i] = "d"
		
		#Loop through the list of changed values and make them literals
		for i in range(len(par2)):
			if par2[i] == "1":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					par2[i] = "a"
				else:
					par2[i] = "c"
			elif par2[i] == "0":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					par2[i] = "b"
				else:
					par2[i] = "d"
		
		
		#Convert back to string for storing
		par1 = ''.join(par1)
		par2 = ''.join(par2)
		
		
		#Now set the evaluated clause set with the changes
		print("Parent1 index of clause list")
		print(parent1index)
		self.theEvaluatedClauses[parent1index] = par1
		print("Parent2 index of clause list")
		print(parent2index)
		self.theEvaluatedClauses[parent2index] = par2
		
		print("Post index")
		print(self.theEvaluatedClauses)
		print("\n")
		
		#Convert list back to string
		thenewExpression = ''.join(self.theEvaluatedClauses)
		
		#Reset the list
		self.theEvaluatedClauses = []
		
		#Reset the parents list
		self.theparentlist = []
		#Set the expression to new one
		self.theExpression = thenewExpression
		
	#Evaluates the expression
	def EvaluateExpression(self):
		#The value of the expression
		thevalue = 0
		#New expression has new clauses, so reset fitness score
		self.fitnessscore = 0
		#Temporary variable for parsing
		expressionCopy = ""
		#Temporary variable for parsing
		referenceCopy = ""
		#List of the return values for each clause
		self.clauseReturnValueslist = []
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for i in range(len(self.theExpression)):
			if(self.theExpression[i] == ")"):
				expressionCopy += self.theExpression[i]
				referenceCopy += self.theExpression[i]
				self.theExpressionReference.append(referenceCopy)
				self.numberofclauses += 1
				self.totalclauses = self.numberofclauses				
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				print("To be selected")
				print(chromosome.getEvaluatedClause())
				self.theEvaluatedClauses.append(chromosome.getEvaluatedClause())
				#The list that will be used for selection
				self.theSelectedMembers.append(chromosome.getEvaluatedClause())
				if thevalue == 1:
					self.fitnessscore += 1
				self.clauseReturnValueslist.append(thevalue)
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""
				referenceCopy = ""
			elif(self.dictionary.has_key(self.theExpression[i])):
				referenceCopy += self.theExpression[i]
				expressionCopy += str(self.dictionary.get(self.theExpression[i]))
			else:
				expressionCopy += self.theExpression[i]
				referenceCopy += self.theExpression[i]
				
		self.numberofclauses = 0
		#Now to find the value of an expression you must use the AND operation for each
		#returned value of each clause.
		#However, do to the fact of using a list we only have to check if their is a 0
		#in the list. If there is a 0, then performing the AND operations would result in 0.
		#If only 1s are present in the list then using the AND operation will result in a 1.
		theexpressionvalue = 0
		if 0 in self.clauseReturnValueslist:
			theexpressionvalue = 0
		else:
			theexpressionvalue = 1
		
		return theexpressionvalue
	
	#Evaluate the expression on init
	def __EvaluateOnInit(self):
		#The value of the expression
		thevalue = 0
		#New expression has new clauses, so reset fitness score
		self.fitnessscore = 0
		#Temporary variable for parsing
		expressionCopy = ""
		#List of the return values for each clause
		self.clauseReturnValueslist = []
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for s in self.theExpression:
			if(s == ")"):
				expressionCopy += s
				self.numberofclauses += 1
				self.totalclauses = self.numberofclauses
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				if thevalue == 1:
					self.fitnessscore += 1
				self.clauseReturnValueslist.append(thevalue)
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""				
			elif(self.dictionary.has_key(s)):
				expressionCopy += str(self.dictionary.get(s))
			else:
				expressionCopy += s

		self.numberofclauses = 0
		
	#Selects the members based on fitness
	def SelectMembers(self):
		#Get the length 
		length = len(self.theSelectedMembers)
		#Get a random number
		parent1index = random.randint(0,length-1)
		#Set parent1 to the index of the list
		parent1 = self.theSelectedMembers[parent1index]
		c = Chromosome(parent1)
		print("This is to be reset Parent1")
		print(parent1)
		#Append it to the list
		self.theparentlist.append(parent1)
		#Delete this of the list..this prevents both parents being
		#equal to one another
		del self.theSelectedMembers[parent1index]
		
		#Get the length 
		length = len(self.theSelectedMembers)
		#Get a random number
		parent2index = random.randint(0,length-1)
		#Set parent2 to the index of the list
		parent2 = self.theSelectedMembers[parent2index]
		print("This is to be reset Parent2")
		print(parent2)
		#Append it to the list
		self.theparentlist.append(parent2)
		#Delete this of the list..this prevents both parents being
		#equal to one another
		del self.theSelectedMembers[parent2index]

		#Set the offspring
		self.theOffspring = self.__MakeOffspring(parent1, parent2)
		
	#Make offspring
	def __MakeOffspring(self, parent1, parent2):
		#Create lists for the siblings
		sibling1 = []
		sibling2 = []
		
		#Loop through the selected clause and check if the the index is a number if it is then add to list
		for i in range(len(parent1)):
			if parent1[i] == "1":
				sibling1.append(parent1[i])
			if parent1[i] == "0":
				sibling1.append(parent1[i])
		
		#Loop through the selected clause and check if the the index is a number if it is then add to list		
		for i in range(len(parent2)):
			if parent2[i] == "1":
				sibling2.append(parent2[i])
			if parent2[i] == "0":
				sibling2.append(parent2[i])
		
		#Get the length of the list
		num1 = len(sibling1)
		#Get the length of the list
		num2 = len(sibling2)
		
		#Use the ceiling function if num1 is an odd number
		if num1 % 2 != 0:
			thenewnum = num1 / 2 
			num1 = math.ceil(thenewnum)
			num1 = int(thenewnum)
		
		#Use the ceiling function if num2 is an odd number
		if num2 % 2 != 0:
			thenewnum = num2 / 2 
			num2 = math.ceil(thenewnum)
			num2 = int(thenewnum)

		#Range from middle of string to end - Switch back ends
		for i in range(num1/2,num1):
			temp = sibling1[i]
			sibling1[i] = sibling2[i]
			sibling2[i] = temp
		
		#Range from front to back - to switch the literal values to its opposite
		for i in range(0,num1/2):
			thereturnvalue = self.__NOT(int(sibling1[i]))
			sibling1[i] = str(thereturnvalue)
			thereturnvalue = self.__NOT(int(sibling2[i]))
			sibling2[i] = str(thereturnvalue)

		#Make the siblings a string
		theChildren = ''.join(sibling1)
		theChildren += ''.join(sibling2)

		#return the children
		return theChildren
	
	#Performs the NOT operation
	def __NOT(self, nextNumber):
	
		#If the number is 1 then return 0
		if nextNumber == 1:
			return 0
		#If number is not 1 then return 1
		else:
			return 1
			
	#Get the fitness score
	def getFitnessScore(self):
		return self.fitnessscore
	
	#Get the number of clauses
	def getNumberOfClauses(self):
		return self.totalclauses
	
	#Get the return values of all clauses
	def getClauseEvalList(self):
		return self.clauseReturnValueslist
		