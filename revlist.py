while True:
	try:
		x=int(input())
		a=input().split()
		break
	except:
		print("Invalid input")
		break
if(len(a)==x):
	print('->'.join(str(x) for x in a[::-1]))
