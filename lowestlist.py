try:
	a=input()
	a=int(a)
	b=[0]
	for x in range(a):
		b= input().split()
		b=int(b)
except:
	e=0

c=min(b)
print(c)
