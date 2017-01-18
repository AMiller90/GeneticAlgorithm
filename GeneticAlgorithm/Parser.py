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
		self.clauseReturnValueslist = []
		self.theSelectedMembers = []
		
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
		
	#Get the list of expressions
	def getExpressions(self):
		return self.expressionlist