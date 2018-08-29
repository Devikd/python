#include<stdio.h>
int main()
{
int i,j,b[20],v,n;
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&b[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(b[i]>b[j])
{
v=b[i];
b[i]=b[j];
b[j]=v;
}
}
}
printf("%d",b[n-1]);
return 0;
}
