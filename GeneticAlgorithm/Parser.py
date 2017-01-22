import sys

#Class that will parse the data
#This class is responsible for reading in from a file and getting all of
#the expressions in the file
class Parser:	
	#Initialize Parser object
	def __init__(self, filePath):
		#This is used to map literals with values
		self.dictionary = {'a': 1, 'b': 0, 'c': 1, 'd': 0}
		#The total number of clauses
		self.numberofclauses = 0
		#The expression list used to hold the expressions found in the file
		self.expressionlist = []
		#Read from the file
		self.__readfromfile(filePath)
		
	#Read from a file
	def __readfromfile(self, thefileName):
		#The file string
		theFile = ""
		#Open the file for reading and writing
		theFile = open(thefileName, "r+")
		#Store the file contents into the variable
		fileContents = theFile.read()
		#Parse the file
		self.__parse(fileContents)
		#Close the file
		theFile.close()
	
	#Parse the data inside the file and find all the expressions
	def __parse(self, fileContents):
		#Holds data for an expression
		theexpression = ""
		#The lenght of the contents of the file
		num = len(fileContents)
		#To hold record of the line count
		lineCount = 0
		#The literals found
		theliterals = []
		#The number of literals
		numberofliterals = 0
		
		#Print the operator definitions
		sys.stdout.write("Operators: \n! is NOT\n* is AND\nV is OR\n\n")
		#Loop through the file contents
		for index in range(num):
			#If the current index of the file contents is not a new line
			if (fileContents[index] != "\n"):
				#Add it to the expression variable
				theexpression += fileContents[index]
			
			#If the current index of the file contents is a new line
			if (fileContents[index] == "\n"):
				#Sort the literals
				theliterals.sort()
				#Increase the line count
				lineCount += 1
				#Add this to the expression list
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
			#Else
			else:
				#Check if the index is inside the literals list, if it is
				if (fileContents[index] in theliterals):
					#Just continue
					continue;
				#If the index is inside the dictiontary then..
				elif fileContents[index] in self.dictionary:
					#Increment the number of literals
					numberofliterals += 1
					#Add the character to the literals list
					theliterals.append(fileContents[index]);

	#Function used to print data
	def __printfunction(self, lines, expression, theliterals, numofliterals):
		#Print the number of the line the expression is on, in the file
		sys.stdout.write("Line: " + str(lines) + "\n")
		#Print the expression
		sys.stdout.write("The Expression: " + expression + "\n")
		#Print the literals
		sys.stdout.write("The Literals: " + " ".join(theliterals) + "\n")
		#Print the number of clauses
		sys.stdout.write("The Number Of Clauses: " + str(self.numberofclauses) + "\n")
		#Print the number of literals
		sys.stdout.write("The Number Of Literals: " + str(numofliterals) + "\n" + "\n")
		
	#Get the list of expressions
	def getExpressions(self):
		return self.expressionlist