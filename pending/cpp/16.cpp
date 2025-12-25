#include<bits/stdc++.h>

#define fi first
#define se second 
#define nhmt main()
#define docnhanh ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define mod 1000000007

using namespace std;

//===============declare===============

long long n,m,res;
long long u,v,dem;
long long a[1005];
long long t,x,y,k,ans;
string s;

//===============function==============
void mo()
{
	freopen("nhap.inp","r",stdin);
	freopen("nhap.out","w",stdout);
}
void inra()
{
	long long dem=0;
	for(long long i=1;i<=n;i++)
	{
		if(a[i]==0)
		{
			dem++;
		}
	}
	if(dem==k)
	{
		for(long long i=1;i<=n;i++)
		{
			if(a[i]==0)
			{
				cout<<i<<" ";
			}
		}
		ans++;
		cout<<'\n';
	}
}
void sinhday(long long i)
{
	for(long long j=0;j<=1;j++)
	{
		a[i]=j;
		if(i==n)
		{
			inra();
		}
		else sinhday(i+1);
	}
}
//================code=================
nhmt
{
	//mo();
	docnhanh
	ans=0;
	cin>>k>>n;
	sinhday(1);
	cout<<ans;
	return 0;
}
/*===============end===================
Code by vinh_nguyenhuumanhtuong
*/