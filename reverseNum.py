import sys
num = 0
for line in sys.stdin:
	num = int(line)
temp = num
ans = 0
while temp > 0 :
	t = temp % 10
	ans = (ans * 10) + t
	temp = temp // 10
print(ans)
