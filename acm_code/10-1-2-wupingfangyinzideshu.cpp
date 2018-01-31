#include <iostream>
#include <cmath>
#include <cstring>
using namespace std;

#define maxn 10000000+100
int vis[maxn];
int prime[maxn];

int Prime(int x)
{
    int c = 0;
    for(int i = 2;i <= x; ++i)
    {
        if(vis[i] != 1)
        {
            prime[c++] = i;
            for(int j = i * 2; j <= x; ++j)
            {
                vis[j] = 1;
            }
        }
    }
    return c;
}

int main()
{
    int n,m;
    cin >> n >> m;
    int num = 0;
    memset(vis, 0, sizeof(vis));
    int c = Prime(sqrt(m + 0.5));
    for(int i = n; i <= m; ++i)
    {
        for(int j = 0; j < c; ++j)
        {
            int power = pow(prime[j], 2);
            if(i % power == 0)
            {
                num++;
                break;
            }
        }
    }
    int ans = m - n + 1 - num;
    cout << ans << endl;
    return 0;

}

