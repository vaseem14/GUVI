while True:
	try:
		b=raw_input()
		x = int(b)
		a=len(b)
		print(a)
		break
	except:
		print("Invalid input")
		break
