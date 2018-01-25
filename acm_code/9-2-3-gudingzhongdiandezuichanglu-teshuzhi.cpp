#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
#define maxn 100+10

int V[maxn];
int n;
int d[maxn];

int dp(int S)
{
	int& ans = d[S];

	if(ans != -1) return ans;
	ans = -1 << 30;
	for(int i =0; i < n; ++i)
    {
        if(S >= V[i])
		{
			int tmp = dp(S - V[i]);
			if(ans < tmp + 1) ans = tmp + 1;
		}
    }

	return ans;
}

int main()
{
    int S;
	cout << "Please input n and S:" <<endl;
	cin >> n >> S;

	for(int i = 0; i < n; i++)
	{
		cin >> V[i];
	}

	sort(V, V + n);
	memset(d, -1, sizeof(d));
	d[0] = 0;
	int ans = dp(S);
	cout << ans <<endl;
	return 0;
}
