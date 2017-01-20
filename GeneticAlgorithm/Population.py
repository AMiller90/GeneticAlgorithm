import sys
import random
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
		self.__EvaluateOnInit()
		
	#Get the current population
	def getPopulation(self):
		return self.theExpression
	
	#Set the population to its new changed state
	def changePopulation(self):
		#Create list for valuse of expression
		thenewExpression = []
		#The index to swap
		offspringIndex = 0
		
		
		#Put in a mutation rate - We are only changing the value of 0 or 1
		#Do not touch the operators
		randomnum1 = random.randint(0, len(self.theOffspring)-1)
		randomnum2 = random.randint(0, len(self.theOffspring)-1)
		
		mutationRate1 = randomnum1 / 3
		mutationRate2 = randomnum2 / 3
		
		#convert to list to prepare for mutation
		self.theOffspring = list(self.theOffspring)
		
		if mutationRate1 < 2:
			if self.theOffspring[mutationRate1] == '1':
				self.theOffspring[mutationRate1] = '0'
			else:
				self.theOffspring[mutationRate1] = '1'
			
		if mutationRate2 < 2:
			if self.theOffspring[mutationRate2] == '1':
				self.theOffspring[mutationRate2] = '0'
			else:
				self.theOffspring[mutationRate2] = '1'
		
		#Loop through the expression and get the values
		#of the current literals
		for i in range(len(self.theExpression)):
			if self.theExpression[i] == "a":
				avalue = self.dictionary.get(self.theExpression[i])
				thenewExpression.append(str(avalue))
			elif self.theExpression[i] == "b":
				bvalue = self.dictionary.get(self.theExpression[i])
				thenewExpression.append(str(bvalue))
			elif self.theExpression[i] == "c":
				cvalue = self.dictionary.get(self.theExpression[i])
				thenewExpression.append(str(cvalue))
			elif self.theExpression[i] == "d":
				dvalue = self.dictionary.get(self.theExpression[i])
				thenewExpression.append(str(dvalue))
			else:
				thenewExpression.append(self.theExpression[i])
	
		#Loop through the list and change accordingly to offspring
		for i in range(len(thenewExpression)):
			if thenewExpression[i] == "1":
				thenewExpression[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
			elif thenewExpression[i] == "0":
				thenewExpression[i] = self.theOffspring[offspringIndex]
				offspringIndex+=1
		#Loop through the list of changed values and make them literals
		for i in range(len(thenewExpression)):
			if thenewExpression[i] == "1":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					thenewExpression[i] = "a"
				else:
					thenewExpression[i] = "c"
			elif thenewExpression[i] == "0":
				#We will randomize so it wont always be the same literal
				number = random.randint(0,1)
				if number == 1:
					thenewExpression[i] = "b"
				else:
					thenewExpression[i] = "d"

		#Convert list back to string
		thenewExpression = ''.join(thenewExpression)
		print(thenewExpression)

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
		#List of the return values for each clause
		self.clauseReturnValueslist = []
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for s in self.theExpression:
			if(s == "!"):
				expressionCopy += s
			elif(s == "V"):
				expressionCopy += s
			elif(s == "*"):
				expressionCopy += s
			elif(s == "("):
				expressionCopy += s
			elif(s == ")"):
				expressionCopy += s
				self.numberofclauses += 1
				self.totalclauses = self.numberofclauses
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				self.theparentlist.append(chromosome.getEvaluatedClause())
				#The list that will be used for selection
				self.theSelectedMembers.append(chromosome.getEvaluatedClause())
				if thevalue == 1:
					self.fitnessscore += 1
				self.clauseReturnValueslist.append(thevalue)
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""				
			elif(self.dictionary.has_key(s)):
				expressionCopy += str(self.dictionary.get(s))
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
			if(s == "!"):
				expressionCopy += s
			elif(s == "V"):
				expressionCopy += s
			elif(s == "*"):
				expressionCopy += s
			elif(s == "("):
				expressionCopy += s
			elif(s == ")"):
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
		
		
		self.numberofclauses = 0
		
	#Selects the members based on fitness
	def SelectMembers(self):
		length = len(self.theSelectedMembers)

		parent1index = random.randint(0,length-1)
		parent1 = self.theSelectedMembers[parent1index]
		del self.theSelectedMembers[parent1index]
		
		length = len(self.theSelectedMembers)
		
		parent2index = random.randint(0,length-1)
		parent2 = self.theSelectedMembers[parent2index]
		del self.theSelectedMembers[parent2index]
		
		for s in self.theparentlist:
			if s == parent1:
				print("Found parent1")
			if s == parent2:
				print("Found parent2")
				
		self.theOffspring = self.__MakeOffspring(parent1, parent2)
		
	#Make offspring
	def __MakeOffspring(self, parent1, parent2):
		numbersonly1 = []
		numbersonly2 = []
		sibling1 = numbersonly1
		sibling2 = numbersonly2
		temp = ""
		
		#Loop through the selected clause and check if the the index is a number if it is then add to list
		for i in range(len(parent1)):
			if parent1[i] == "1":
				numbersonly1.append(parent1[i])
			if parent1[i] == "0":
				numbersonly1.append(parent1[i])
		
		#Loop through the selected clause and check if the the index is a number if it is then add to list		
		for i in range(len(parent2)):
			if parent2[i] == "1":
				numbersonly2.append(parent2[i])
			if parent2[i] == "0":
				numbersonly2.append(parent2[i])
		
		num = len(numbersonly1)

		#Range from middle of string to end - Switch back ends
		for i in range(num/2,num):
			temp = sibling1[i]
			sibling1[i] = sibling2[i]
			sibling2[i] = temp
		
		#Range from front to back - to switch the literal values to its opposite
		for i in range(0,num/2):
			thereturnvalue = self.__NOT(int(sibling1[i]))
			sibling1[i] = str(thereturnvalue)
			thereturnvalue = self.__NOT(int(sibling2[i]))
			sibling2[i] = str(thereturnvalue)

		theChildren = ''.join(sibling1)
		theChildren += ''.join(sibling2)

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
		