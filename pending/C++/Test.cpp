#include <bits/stdc++.h>

using namespace std;
bool ktra(long long k)
{
    long long h=k,s=0;
    while(h>0)
    {
        s+=h%10;
        h/=10;
    }
    if(s==6)
    {
        return true;
    }
    else
    {
        return false;
    }
}
long long a,b,kq;

int main()
{
    cin>>a>>b;
    if(a%2!=0)
    {
        a++;
    }
    if(b%2!=0)
    {
        b++;
    }
    for(int i=a;i<=b;i+=2)
    {
        if(ktra(i)) kq+=i;
    }
    cout<<kq;
}
