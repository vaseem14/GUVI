import itertools
from textwrap import wrap
a=input()
a=list(a)
b=list(itertools.permutations(a))
d=""
for i in range(len(b)):
	d=d.join(b[i])
c=len(a)
d=wrap(d,c)
b=list(set(b))
print('\n'.join(str(x) for x in d))
