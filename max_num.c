#include<stdio.h>
int main()
{
int i,j,a[20],v,n;
scanf("%d",&n);
for(i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<n;i++)
{
for(j=i+1;j<n;j++)
{
if(a[i]>a[j])
{
v=a[i];
a[i]=a[j];
a[j]=v;
}
}
}
printf("%d",a[n-1]);
return 0;
}
