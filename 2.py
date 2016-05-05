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

def print_lp(A, b, c, s):
    max = find_max_long_of_int(A, b, c)
    xes = len(str(len(A[0])))
    str1 = "{{p:3}}{{a:>{}}}{{g:1}}{{x:1}}{{j:<{}}}".format(max, xes)           # '{plus:3}{Aij:>[max]}{gwiazdka:1}{x:1}{indeks_x:<[xes]}'
    str2 = "  {{z:<2}}  {{b:>{}}}".format(max)                                  # '  {znak:<2}  {bi:>5}'
    n = len(A[0])
    for r in range(0, len(A)):
        row = A[r]
        written = False
        for c in range(0, len(row)):
            if row[c] != 0:
                print(str1.format(a=row[c], x="x", g="*", j=c+1, p=" + " if written else ""), end="")
                written = True
            else:
                print(str1.format(a="", x="", g="", j="", p=""), end="")
        print(str2.format(z=s[r], b=b[r]))

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

print("C",C)
print("A",A)
print("b",b)
print("s",s)
print_lp(A, b, C, s)
