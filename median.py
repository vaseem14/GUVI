import statistics
try:
	a=input()
	a=int(a)
	b=[0]
	for x in range(a):
		b= input().split()
		b=int(b)
except:
	e=0
c=statistics.median(b)
print(c)
