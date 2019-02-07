while True:
	try:
		a, b= input().split( )
		a=int(a)
		b=int(b)
		break
	except:
		print("Invalid input")
		break
c=0
for x in range(a+1,b):
	if x%2==0:
		c=c+1
		
for x in range(a+1,b):
	if x%2==0:
		if c>0:
			print(x,end=' ')
		else:
			print(x)
		
