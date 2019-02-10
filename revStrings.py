a=input().split()
b=[]
for i in range(len(a)):
	a[i]=a[i][::-1]
print(' '.join(str(x) for x in a))
