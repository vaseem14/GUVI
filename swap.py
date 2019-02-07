a=input()
b=[]
b=([a[i:i+1] for i in range(0, len(a), 1)])
t=0
i=0
for x in range(0,len(a),2):
	t=b[i]
	b[i]=b[i+1]
	b[i+1]=t
	i=i+2
print(b)
	
