#include <stdio.h>
int main(void)
{
int a,rev=0;
printf("enter the  numbers");
scanf("%d",&a);
while(a!=0)
{
rev=rev*10;
rev=rev+ a%10;
a=a/10;
}
printf("the swapped number is %d",rev);
	return 0;
}
