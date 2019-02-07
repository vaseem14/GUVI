while True:
	try:
		a, b= input().split( )
		a=int(a)
		b=int(b)
		break
	except:
		print("Invalid input")
		break
for x in range(a+1,b):
	if x%2==0:
		print(x,end=' ')
		
		
