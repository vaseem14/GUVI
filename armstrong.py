while True:
	try:
		n = input()
		break
	except:
		print("Invalid input")
		break
a=len(n)
s=0
x=0
c=int(n)
for i in range(0,a):
    x=int(n[i])
    s=s+x**a
if s==c:
    print("yes")
else:
    print("no")
