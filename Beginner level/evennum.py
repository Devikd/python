lower=int(input("\nenter the lower limit range "))
upper=int(input("\nenter the upper limit range\n"))
for i in range(lower,upper+1):
	if(i%2==0):
		print(i)
