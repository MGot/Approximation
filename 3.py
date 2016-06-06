import json
import sys
from pprint import pprint

def getClauses(f):
	clauses = []
	
	with open(f) as data_file:
		data = json.load(data_file)
	numOfVar = data["numberOfVariables"]
	clauses = data["clauses"]
	
	return clauses, numOfVar

def fval(formula, values):
    l = []
    for clause in formula:
        if cval(clause, values):
            l.append(1)
        else:
            l.append(0)
    return sum(l), l

def cval(clause, values):
    for x in clause:
        if values[abs(x)] == "?":
            pass
        elif (x > 0 and bool(values[x])) or (x < 0 and not bool(values[-x])):
                return True
    return False


clauses, numOfVar = getClauses(sys.argv[1])

print (numOfVar)
print (clauses)

print(fval(clauses,[0, 0, 0, '?'])) 
