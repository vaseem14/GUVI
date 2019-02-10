while True:
	try:
		x=input()
		x=int(x)
		a=input().split()
		break
	except:
		print("Invalid input")
		break
b=[]
for i in range(len(a)):
	if (int(a[i])==i):
		b.append(int(a[i]))
if (len(a)==x):
	if (len(b)==0):
		print("-1")
	else:
		b=list(set(b))
		print(' '.join(str(x) for x in b))
else:
	print("Invalid input")
