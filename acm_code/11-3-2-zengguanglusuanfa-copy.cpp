#include <iostream>
#include <cstring>
#include <queue>
using namespace std;

#define maxn 1000
#define INF 0x3F3F3F3F

int cap[maxn][maxn], flow[maxn][maxn];
int a[maxn];
int p[maxn];
queue<int> q;
int f;

int n, m, s, t;

void Init()
{
    memset(cap, 0, sizeof(cap));
    memset(flow, 0, sizeof(flow));

    cout << "Please input n, m, s, t: " << endl;
    cin >> n >> m >> s >> t;

    int u, v, c;
    for(int i = 0; i < m; ++i)
    {
        cin >> u >> v >> c;
        cap[u][v] = c;
    }
}

int EK()
{
    for(;;)
    {
        q.push(s);
        memset(a, 0, sizeof(a));
        a[s] = INF;
        while(!q.empty())
        {
            int u = q.front(); q.pop();
            for(int v = 0; v < n; ++v)
            {
                if(!a[v] && cap[u][v] > flow[u][v])
                {
                    p[v] = u;
                    q.push(v);
                    int tmp = cap[u][v] - flow[u][v];
                    a[v] = (a[u] < tmp) ? a[u] : tmp;
                }
            }
        }

        if(a[t] == 0) break;
        for(int u = t; u != s; u = p[u])
        {
            flow[p[u]][u] += a[t];
            flow[u][p[u]] -= a[t];
        }
        f += a[t];
    }
    return f;
}

int main()
{
    Init();
    int ans = EK();
    cout << "result: " << ans << endl;
    return 0;
}

/*
6 10 0 5
0 1 8
0 2 4
1 3 2
1 4 2
2 1 4
2 3 1
2 4 4
3 4 6
3 5 9
4 5 7
*/
