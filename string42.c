#include<stdio.h>
#incude<conio.h>
void main()
{
int k,d;char a[20],c[20];
printf("enter the value of a and c");
scanf("%s %s",&a,&c);
k=strlen(a);
d=strlen(c);
if(k>=d)
{
printf("%s",a);
}
else
{
printf("%s",c);
}
}
