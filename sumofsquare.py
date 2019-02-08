while True:
	try:
		a=int(input())
		break
	except:
		print("Invalid input")
		break
e=len(str(a))
c=list(str(a))
b=0
for x in range(e):
	d=int(c[x])*int(c[x])
	b=b+d
print(b)	
