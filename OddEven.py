while True:
	try:
		x = int(input())
		break
	except:
		print("Invalid input")
		break
if x%2==0:
	print('Even')
else:
	print('Odd')
