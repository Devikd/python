#include<stdio.h>
void main()
{
    int m;
    printf("enter the no");
    scanf("%d",&m);
    if(m%2==0)
    {
        printf("the nearest even no is %d\n",m-2);
        
    }
    else
    {
        printf("the nearest even no is %d\n",m-1);
    }
}
