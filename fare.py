while True:
	try:
		a=int(input("Enter the distance in km: \n"))
		x,y=input("Duration hh:mm : \n").split(':')
		x=int(x)
		y=int(y)
		break
	except:
		print("Invalid input")
		break
x=x*60
b=x+y
if (a<5):
	print("Bill amount:")
	print(75+b)
else:
	a=a-5
	c=a*8
	print("Bill amount:")
	print(75+c+b)
	

