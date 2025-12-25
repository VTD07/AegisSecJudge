#include<bits/stdc++.h>
#define fo(i,x,n) for(int i=x;i<=n;++i)
#define fi(i,x,n) for(int i=x;i>=n;--i)
#define SYNCHRONIZE ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define ll long long 
#define ld long double
#define pii pair<int,int> 
#define pil pair<int,ll>
#define BIT(i,mask) ((mask >> (i-1)) & 1) 
#define pli pair<ll,int>
#define maxn 100005 
#define pll pair<ll,ll>
#define uni(vt) vt.resize(unique(vt.begin(),vt.end()) - vt.begin());
#define DAOBIT(i,mask) ((mask ^ (1ll<<i-1))) 
#define OFFBIT(i,mask) ((mask & ~(1ll << (i - 1))))
#define ONBIT(i,mask) ((mask | (1ll << (i - 1)))) 
const ll mod =1e9+7;
using namespace std;
//----------------- STRUCTURE ---------------

//----------------- DECLARE ------------------
int n, m,k;
ll dp[maxn][24][24], sum[maxn][24][24];
string A, B;
//----------------- FUNCTION -----------------

//----------------- MAIN PRO ------------------
int main()
{  
    SYNCHRONIZE;

    cin >> n >> m >> k >> A >> B ;
    A = ' '+A;
    B = ' ' +B;

    sum[0][0][0] = 1;

    fo(t, 0, k) 
        fo(j, 0, m)   
            fo(i, 1, n) {
                sum[i][j][t] = sum[i-1][j][t];
                
                if(A[i] == B[j]) {
                    if(j > 0) {
                        dp[i][j][t] = dp[i-1][j-1][t] ;
                        if(t > 0) dp[i][j][t] = (dp[i][j][t] + sum[i-1][j-1][t-1]) % mod;
                    }
                    sum[i][j][t] = (sum[i][j][t] + dp[i][j][t]) % mod;
                }
        
            }

    cout << sum[n][m][k];

}