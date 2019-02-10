while True:
	try:
		a=input()
		a=list(a)
		break
	except:
		print("Invalid input")
		break
a=list(set(a))
print(''.join(str(x) for x in a))
