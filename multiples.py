while True:
	try:
		a=int(input())
		break
	except:
		print("Invalid input")
		break
b=0
if(a>0):
	for x in range(a):
		b=a+a
		c=b+a
		d=c+a
		e=d+a
	print(a,b,c,d,e)
else:
	print("0 0 0 0 0")
