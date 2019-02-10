while True:
	try:
		a,b,c=input().split()
		a=int(a)
		b=int(b)
		c=int(c)
		break
	except:
		print("Invalid input")
		break
d=b+c
if(a%d==0):
	print("YES")
else:
	print("NO")	
