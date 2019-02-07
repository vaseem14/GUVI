x=raw_input()
a=x.isalpha()
if len(x)==1:
	if a==True:
			if x in ('a', 'e', 'i', 'o', 'u','A','E','I','O','U'):
				print('Vowel')
			else:
				print('Consonant')
	else:
		print('invalid')		
else:
	print('invalid')
