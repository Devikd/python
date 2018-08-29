#include<stdio.h>
#include<string.h>
#include<ctype.h>
void main()
{
char v[50];
int n,i,count=1;
printf("ENTER THE INPUT SENTENCE:\n");
gets(v);
n=strlen(v);
printf("\nTHE LENGTH OF SENTENCE IS %d",n);
for(i=0;i<n;i++)
{
if(v[i]=='\.')
{
count++;
}
}
printf("\nTHE NO.OF.LINES IN THE GIVEN PARAGRAPH ARE %d",count);
}
