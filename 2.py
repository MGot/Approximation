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

def parseAb(cStr, varCount):
	signs = [">=","<=", "=", ">", "<"]
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
	try:
		f = open(path, 'r')
		for i,l in enumerate(f):
			if i == 0:
				varCount = int(l)
			elif i == 1:
				C = parseLeftSide(l, varCount, True)
			else:
				Ap, bp, sp =  parseAb(l, varCount)
				A.append(Ap)
				b.append(bp)
				s.append(sp)
		f.close()
	except:
		print("Blad przy czytaniu pliku")
	return C, A, b, s


def transpose(A):
	return [[A[j][i] for j in range(0, len(A))] for i in range(0, len(A[0]))]

def print_lp(A, b, C, s, zmienna="π"):
	max = find_max_long_of_int(A, b, C)
	xes = len(str(len(A[0])))
	str1 = "{{p:3}}{{a:>{}}}{{g:1}}{{x:1}}{{j:<{}}}".format(max, xes)			# '{plus:3}{Aij:>[max]}{gwiazdka:1}{x:1}{indeks_x:<[xes]}'
	str2 = "  {{z:<2}}	{{b:>{}}}".format(max)									# '  {znak:<2}	{bi:>5}'
	n = len(A[0])
	for r in range(0, len(A)):
		row = A[r]
		written = False
		for c in range(0, len(row)):
			if row[c] != 0:
				print(str1.format(a=row[c], x=zmienna, g="*", j=c+1, p=" + " if written else ""), end="")
				written = True
			else:
				print(str1.format(a="", x="", g="", j="", p=""), end="")
		print(str2.format(z=s[r], b=b[r]))
	print("FUNKCJA CELU:")
	written = False
	for i in range(0, len(C[:-1])):
		if i != 0:
			print(str1.format(a=i, x=zmienna, g="*", j=i+1, p=" + " if written else ""), end="")
			written = True
		else:
			print(str1.format(a="", x="", g="", j="", p=""), end="")
	print()

def print_Axbc(A, b, C, s, zmienna="π"):
	max = find_max_long_of_int(A, b, C)
	str1 = "{{:{}}}{{:2}}".format(max)
	print("C = {}".format(C))
	print("s = {}".format(s))
	print("A || b = ")
	for r in range(0, len(A)):
		row = A[r]
		for c in range(0, len(row)):
			print(str1.format(row[c], ", " if c < len(row)-1 else ""), end="")
		print("|| ", end="")
		print(str1.format(b[r], ""))
	print("{} = [".format(zmienna), end="")
	for i in range(0, len(A[0])):
		print("{}{}{}".format(zmienna, i+1, ", " if i < len(A[0])-1 else ""), end="")
	print("]")

def primal_to_dual(A, b, C, s):
	AT = transpose(A)
	sp = []
	for i in s:             # po sprowadzeniu do standardowej do poprawki
		if i == ">":
			sp.append("<")
		elif i == "<":
			sp.append(">")
		elif i == ">=":
			sp.append("<=")
		elif i == "<=":
			sp.append(">=")
		else:
			sp.append("=")
	return AT, C, b, sp

def find_max_long_of_int(A, b, c):
	x = [
		min([y if y < 0 else -y for y in b]),
		min([y if y < 0 else -y for y in c]),
		min([y if y < 0 else -y for r in A for y in r])
	]
	return len(str(min(x)))

C = []
A = []
b = []
s = []

C, A, b, s = readFile(sys.argv[1])

print("PRYMALNE")
print_Axbc(A, b, C, s, zmienna="x")
print("\n\n")
#print_lp(A, b, C, s, zmienna="x") # ten ok
AT, bT, CT, sT = primal_to_dual(A, b, C, s)
print("\n\n")
print("DUALNE")
print_Axbc(AT, bT, CT, sT)
print("\n\n")
#print_lp(AT, bT, CT, sT) # nie ma jeszcze wszystkich znaków takich samych, więc się sypnie
