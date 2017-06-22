import sys
num = 0
for line in sys.stdin:
	num = int(line)
i = 1
fact = 1
for i in range(1,num+1):
	fact = fact * i
print(fact)
