from Parser import *
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
			4.Replace candidates based on Fitness, P(t)
			5.Set time t +=1'''
			
def main():
	theTime = 0

	#Parses the file and finds all expressions in the file
	p = Parser("Expressions.txt")
	#Gets the list of expressions that were found
	lists = p.getExpressions()	
	
	#Evaluate expression first - to run each expression in the list we would need to loop through the list and then run algorithm
	#while the fitness score is not equal to the total number of clauses
	'''while p.getFitnessScore() != p.getNumberOfClauses():
		#Run algorithm'''
	
main()