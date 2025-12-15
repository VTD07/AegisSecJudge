#include<bits/stdc++.h>
using namespace std;
typedef long long l2;
const int nmax=1e6+9;
const l2 mod=1209;
l2 a,n;
l2 mu(l2 a,l2 n)
{
    if(n==0) return 1;
    l2 tam=mu(a,n/2);
    tam=(tam*tam)%mod;
    if(n%2!=0) tam=(tam*a)%mod;
    return tam;
}
l2 cal(l2 a,l2 n)
{
    if(n==1) return a;
    l2 tam=cal(a,n/2);
    tam=(tam%mod*(1+mu(a,n/2))%mod)%mod;
    if(n%2!=0) tam=(tam+mu(a,n))%mod;
    return tam;
}
signed main ()
{
    // freopen("TONGCSNMOD.inp","r",stdin);
    // freopen("TONGCSNMOD.out","w",stdout);
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);cout.tie(NULL);
    cin>>a>>n;
    cout<<cal(a,n)+1;
}