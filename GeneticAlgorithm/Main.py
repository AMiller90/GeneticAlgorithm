from Parser import *
from Population import *
import time

'''The Algorithm 
	begin
		set t = 0;
		Init Population P(t)
	
		while termination condition not met do
			begin
				(Evaluate - check fitness score of each clause) true means fittest
				1.Evaluate fitness of each member of Population P(t)
				2.Select members based on fitness
				3.Make offspring
				Mutation
				4.Replace candidates based on Fitness, P(t)
				5.Set time t +=1'''

#The Genetic Algorithm
def theAlgorithm(theExpression):

	#Initialize a population
	population = Population(theExpression)
	#Initialize the generation count
	theGeneration = 0
	#Get the start time
	start = time.time()
	
	#while the fitness score is not equal to the total number of clauses
	while population.getFitnessScore() != population.getNumberOfClauses():
		#Run algorithm
		#Step 1 - Evaluate fitness of each member of Population
		population.EvaluateExpression()
		#Step 2 - Select members based on fitness
		#Step 3 - Make OffSpring internally done in Select Members function
		population.SelectMembers()
		#Step4 - Replace candidates based on Fitness
		population.changePopulation()
		print("Solving")
		#Step5 - Increment generation
		theGeneration += 1
	
	
	end = time.time()
	
	print("The Solution Gene")
	print(population.getSolutionGene())
	#Get seconds
	seconds = (end - start) / 60
	print(str(theGeneration) + " generations in: " + str(round(seconds,1)) + " seconds.")

#The main function
def main():
	#Variable for the application loop
	applicationLoop = True
	#Prompt user to enter the file name to read from
	print("Enter filename to read from.")
	print("Must have quotation marks and extension type.")
	print("Example: \"Expressions.txt\"")
	#Grab the input and store it
	thefile = input()
	#Parses the file and finds all expressions in the file
	p = Parser(thefile)
	#Gets the list of expressions that were found in the file
	lists = p.getExpressions()

	#The Application Loop
	while(applicationLoop):
		#Prompt user how to quit
		print("Enter 0 to quit")
		#Prompt the user to input the line number of the expression to evaluate
		expressionIndex = input("Enter the line number of the expression to evaluate: ")
		#Print new lines to help stop cluttered screen
		print("\n" * 25)
		#If the user inputs 0
		if(expressionIndex == 0):
			#Print Quit Application
			print("Quit Application")
			#Set variable to false and exit
			applicationLoop = False;
		#Else
		else:
			#Set the index to the appropriate number for iteration
			expressionIndex = expressionIndex - 1
			#Run the Algorithm - Pass in the expression
			theAlgorithm(lists[expressionIndex])

main()