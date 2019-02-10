while True:
	try:
		x=input()
		x=int(x)
		a=input().split()
		break
	except:
		print("Invalid input")
		break
a=sorted(a,reverse=True)
if (len(a)==x):
	for i in range(len(a)):
		print(a[i],end="")
else:
	print("Invalid input")
