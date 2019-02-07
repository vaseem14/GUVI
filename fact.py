while True:
	try:
		c=int(input())
		break
	except:
		print("Invalid input")
		break
b=1
if c==0:
	print('1')
else:
	for x in range(2,c):
		b=b*x
	print(b*c)
