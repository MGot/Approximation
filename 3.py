import json
import sys
from pprint import pprint

def getClauses(f):
	clauses = []
	
	with open(f) as data_file:
		data = json.load(data_file)
	
	numOfVar = data["numberOfVariables"]
	clauses = data["clauses"]
	valueOfClauses = data["valueOfClauses"]
	
	return clauses, numOfVar, valueOfClauses

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

def fval_v2(formula, values):
    l = []
    for clause in formula:
        val, _ = cval_v2(clause, values)
        if val: 
            #print("pr")
            l.append(1)
        elif val == False:
            #print("fal")
            l.append(0)
        else:
            #print("none")
            l.append(None)
    return sum([i for i in l if i!=None]), l

def cval_v2(clause, values):
    unknown = False
    value = False
    unknown_count = 0
    for x in clause:
        if values[abs(x)] == "?":
            unknown = True
            unknown_count = unknown_count + 1
        elif (x > 0 and bool(values[x])) or (x < 0 and not bool(values[-x])):
                value = True
    if unknown and not value:
        return None, unknown_count
    return value, unknown_count

def expected_Wc(clause, values, valueOfClause):
	val, count = cval_v2(clause, values)
	print("ewc",val)
	print("ewc",count)
	print("ewc val", valueOfClause)
	if val:
		return valueOfClause
	elif val==False:
		return 0
	else:
		return float(valueOfClause*(1-pow(0.5,count)))

def expected_W(clauses, values, valueOfClauses):
	expected = 0.0
	for i in range(len(clauses)):
		expected = expected + expected_Wc(clauses[i], values, valueOfClauses[i])
	return expected


clauses, numOfVar, valueOfClauses = getClauses(sys.argv[1])

print (numOfVar)
print (clauses)

print(fval_v2(clauses,['_', '?', '?', '?']))
print(expected_W(clauses,['_', '?', '?', '?'],valueOfClauses))
print(fval_v2(clauses,['_', 1, '?', '?'])) 
print(expected_W(clauses,['_', 1, '?', '?'],valueOfClauses))
print(fval_v2(clauses,['_', 0, 1, '?']))  
print(expected_W(clauses,['_', 1, 1, '?'],valueOfClauses))