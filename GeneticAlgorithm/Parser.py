import sys

#Class that will parse the data
#This class is responsible for reading in from a file and getting all of
#the expressions in the file
class Parser:	
	#Initialize Parser object
	def __init__(self, filePath):
		self.dictionary = {'a': 1, 'b': 0, 'c': 1, 'd': 0}
		self.numberofclauses = 0
		self.expressionlist = []
		self.file = ""
		self.__readfromfile(filePath)
		self.fitnessscore = 0
		self.totalclauses = 0
		
	#Read from a file
	def __readfromfile(self, thefileName):
		#Open the file for reading and writing
		self.file = open(thefileName, "r+")
		#Store the file contents into the variable
		fileContents = self.file.read()
		#Parse the file
		self.__parse(fileContents)
		#Close the file
		self.file.close()
	
	#Parse the data inside the file and find all the expressions
	def __parse(self, fileContents):
		theexpression = ""
		num = len(fileContents)
		lineCount = 0
		theliterals = []
		numberofliterals = 0
		
		sys.stdout.write("Operators: \n! is NOT\n* is AND\nV is OR\n\n")
		for index in range(num):
			#If the current index of the file contents is not a new line
			if fileContents[index] != "\n":
				#Add it to the expression variable
				theexpression += fileContents[index]
			
			#If the current index of the file contents is a new line
			if fileContents[index] == "\n":
				#Sort the literals
				theliterals.sort()
				#Increase the line count
				lineCount += 1
				self.expressionlist.append(theexpression)
				#Print the line count and expression
				self.__printfunction(lineCount, theexpression, theliterals, numberofliterals)
				#Set the expression variable to empty
				theexpression = ""
				#Delete the literals
				del theliterals[:]
				#Variable for the number of clauses
				self.numberofclauses = 0
				#Variable for the number of literals
				numberofliterals = 0
			#If index is equal to )
			elif fileContents[index] == ")":
				#Increase clauses count
				self.numberofclauses += 1
			#If index is equal to !
			elif fileContents[index] == "!":
				#Just continue
				continue;
			#If index is equal to V
			elif fileContents[index] == "V":
				#Just continue
				continue;
			#If index is equal to *
			elif fileContents[index] == "*":
				#Just continue
				continue;
			#If index is equal to (
			elif fileContents[index] == "(":
				#Just continue
				continue;
			#Else
			else:
				#Check if the index is inside the literals list, if it is
				if fileContents[index] in theliterals:
					#Just continue
					continue;
				#If the index is not inside the list then..
				#Increment the number of literals
				numberofliterals += 1
				#Add the character to the literals list
				theliterals.append(fileContents[index]);

	#Function used to print data
	def __printfunction(self, lines, expression, theliterals, numofliterals):
		sys.stdout.write("Line: " + str(lines) + "\n")
		sys.stdout.write("The Expression: " + expression + "\n")
		sys.stdout.write("The Literals: " + " ".join(theliterals) + "\n")
		sys.stdout.write("The Number Of Clauses: " + str(self.numberofclauses) + "\n")
		sys.stdout.write("The Number Of Literals: " + str(numofliterals) + "\n" + "\n") 
	
	#Evaluates the expression
	def EvaluateExpression(self, theExpression):
		#The value of the expression
		thevalue = 0
		#New expression has new clauses, so reset fitness score
		self.fitnessscore = 0
		#Temporary variable for parsing
		expressionCopy = ""
		#List of the return values for each clause
		clauseReturnValueslist = []
		#Loop through expression and make a copy with the literals 
		#replaced with numbers accordingly
		for s in theExpression:
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
				#Evaluate the clause that is made of numbers and return its value
				thevalue = self.EvaluateClause(expressionCopy)
				if thevalue == 1:
					self.fitnessscore += 1
				clauseReturnValueslist.append(thevalue)
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
		if 0 in clauseReturnValueslist:
			theexpressionvalue = 0
		else:
			theexpressionvalue = 1
		
		return theexpressionvalue
	
	#Evaluates the clause
	def EvaluateClause(self, theClause):
		#Turn the passed in string into a list
		evaluatedclause = list(theClause)
		#Variable to represent the return value
		thereturnvalue = 0
		#Loop through the list
		for index in range(len(evaluatedclause)):
			#If the index is equal to !
			if evaluatedclause[index] == "!":
				#Perform the NOT operation on the next index and return the value
				thereturnvalue = self.__NOT(int(evaluatedclause[index+1]))
				#Set the index to its new value
				evaluatedclause[index+1] = thereturnvalue;
			#If the index is equal to V
			elif evaluatedclause[index] == "V":
				#Perform the OR operation on the previous index and next index then return the value
				thereturnvalue = self.__OR(int(evaluatedclause[index-1]),int(evaluatedclause[index+1]))
			#If the index is equal to * and the next index is not equal to )
			elif evaluatedclause[index] == "*" and evaluatedclause[index+1] != "(":
				#Perform the AND operation on the previous index and next index then return the value
				thereturnvalue = self.__AND(int(evaluatedclause[index-1]),int(evaluatedclause[index+1]))
				
		#return the value of the clause
		return thereturnvalue
	
	#Performs the AND operation
	def __AND(self, preNumber, nextNumber):
		#If the numbers match then return one of them
		if(preNumber == nextNumber):
			return preNumber
		#If the numbers dont match then return 0
		else:
			return 0
	
	#Performs the OR operation
	def __OR(self, preNumber, nextNumber):
		#If the numbers dont match then return 1
		if preNumber != nextNumber:
			return 1
		#If the numbers do match then return one of them..it will either be 1 or 0
		else:
			return preNumber
	
	#Performs the NOT operation
	def __NOT(self, nextNumber):
	
		#If the number is 1 then return 0
		if nextNumber == 1:
			return 0
		#If number is not 1 then return 1
		else:
			return 1
	
	#Get the list of expressions
	def getExpressions(self):
		return self.expressionlist
		
	def getFitnessScore(self):
		return self.fitnessscore
		
	def getNumberOfClauses(self):
		return self.totalclauses