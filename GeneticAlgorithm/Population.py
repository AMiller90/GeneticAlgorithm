import sys
import random
import math
from Chromosome import *

#Class that will be the object to represent what an expression is.
class Population:
	#Initialize Population Object
	def __init__(self, newExpression):
		#Set the expression
		self.theExpression = newExpression
		#The initial expression
		self.theInitialExpression = self.theExpression
		#Fitness Score reference
		self.fitnessscore = 0
		#Total Clauses reference
		self.totalclauses = 0
		#Number of clauses reference
		self.numberofclauses = 0
		#The dictionary used for mapping values
		self.dictionary = {'a': 1, 'b': 0, 'c': 1, 'd': 0, 'e': 1, 'f': 0,
						   'g': 1, 'h': 0, 'i': 1, 'j': 0, 'k': 1, 'l': 0,
						   'm': 1, 'n': 0, 'o': 1, 'p': 0, 'q': 1, 'r': 0,
						   's': 1, 't': 0, 'u': 1, 'v': 0, 'w': 1, 'x': 0,
						   'y': 1, 'z': 1}
						   
		#The members selected reference
		self.theSelectedMembers = []
		#The offspring reference
		self.theOffspring = ""
		#The list of the parents
		self.theparentlist = []
		#The list of clauses after being evaluated
		self.theEvaluatedClauses = []
		#Holds reference to the initial expression
		self.theExpressionReference = []
		#The function for evaluating an expression on initialization
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
		
		#Loop through and find the parents in the list
		#Store the index for future changes
		for i in range(len(self.theEvaluatedClauses)):
			#If the current index is equal to parent 1
			if (self.theEvaluatedClauses[i] == self.theparentlist[0]):
				#Store its index
				parent1index = i
			#If the current index is equal to parent 2
			elif self.theEvaluatedClauses[i] == self.theparentlist[1]:
				#Store its index
				parent2index = i
		
		#Clear the reference list
		self.theExpressionReference = []
		
		#The chance of mutating the first sibling
		if mutationRate1 > 0:
			#Mutate the given index
			#If the current offspring is a 1
			if self.theOffspring[mutationRate1] == '1':
				#Make it a 0
				self.theOffspring[mutationRate1] = '0'
			#Else
			else:
				#Mutate the given index
				#Make it a 1
				self.theOffspring[mutationRate1] = '1'
		
		#The chance of mutating the second sibling
		if mutationRate2 >= 0:
			#Mutate the given index
			#If the current offspring is a 1
			if self.theOffspring[mutationRate2] == '1':
				#Make it a 0
				self.theOffspring[mutationRate2] = '0'
			#Else
			else:
				#Mutate the given index
				#Make it a 1
				self.theOffspring[mutationRate2] = '1'

		
		#Loop through the list and change parent1 accordingly to offspring
		for i in range(len(par1)):
			#If the index is 1
			if (par1[i] == "1"):
				#Its a number so set it to the offspring number
				par1[i] = self.theOffspring[offspringIndex]
				#Increment the index by 1
				offspringIndex+=1
			#If the index is 0
			elif (par1[i] == "0"):
				#Its a number so set it to the offspring number
				par1[i] = self.theOffspring[offspringIndex]
				#Increment the index by 1
				offspringIndex+=1
				
		#Loop through the list and change parent2 accordingly to offspring
		for i in range(len(par2)):
			#If the index is 1 or 0
			if (par2[i] == "1"):
				#Its a number so set it to the offspring number
				par2[i] = self.theOffspring[offspringIndex]
				#Increment the index by 1
				offspringIndex+=1
			#If the index is 0
			elif (par2[i] == "0"):
				#Its a number so set it to the offspring number
				par2[i]  = self.theOffspring[offspringIndex]
				#Increment the index by 1
				offspringIndex+=1
	
		
		#Convert back to string for storing
		par1 = ''.join(par1)
		par2 = ''.join(par2)
		
		#Now set the evaluated clause with the changes
		self.theEvaluatedClauses[parent1index] = par1
		self.theEvaluatedClauses[parent2index] = par2
		
		#Fix error of "*" character being added to the front of an expression
		if self.theEvaluatedClauses[0][0] == "*":
			#Convert to a list for changing
			thelisttochange = list(self.theEvaluatedClauses[0])
			#Change it to empty
			thelisttochange[0] = ""
			#Set the clause to the list converted to a string
			self.theEvaluatedClauses[0] = ''.join(thelisttochange)

		
		#Convert list back to string
		thenewExpression = ''.join(self.theEvaluatedClauses)

		#Reset the list
		self.theEvaluatedClauses = []
		
		#Reset the parents list
		self.theparentlist = []
		#Set the expression to the new one
		self.theExpression = thenewExpression
		
		#List to check for literals already found
		alreadychecked = []
		
		#Change dictionary values
		for index in range(len(self.theInitialExpression)):
			#If its in the dictionary
			if self.theInitialExpression[index] in self.dictionary:
				#If the literal is already in the list
				if self.theInitialExpression[index] in alreadychecked:
					#Continue
					continue
				#Get the index 
				elif(thenewExpression[index] == "1"):
					#Grab the key
					thekey = str(self.theInitialExpression[index])	
					#Grab the value
					thevalue = int(thenewExpression[index])
					#Set new value
					self.dictionary[thekey] = thevalue
					#Append the literal
					alreadychecked.append(thekey)
				elif(thenewExpression[index] == "0"):
					#Grab the key
					thekey = str(self.theInitialExpression[index])
					#Grab the value
					thevalue = int(thenewExpression[index])
					#Set new value
					self.dictionary[thekey] = thevalue
					#Append the literal
					alreadychecked.append(thekey)
		
		#ReEvaluate the expression to see if it has found the solution
		self.__ReEvaluateExpression(self.theExpression)
			
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
		clauseReturnValueslist = []
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for i in range(len(self.theExpression)):
			#If the i is equal to )
			if(self.theExpression[i] == ")"):
				#Append it to the copy
				expressionCopy += self.theExpression[i]
				#Append it to the reference copy
				referenceCopy += self.theExpression[i]
				#Append it to the list
				self.theExpressionReference.append(referenceCopy)
				#Increase number of clauses
				self.numberofclauses += 1
				#Set total clauses
				self.totalclauses = self.numberofclauses				
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				#Append the evaluated clause to the list
				self.theEvaluatedClauses.append(chromosome.getClause())
				self.theSelectedMembers.append(chromosome.getClause())
				#If value is equal to 1
				if thevalue == 1:
					#Increase fitness score
					self.fitnessscore += 1
				#Append to the list
				clauseReturnValueslist.append(thevalue)
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""
				referenceCopy = ""
			#Elif the dictionary has the key
			elif(self.dictionary.has_key(self.theExpression[i])):
				#Add to the reference copy
				referenceCopy += self.theExpression[i]
				#Add it to the copy
				expressionCopy += str(self.dictionary.get(self.theExpression[i]))
			#Else
			else:
				#Add to the copy
				expressionCopy += self.theExpression[i]
				#Add to the reference copy
				referenceCopy += self.theExpression[i]
		#Reset the number of clauses
		self.numberofclauses = 0
		
		#Now to find the value of an expression you must use the AND operation for each
		#returned value of each clause.
		#However, do to the fact of using a list we only have to check if their is a 0
		#in the list. If there is a 0, then performing the AND operations would result in 0.
		#If only 1s are present in the list then using the AND operation will result in a 1.
		theexpressionvalue = 0
		#If there is a 0 in the list
		if 0 in clauseReturnValueslist:
			#Set to 0
			theexpressionvalue = 0
		#Else
		else:
			#Set to 1
			theexpressionvalue = 1
			
		#Return theexpressionvalue
		return theexpressionvalue
	
	#Evaluate the expression on init so the loop can run
	def __EvaluateOnInit(self):
		#The value of the expression
		thevalue = 0
		#New expression has new clauses, so reset fitness score
		self.fitnessscore = 0
		#Temporary variable for parsing
		expressionCopy = ""
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for s in self.theExpression:
			#If s == )
			if (s == ")"):
				#Add it to the copy
				expressionCopy += s
				#Increase th eclause count by 1
				self.numberofclauses += 1
				#Set total clauses for checking 
				self.totalclauses = self.numberofclauses
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				#If the value is 1
				if (thevalue == 1):
					#Increase the fitness score
					self.fitnessscore += 1
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""
			#Elif the dictionary has this key
			elif(self.dictionary.has_key(s)):
				#Add it to the copy
				expressionCopy += str(self.dictionary.get(s))
			#Else add to the copy
			else:
				expressionCopy += s
		#Reset the number of clauses
		self.numberofclauses = 0
		
	#Selects the members based on fitness
	def SelectMembers(self):
		#Get the length 
		length = len(self.theSelectedMembers)	
		length = length-1
		
		#Get a random number
		parent1index = random.randint(0,length)
		#Set parent1 to the index of the list
		parent1 = self.theSelectedMembers[parent1index]
		#Append it to the list
		self.theparentlist.append(parent1)
		#Delete this of the list..this prevents both parents being
		#equal to one another
		self.theSelectedMembers.remove(parent1)
		
		#Get the length 
		length = len(self.theSelectedMembers)
		length = length-1
		
		#Get a random number
		parent2index = random.randint(0,length)
		#Set parent2 to the index of the list
		parent2 = self.theSelectedMembers[parent2index]
		
		#Append it to the list
		self.theparentlist.append(parent2)
		#Delete this of the list..this prevents both parents being
		#equal to one another
		self.theSelectedMembers.remove(parent2)

		self.theSelectedMembers = []
		#Set the offspring
		self.theOffspring = self.__MakeOffspring(parent1, parent2)
		
	#Make offspring
	def __MakeOffspring(self, parent1, parent2):
		#Create lists for the siblings
		sibling1 = []
		sibling2 = []
		
		#Loop through the selected clause and check if the the index is a number
		for i in range(len(parent1)):
			#If it is a number then add it to the list	
			if parent1[i] == "1" or parent1[i] == "0":
				sibling1.append(parent1[i])
		
		#Loop through the selected clause and check if the the index is a number
		for i in range(len(parent2)):
			#If it is a number then add it to the list		
			if parent2[i] == "1" or parent2[i] == "0":
				sibling2.append(parent2[i])
		
		#Get the length of the list
		num1 = len(sibling1)
		#Get the length of the list
		num2 = len(sibling2)
		
		#If num1 is an odd number
		if num1 % 2 != 0:
			#Divide by 2
			thenewnum = num1 / 2
			#Use the ceiling function
			num1 = math.ceil(thenewnum)
			#Convert to int
			num1 = int(thenewnum)
		
		#If num2 is an odd number
		if num2 % 2 != 0:
			#Divide by 2
			thenewnum = num2 / 2
			#Use the ceiling function
			num2 = math.ceil(thenewnum)
			#Convert to int
			num2 = int(thenewnum)

		#Prevent breaking
		if num2 > num1:
			#Range from middle of string to end - Switch back ends
			for i in range(num1/2,num1):
				#Swap values accordingly
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
	
	#ReEvaluate the Expression 
	def __ReEvaluateExpression(self, theExpression):
		#The value of the expression
		thevalue = 0
		#New expression has new clauses, so reset fitness score
		self.fitnessscore = 0
		#Temporary variable for parsing
		expressionCopy = ""
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for i in range(len(self.theExpression)):
			#If the index is )
			if(self.theExpression[i] == ")"):
				#Add it to the copy
				expressionCopy += self.theExpression[i]
				#Increment the number of clauses
				self.numberofclauses += 1
				#Set total clauses
				self.totalclauses = self.numberofclauses	
				#Create Chromosome Object 
				chromosome = Chromosome(expressionCopy)
				#Evaluate the clause that is made of numbers and return its value
				thevalue = chromosome.EvaluateClause()
				thevalue = int(thevalue)
				#If the value is 1
				if (thevalue) == 1:
					#Increment the fitness score
					self.fitnessscore += 1
				#Reset to empty, so as it continues to loop it will evaluate next clause
				expressionCopy = ""
			#Elif the index is found in the dictionary
			elif(self.dictionary.has_key(self.theExpression[i])):
				#Add it to the copy
				expressionCopy += str(self.dictionary.get(self.theExpression[i]))
			#Else
			else:
				#Add it to the copy
				expressionCopy += self.theExpression[i]

		#Reset the number of clauses
		self.numberofclauses = 0
		#Return the value
		return self.fitnessscore
		
	#Get the literals in the expression
	def getSolutionGene(self):
		#Print the expression
		print("The Expression")
		print(self.theInitialExpression)
		print("\n")
		#Store the found literals
		theLiteralsfound = []
		#Store the number of the literal representation
		thegenesolution = []
		
		#Loop through the initial expression
		for s in self.theInitialExpression:
			#If its already in the list
			if (s in theLiteralsfound):
				#Continue
				continue;
			#If the index is inside the dictiontary then..
			elif s in self.dictionary:
				#Add the character to the literals list
				theLiteralsfound.append(s);
				
		#Sort literals
		theLiteralsfound.sort()
		#Make into a string
		theLiteralsfound = ''.join(theLiteralsfound)
		
		#Print the literals found
		print(theLiteralsfound)
		
		#Loop through and append
		for s in theLiteralsfound:
			thegenesolution.append(str(self.dictionary.get(s)))
		
		#Make into a string
		thegenesolution = ''.join(thegenesolution)
		#Return the string 
		return thegenesolution
	
		#Performs the NOT operation
	def __NOT(self, nextNumber):
		#If the number is 1 then return 0
		if (nextNumber == 1):
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
