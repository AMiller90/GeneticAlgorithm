from Parser import *
from Population import *
import time
import sys
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
			
def main():

	#Parses the file and finds all expressions in the file
	p = Parser("Expressions.txt")
	#Gets the list of expressions that were found in the file
	lists = p.getExpressions()	
	
	#Initialize the generation count
	theTime = 0
	
	#For time being we will only parse the first expression to run the algorithm.
	#Once algorithm is working correctly then we will code it to where it will run
	#the algorithm for each expression found
	#Initialize a population
	population = Population(lists[0])
	
	population.SelectMembers()
	population.changePopulation()
	#while the fitness score is not equal to the total number of clauses
	'''while population.getFitnessScore() != population.getNumberOfClauses():
		#Run algorithm
		#Step 1 - Evaluate fitness of each member of Population
		#population.EvaluateExpression()
		#Step 2 - Select members based on fitness
		#Step 3 - Make OffSpring internally done in Select Members function
		#population.SelectMembers()
		#Step4 - Replace candidates based on Fitness'''
		
	#Step5 - Increment generation
	theTime += 1

main()