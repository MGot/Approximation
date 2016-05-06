import sys
import math
import string

def parseLeftSide(cStr, varCount, OptFunc):
	cStr = cStr.replace(" ", "").replace("*", "")
	tmpStr = ""
	tmpList = []
	if OptFunc:
		C = [0]*(varCount+1)
	else:
		C = [0]*varCount

	if cStr[0] != '-':
		cStr = "+" + cStr

	tmpStr = cStr[0]
	for i in cStr[1:]+' ':
		if i in string.digits:
			tmpStr = tmpStr + i
		elif i in 'x+- ':
			if len(tmpStr) == 1:
				tmpStr = tmpStr + "1"

			if tmpStr[0] == 'x':
				tmpStr = tmpStr[1:]
				C[int(tmpStr)] = tmpList.pop()
			else:
				tmpList.append(int(tmpStr))
			tmpStr = i

	if len(tmpList) != 0 and OptFunc:
		C[-1] = tmpList.pop()

	return C

def isInt(value):
	try:
		int(value)
		return True
	except:
		return False

def isVariable(v):
	if v[0] == 'x' and isInt(v[1:]):
		return True
	else: 
		return False	

def isVariableInequality(cStr):
	signs = [">=","<=", "="]
	tmpSplits = []
	for s in  signs:
		tmpSplits = cStr.split(s)
		if len(tmpSplits)>=2:
			break

	if int(tmpSplits[1]) == 0 and isVariable(tmpSplits[0]):
		return True, s, int(tmpSplits[0][1:])
	else:
		return False, None, None

def parseAb(cStr, varCount):
	signs = [">=","<=", "="]
	tmpSplits = []
	for s in  signs:
		tmpSplits = cStr.split(s)
		if len(tmpSplits)>=2:
			break

	A = parseLeftSide(tmpSplits[0], varCount, False)
	b = int(tmpSplits[1])

	return A, b, s

def readFile(path):
	varCount = 0
	C = []
	A = []
	b = []
	s = []
	d = []
	try:
		f = open(path, 'r')
		for i,l in enumerate(f):
			if i == 0:
				varCount = int(l)
				d = ['R']*varCount
			elif i == 1:
				C = parseLeftSide(l, varCount, True)
			else:
				check, sign, variable = isVariableInequality(l)
				if check:
					d[variable] = sign
				else:	
					Ap, bp, sp =  parseAb(l, varCount)
					A.append(Ap)
					b.append(bp)
					s.append(sp)
		f.close()
	except:
		print("Blad przy czytaniu pliku")
	return C, A, b, s, d


def transpose(A):
	return [[A[j][i] for j in range(0, len(A))] for i in range(0, len(A[0]))]

def print_lp(A, b, C, s, variables):
	max = find_max_long_of_int(A, b, C, variables)
	xes = len(str(len(A[0])))
	str1 = "{{p:3}}{{a:>{}}}{{g:1}}{{x:2}}".format(max, xes)				# '{plus:3}{Aij:>[max]}{gwiazdka:1}{x:2}'
	str2 = "  {{z:1}}	{{b:>{}}}".format(max)						# '  {znak:<2}	{bi:>[max]}'
	n = len(A[0])
	for r in range(0, len(A)):
		row = A[r]
		written = False
		for c in range(0, len(row)):
			if row[c] != 0:
				print(str1.format(a=row[c], x=variables[c], g="*", p=" + " if written else ""), end="")
				written = True
			else:
				print(str1.format(a="", x="", g="", p=""), end="")
		print(str2.format(z=s[r], b=b[r]))
	print("Funkcja celu:")
	written = False
	for i in range(0, len(variables)):
		if C[i] != 0:
			print(str1.format(a=C[i], x=variables[i], g="*", p=" + " if written else ""), end="")
			written = True
		else:
			print(str1.format(a="", x="", g="", p=""), end="")
	print()

def print_Axbc(A, b, C, s, variables, d):
	max = find_max_long_of_int(A, b, C, variables)
	str1 = "{{:>{}}}{{:2}}".format(max)
	print("C = {}".format(C))
	print("|A|*|x|^T (= / ≤ / ≥) |b|")
	print("[", end="")
	for i in range(0, len(variables)):
	    print(str1.format(variables[i] + ("∈R" if d[i] == 'R' else d[i]+"0"), ", " if i < len(A[0])-1 else ""), end="")
	print("]")
	for r in range(0, len(A)):
		row = A[r]
		print("|", end="")
		for c in range(0, len(row)):
			print(str1.format(row[c], ", " if c < len(row)-1 else ""), end="")
		print("| {:1} |".format(s[r]) + str1.format(b[r], " |"))
	print()

def primal_to_dual(A, b, C, s):
	AT = transpose(A)
	sp = []
	for i in range(len(AT)):
		sp.append("=")
	return AT, C, b, sp

def replace_free_var(d, x):
	t = x[:]
	c = 0
	for i in range(0, len(d)):
		if d[i] == 'R':
			t[i+c] = "y{}".format(i+1)
			c += 1
			t.insert(i+c, "z{}".format(i+1))
		elif d[i] == '<=':
			t[i+c] = "y{}".format(i+1)
	return t

def add_s_var(signs, x):
	t = x[:]
	c = 0
	for i in range(0, len(signs)):
		if signs[i] == '<=' or signs[i] == '<':
			t.append("s{}".format(i+1))
			c += 1
		if signs[i] == '>=' or signs[i] == '>':
			t.append("s{}".format(i+1))
			c += 1
	sn = ['=' for s in signs]
	return sn, t, c

def gen_vars(size, var="π"):
	str1 = "{}{{}}".format(var)
	X = []
	for i in range(0, size):
		X.append(str1.format(i+1))
	return X

def find_max_long_of_int(A, b, c, variables):
	amm = len(str(len(variables))) + 3
	max = [
		min([y if y < 0 else -y for y in b]),
		min([y if y < 0 else -y for y in c]),
		min([y if y < 0 else -y for r in A for y in r])
	]
	return len(str(min(max))) if len(str(min(max))) > amm else amm

def convert_to_standard_form(A, S, d, c):
	As = A[:]
	for i in range(len(As)):
		if d[i] == "<=":
			c[i] = c[i]*(-1)
			for k in range (len(As)):
				#As[k].insert(2*i+1,As[k][i+i])
				As[k][i] = As[k][i]*(-1)

	amountOfR = 0
	for i in range(len(d)):
		if d[i] == "R":
			amountOfR += 1
			pos = amountOfR + i
			for j in range(len(As)):
				As[j].insert(pos,As[j][pos-1]*(-1))
			c.insert(pos,-c[pos-1]) # Pompowanie funkcji celu

	for i in range(len(S)):
		if S[i] == "<=":
			As[i].append(1)
			c.append(0)
			for j in range(len(S)):
				if i != j:
					As[j].append(0)

		elif S[i] == ">=":
			As[i].append(-1)
			c.append(0)
			for j in range(len(S)):
				if i != j:
					As[j].append(0)

	return As, c


C, A, b, S, d = readFile(sys.argv[1])


print("_____________________________________________________________________________________")
print("\nPRYMALNE\n")
variables = gen_vars(len(A[0]), var='x')
dp = [x if x == 'R' else "≤" if x == '<=' else "≥" for x in d]
Sp = [x if x == '=' else "≤" if x == '<=' else "≥" for x in S]
print_Axbc(A, b, C, Sp, variables, dp)
print("\n\nUkład:\n")
print_lp(A, b, C, Sp, variables)
print("\n\n")


print("_____________________________________________________________________________________")
print("\nPOSTAĆ STANDARDOWA\n")
As, Cs = convert_to_standard_form(A,S,d,C)
print ("d = ",d)
vars_tmp = replace_free_var(d, variables)
Ss, variablesS, s_len = add_s_var(S, vars_tmp)
ds = ["≥" for i in range(len(variablesS))]
print_Axbc(As, b, Cs, Ss, variablesS, ds)
print("\n\nUkład:\n")
print_lp(As, b, Cs, Ss, variablesS)
print("\n\n")


print("_____________________________________________________________________________________")
print("\nDUALNE\n")
AD, bD, CD, SD = primal_to_dual(As, b, Cs, Ss)
variablesD = gen_vars(len(AD[0]))
dD = ["≥" for i in range(len(variablesD))]
print_Axbc(AD, bD, CD, SD, variablesD, dD)
print("\n\nUkład:\n")
print_lp(AD, bD, CD, SD, variablesD)
