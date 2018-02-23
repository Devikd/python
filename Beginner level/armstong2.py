lower=int(input())
upper=int(input())
for num in range(lower,upper+1):
	order=len(str(num))
	temp=num
	sum=0
	while (temp>0):
		rem=temp%10
		sum=sum+rem**order
		temp//=10
	if(num==sum):
		print(num)
