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

def genCases(n):
    n = n + 1
    cases = []
    for i in range(pow(2,(n-1))):
        cases.append(list('{0:0b}'.format(i)))
        if len(list('{0:0b}'.format(i))) < n-1:
            for j in range(len(list('{0:0b}'.format(i))),(n-1)):
                cases[i].insert(0,'0')

    for i in range(pow(2,(n-1))):
        cases[i].insert(0,'_')
    return cases

clauses, numOfVar, valueOfClauses = getClauses(sys.argv[1])

#print (numOfVar)
#print (clauses)

#print(fval(clauses,[0, 0, 0, '?'])) 

cases = genCases(numOfVar)
result = []
print(cases)
for i in cases:
        i = ["_"]+[int(j) for j in i[1:]]
        sum1, l = fval_v2(clauses,i)
        print(i[1:])
        print(l)
