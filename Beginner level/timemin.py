#include <stdio.h>
int main(void) 
{
int hours1,hours2,mins1,mins2,hours3,mins3;
scanf("%d %d\n",&hours1,&mins1);
scanf("%d %d\n",&hours2,&mins2);
hours3=abs(hours1-hours2);
mins3=abs(mins1-mins2);
printf("%d %d",hours3,mins3);
	return 0;
}
