#include <bits/stdc++.h>
 using namespace std;
int main() { int n,a[100005]; map<int,int> mp; cin>>n; for(int i=1; i<=n; i++) {cin>>a[i]; mp[a[i]]=i;} int target; cin>>target; for(int i=1; i<=n; i++) if(mp[target-a[i]]) {cout<<i<<" "<<mp[target-a[i]]; return 0; } 
return 0;}