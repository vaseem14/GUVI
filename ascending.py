try:
	a=input()
	a=int(a)
	b=[0]
	for x in range(a):
		b= input().split()
		b=int(b)
except:
	e=0
b=sorted(b,key=int)
for x in range(a):
	print(b[x],end=" ")
