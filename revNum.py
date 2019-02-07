while True:
	try:
		a=int(input())
		break
	except:
		print("Invalid input")
		break
b=str(a)
print(b[::-1])
