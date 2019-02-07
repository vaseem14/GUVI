while True:
	try:
		a= raw_input()
		break
	except:
		print("Invalid input")
		break
b=a[::-1]
if a==b:
	print('yes')
else :
	print('no')
