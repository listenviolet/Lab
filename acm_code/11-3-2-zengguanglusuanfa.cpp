#include <iostream>
#include <cstring>
#include <queue>
using namespace std;
#define maxn 1000
#define INF 0x3F3F3F3F

queue<int> q;
int cap[maxn][maxn], flow[maxn][maxn], a[maxn], p[maxn];
int f;
int n, m, s,t;

void Init()
{
    memset(flow, 0, sizeof(flow));          //Init flow
    f = 0;                                  //Init f
    memset(a, 0, sizeof(a));  //Init a

    cout << "Please input n, m, s, t:" << endl;
    cin >> n >> m >> s >> t;
    a[s] = INF;

    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
            cap[i][j] = (i == j) ? INF : 0;  //capacity - default 0

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
        memset(a, 0, sizeof(a));
        a[s] = INF;
        q.push(s);

        while(!q.empty())
        {
            int u = q.front(); q.pop();
            for(int v = 0; v < n; ++v)
            {
                if(!a[v] && cap[u][v] > flow[u][v])
                {
                    p[v] = u; q.push(v);
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
7 8
0 6
0 1 3
0 2 1
1 3 3
2 3 5
2 4 4
3 6 2
4 5 2
5 6 3
*/
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
