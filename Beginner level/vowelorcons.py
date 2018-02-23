b=input()
c=['a','e','i','o','u','A','E','I','O','U']
if b.isnumeric() :
	print("invalid")
elif b in c:
	print("vowel")
else:
	print("consonent")
