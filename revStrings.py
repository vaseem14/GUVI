a=input().split()
b=[]
for i in range(len(a)):
	if(a[i].isalpha()):
		c=a[i][::-1]
		b.append(c)
	else:
		print("Invalid input")
		
b=list(set(b))
print(' '.join(str(x) for x in b))
