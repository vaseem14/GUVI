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
if (b<=0):
	print("Invalid input")
else:
	if (a<5):
		print("Bill amount:")
		print(75+b)
	elif (a==0):
		print("Bill amount :0")
	elif (a<0):
		print("Invalid input")
	else:
		a=a-5
		c=a*8
		print("Bill amount:")
		print(75+c+b)
		

