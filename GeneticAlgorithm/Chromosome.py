#Class that will be the object to represent a clause of an expression
class Chromosome:
	#Initialize Chromosome Object
	def __init__(self, newClause):
		#The clause to be used
		self.theClause = newClause
		
	#Get the clause
	def getClause(self):
		return self.theClause
	
	#Evaluates the clause
	def EvaluateClause(self):
		#Turn the passed in string into a list
		theEvaluatedClause = list(self.theClause)
		#Variable to represent the return value
		thereturnvalue = 0
		#Loop through the list
		for index in range(len(theEvaluatedClause)):
			#If the index is equal to !
			if (theEvaluatedClause[index] == "!"):
				#Perform the NOT operation on the next index and return the value
				thereturnvalue = self.__NOT(int(theEvaluatedClause[index+1]))
				#Convert to string so it can be stored properly
				thereturnvalue = str(thereturnvalue)
				#Set the index to its new value
				theEvaluatedClause[index+1] = thereturnvalue;
			#If the index is equal to V
			elif theEvaluatedClause[index] == "V":
				#Perform the OR operation on the previous index and next index then return the value
				thereturnvalue = self.__OR(int(thereturnvalue),int(theEvaluatedClause[index+1]))
			#If the index is equal to * and the next index is not equal to )
			elif theEvaluatedClause[index] == "*" and theEvaluatedClause[index+1] != "(":
				#Perform the AND operation on the previous index and next index then return the value
				thereturnvalue = self.__AND(int(thereturnvalue),int(theEvaluatedClause[index+1]))
		
		#convert back to string for clarity
		self.theClause = ''.join(theEvaluatedClause)
		
		#return the value of the clause
		return thereturnvalue
	
	#Performs the AND operation
	def __AND(self, preNumber, nextNumber):
		#If the numbers match then return one of them
		if (preNumber == nextNumber):
			return preNumber
		#If the numbers dont match then return 0
		else:
			return 0
	
	#Performs the OR operation
	def __OR(self, preNumber, nextNumber):
		#If the numbers dont match then return 1
		if (preNumber != nextNumber):
			return 1
		#If the numbers do match then return one of them..it will either be 1 or 0
		else:
			return preNumber
	
	#Performs the NOT operation
	def __NOT(self, nextNumber):
		#If the number is 1 then return 0
		if (nextNumber == 1):
			return 0
		#If number is not 1 then return 1
		else:
			return 1