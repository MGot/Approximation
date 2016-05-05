import sys
import math
import string as str

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
		if i in str.digits:
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

C = []
A = []
b = []
s = []

C, A, b, s = readFile(sys.argv[1])

print("C",C)
print("A",A)
print("b",b)
print("s",s)