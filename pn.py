while True:
	try:
		x = int(input())
		break
	except:
		print("Invalid input")
		break
if x>0:
	print('Positive')
elif x==0:
	print('Zero')
else:
	print('Negative')
