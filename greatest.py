while True:
	try:
		a=input()
		a=list(a)
		break
	except:
		print("Invalid input")
		break
b=sorted(a,reverse=True)
if(a<b):
	print(''.join(str(x) for x in b))
else:
	print("impossible")
