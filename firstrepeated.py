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
	for j in range(len(a)):
		if (i!=j):
			if (a[i]==a[j]):
				b.append(a[i])
		if(len(b)>=1):
			break
if (len(a)==x):
	if(len(b)!=0):
		b=list(set(b))
		print(' '.join(str(x) for x in b))
	else:
		print("unique")
else:
	print("Invalid input")
