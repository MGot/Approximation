import json
from pprint import pprint

def getClauses():
	clauses = []
	
	with open('clauses.txt') as data_file:
		data = json.load(data_file)
	numOfVar = data["numberOfVariables"]
	clauses = data["clauses"]
	
	return clauses, numOfVar



clauses, numOfVar = getClauses()

print (numOfVar)
print (clauses)