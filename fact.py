while True:
	try:
		ca=int(input())
		break
	except:
		print("Invalid input")
		break
b=1
if ca==0:
	print('1')
else:
	for x in range(2,ca):
		b=b*x
	print(b*ca)
