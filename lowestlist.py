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
		z=int(b[i])-int(b[j])
		if z>0:
			d=b[j]
		else:
			d=b[i]
			y=int(d)-int(c)
	if y>0:
			c=d
print(c)
