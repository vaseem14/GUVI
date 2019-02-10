while True:
	try:
		a=input().split()
		break
	except:
		print("Invalid input")
		break
print('->'.join(str(x) for x in a[::-1]))
