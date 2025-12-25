#include<bits/stdc++.h>
using namespace std;
#define ll long long
map<ll,ll> mp,b;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    ll n,t;
    cin>>n;
    vector<ll> a(n);
    for(ll i=0;i<n;i++)
    {
        cin>>a[i];
        b[a[i]]++;
        mp[a[i]]=i;
    }
    cin>>t;
    for(ll i=0;i<n;i++)
    {
        ll ans=t-a[i];
        if(b[ans]>=1)
        {
            if(i<mp[ans]) cout<<i<<" "<<mp[ans];
            else cout<<mp[ans]<<" "<<i;
            return 0;
        }
    }
}
