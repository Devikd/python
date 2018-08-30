#include<stdio.h>
int main()
{
char v1[30],v2[30];
int i=0,j=0;
printf("enter the string");
gets(v1);
printf("enter the string");
gets(v2);
while(v1[i]!='\0')
{
i++;
}
while(v2[j]!='\0')
{
v1[i]=v2[j];
j++;
i++;}
v1[i]!='\0';
printf("concatenate string is %s",v1);
}
}
