#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define max_c 10000+10
#define max_n 100+2

int d[max_c];
int vis[max_c];
int n;

struct Goods
{
    int v;
    int w;
    /*
    bool operator < (const Goods& G)const
    {
        return v < G.v;
    }
    */
};

struct Goods goods[max_n];

int dp(int C)
{
    if(vis[C])
    {
        return d[C];
    }
    vis[C] = 1;

    int& ans = d[C];
    ans = -1 << 30;

    for(int i = 0; i < n; ++i)
    {
        if(C >= goods[i].v)
        {
            int tmp = dp(C - goods[i].v);
            if(ans < tmp + goods[i].w)
                ans = tmp + goods[i].w;
        }
    }
    d[C] = ans;
    return ans;
}

int main()
{
    int C;
    cout << "Please input n and C:" <<endl;
    cin >> n >>C;
    cout << "V & W:" <<endl;
    for(int i = 0; i < n; ++i)
    {
        cin >> goods[i].v >> goods[i].w;
    }

    memset(d, 0, sizeof(d));
    memset(vis, 0, sizeof(vis));

    vis[0] = 1;
    int ans = dp(C);
    cout << ans <<endl;
    return 0;
}
