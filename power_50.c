#include <stdio.h>
 
int main()
{
    int num;
    int m,flag;
     
    printf("Enter an integer number: ");
    scanf("%d",&num);
     
    m=num;
    flag=0;
  
    while(m!=1)
    {
        if(m%2!=0){
            flag=1;
            break;
        }
        t=t/2;
    }
  
    if(flag==0)
        printf("%d is a number that is the power of 2.",num);
    else
        printf("%d is not the power of 2.",num);
      
    return 0;
}
