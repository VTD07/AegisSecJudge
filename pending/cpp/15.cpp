#include<bits/stdc++.h>
using namespace std;
#define ll long long
map<ll,ll> mp;
ll n,t;
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    cin>>n;
    vector<ll> a(n);
    for(ll i=0;i<n;i++)
    {
        cin>>a[i];
        mp[a[i]]=i;
    }
    cin>>t;
    for(ll i=0;i<n;i++)
    {
        ll ans=t-a[i];
        if(mp.count(ans) and mp[ans]!=i)
        {
            if(i<mp[ans]) cout<<i<<" "<<mp[ans];
            else cout<<mp[ans]<<" "<<i;
            return 0;
        }
    }
}
