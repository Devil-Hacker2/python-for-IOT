## program for given number is perfect square

n = int(input())
flag = 0
for i in range(1,1+n//2):
	if n==i*i:
		print("Perfect square")
		break
else:
	print("Not perfect")