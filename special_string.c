#include <stdio.h>

int main()
{
char c[30];
int i=0;
static int spl=0,num=0,alp=0,spc=0;
printf("enter the string:\n");
scanf("%[^\n]s",c);
while(c[i]!='\0')
{
if((c[i]>='a'&&ch[i]<='z')||(c[i]>='A'&&c[i]<='Z'))
{
	alp++;
}
else if(c[i]>='0'&&c[i]<='9')
{
	num++;
}
else if(c[i]==' ')
{
	spc++;
}
else
{
	spl++;	
}
i++;
}

printf("%d",spl);
	return 0;
}
