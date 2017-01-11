import sys

#Class that will parse the data
class Parser:	

	numberofclauses = 0
	numberofliterals = 0;
	theliterals = "";
	file = "";

	def __init__(self):
		print "Parser Evoked"
		
	def readfromfile(self, fileName):
		file = open(fileName, "r+")
		fileContents = file.read()
		
		self.parse(fileContents)
		#file.close()
	
	def parse(self, fileContents):
		num = len(fileContents)
		
		for index in range(num):
			if fileContents[index] == "\n":
				#this means its the end of the line
				#calculate the data accordingly
				sys.stdout.write("The Literals: " + Parser.theliterals + "\n")
				sys.stdout.write("The Number Of Clauses: " + str(Parser.numberofclauses) + "\n")
				sys.stdout.write("The Number Of Literals: " + str(Parser.numberofliterals) + "\n")
				Parser.theliterals = ""
				Parser.numberofclauses = 0
				Parser.numberofliterals = 0
			elif fileContents[index] == ")":
				Parser.numberofclauses += 1
			elif fileContents[index] == "a":
				Parser.theliterals += "a"
				Parser.numberofliterals += 1
			elif fileContents[index] == "b":
				Parser.theliterals += "b"
				Parser.numberofliterals += 1
			elif fileContents[index] == "c":
				Parser.theliterals += "c"
				Parser.numberofliterals += 1
			elif fileContents[index] == "d":
				Parser.theliterals += "d"
				Parser.numberofliterals += 1
				
		print fileContents

		
	def getNumberOfClauses(self):
		return Parser.numberofclauses;

	def getLiterals(self):
		return Parser.theliterals;
		
	def getNumberOfLiterals(self):
		return Parser.numberofliterals;