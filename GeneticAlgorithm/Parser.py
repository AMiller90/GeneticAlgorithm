import sys

#Class that will parse the data
class Parser:	

	def __init__(self, filePath):	 
		self.filename = filePath
		self.numberofclauses = 0
		self.numberofliterals = 0
		self.theliterals = []
		self.file = ""
		self.__readfromfile(filePath)

	def __readfromfile(self, thefileName):
		self.file = open(thefileName, "r+")
		fileContents = self.file.read()
		
		self.__parse(fileContents)
		self.file.close()
	
	def __parse(self, fileContents):
		theexpression = ""
		num = len(fileContents)
		lineCount = 0
		
		sys.stdout.write("Operators: \n! is NOT\n* is AND\nV is OR\n\n")
		for index in range(num):
			if fileContents[index] != "\n":
				theexpression += fileContents[index]
				
			if fileContents[index] == "\n":
				self.theliterals.sort()
				lineCount += 1

				self.__printfunction(lineCount, theexpression)
				theexpression = ""
				del self.theliterals[:]
				self.numberofclauses = 0
				self.numberofliterals = 0
			elif fileContents[index] == ")":
				self.numberofclauses += 1
			elif fileContents[index] == "!":
				continue;
			elif fileContents[index] == "V":
				continue;
			elif fileContents[index] == "*":
				continue;
			elif fileContents[index] == "(":
				continue;
			else:
				if fileContents[index] in self.theliterals:
					continue;
				self.numberofliterals += 1
				self.theliterals.append(fileContents[index]);

	def __printfunction(self, lines, expression):
		sys.stdout.write("Line: " + str(lines) + "\n")
		sys.stdout.write("The Expression: " + expression + "\n")
		sys.stdout.write("The Literals: " + " ".join(self.theliterals) + "\n")
		sys.stdout.write("The Number Of Clauses: " + str(self.numberofclauses) + "\n")
		sys.stdout.write("The Number Of Literals: " + str(self.numberofliterals) + "\n" + "\n") 
	