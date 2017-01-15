from Parser import *

def main():
	#Parses the file and finds all expressions in the file
	p = Parser("Expressions.txt")
	#Gets the list of expressions that were found
	lists = p.getExpressions()
	#Evaluate does exactly that for an expression
	for expression in lists:
		print(p.EvaluateExpression(expression))
	
main()