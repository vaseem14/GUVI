import itertools
a=input()
a=list(a)
b=list(itertools.permutations(a))
for i in range(len(b)):
	for j in range(len(a)):
		print(b[i][j],end="")
	print("")
