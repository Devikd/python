num=int(input())
temp=num
sum=0
while (temp>0):
	rem=temp%10
	sum=sum+rem**3
	temp//=10
if(num==sum):
	print(num,"is amstrong number")
else:
	print(num,"is  not amstrong number")
