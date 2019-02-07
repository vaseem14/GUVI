while True:
	try:
		x = int(input())
		break
	except:
		print("Invalid input")
		break
if x%2:
	print('Even')
else:
	print('Odd')
