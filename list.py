try:
	a=input()
	a=int(a)
	b=[0]
	for x in range(a):
		b= input().split()
		b=int(b)
except:
	e=0

c=b[0]
for i in range(a):
	for j in range(a):
		if b[i]<b[j]:
			d=b[j]
		else:
			d=b[i]
		if d>c:
			c=d
print(c)
