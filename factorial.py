while True:
	try:
		a=int(input())
		break
	except:
		print("Invalid input")
		break
b=1
for x in range(2,a):
	b=b*x
print(b*a)
