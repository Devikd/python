 #include<iostream>
using namespace std;
int main()
{
    int a,b,v;
    a=10;
    b=20;
    v=a^b;
    b=b^v;
    a=t^b;
    cout<<"a="<<a<<" b="<<b;
    return 0;
