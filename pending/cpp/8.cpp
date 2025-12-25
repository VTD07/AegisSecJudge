#include<bits/stdc++.h>
using namespace std;
int main(){
   long long a,b,c;
   cin>>a>>b>>c;
   long long x,y;
   if (a>=b and a>=c) x=a;
   else if (b>=a and b>=c) x=b;
   else x=c;
   if (a<=b and a<=c) y=a;
   else if (b<=a and b<=c) y=b;
   else y=c;
   cout<< x-y;
   return 0;
}