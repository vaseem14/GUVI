while True:
	try:
		a = int(input())
		b = int(input())
		c = int(input())
		break
	except:
		print("Invalid input")
		break
if a>b:
	if a>c:
		print (a)
	elif c>a:
		print(c)
elif b>a:
	if b>c:
		print (b)
	elif c>b:
		print(c)
