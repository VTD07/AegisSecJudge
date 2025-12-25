#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long a[10];
    cin>>a[1]>>a[2]>>a[3];
    sort(a+1,a+4);
    cout<<a[3]-a[1];
}