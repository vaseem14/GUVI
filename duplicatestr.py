while True:
	try:
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
b=list(set(b))
print(' '.join(str(x) for x in b))
