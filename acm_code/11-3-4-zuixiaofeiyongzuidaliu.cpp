#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

#define maxn 1000
#define INF 0x3F3F3F3F

queue<int> q;
int d[maxn];    //distance
int p[maxn];    //parent
bool inq[maxn]; // in queue
int flow[maxn][maxn], cap[maxn][maxn], cost[maxn][maxn];
int n, m, s, t;
int c = 0;
int f = 0;

void read()
{
    cout << "Please input n, m, s, t" << endl;
    cin >> n >> m >> s >> t;

    memset(flow, 0, sizeof(flow));
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
            cap[i][j] = (i == j)? INF : 0;
    }
    memset(cost, INF, sizeof(cost));

    int u, v, capacity, C;
    for(int i = 0; i < m; ++i)
    {
        cin >> u >> v >> capacity >> C;
        cap[u][v] = capacity;
        cost[u][v] = C;

        //cout << u << "--" << v << "--" << cap[u][v] << "--" << cost[u][v] << endl;
    }
}

int main()
{
    read();

    for(;;)
    {
        memset(inq, 0, sizeof(inq));
        for(int i = 0; i < n; ++i) d[i] = (i == s) ? 0 : INF;
        q.push(s);
        while(!q.empty())
        {
            int u = q.front(); q.pop();
            inq[u] = false;
            for(int v = 0; v < n; ++v)
            {
                if(cap[u][v] > flow[u][v] && d[v] > d[u] + cost[u][v])
                {
                    //cout << "cap: " << cap[u][v] << "--" << "cost: " << cost[u][v] << "-- ";
                    d[v] = d[u] + cost[u][v];  //cout << u << "--" << v << "--"<< "d[v]: " << d[v] << endl;
                    p[v] = u;
                    if(!inq[v])
                    {
                        q.push(v);
                        inq[v] = true;
                    }
                }
            }
        }

        if(d[t] == INF) break;

        int a = INF;
        for(int u = t; u != s; u = p[u])
        {
            int tmp = cap[p[u]][u] - flow[p[u]][u];
            a = (a < tmp) ? a :tmp;
        }
        for(int u = t; u != s; u = p[u])
        {
            flow[p[u]][u] += a;
            flow[u][p[u]] -= a;
        }

        c += d[t] * a;  //cout << "c: " << c << endl;
        f += a;         //cout << "f: " << f << endl;
    }
    cout << "Total cost: " << c << endl;
    cout << "Max_Pool: " << f << endl;

    return 0;
}

/*
4 5 0 3
0 1 2 2
0 2 1 5
1 2 1 2
1 3 1 3
2 3 1 1
*/
