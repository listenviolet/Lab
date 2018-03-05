#include <iostream>
using namespace std;

#define INF 0x3F3F3F3F
#define maxn 1000

int dist[maxn];
int n,m, s; //points, edges number, source

typedef struct Edge
{
    int u;
    int v;
    int w;
}Edge;

Edge edge[maxn];

void read()
{
    cout << "Please input the points, edges number and source: " << endl;
    cin >> n >> m >> s;

    for(int i = 0; i < n; ++i)
    {
        dist[i] = INF;
    }

    dist[s] = 0;
    for(int i = 0; i < m; ++i)
    {
        cin >> edge[i].u >> edge[i].v >> edge[i].w;
        dist[edge[i].v] = (edge[i].u == s) ? edge[i].w : dist[edge[i].v];
        //if(edge[i].u == s) dist[edge[i].v] = edge[i].w;
    }

    cout << "Init:" << endl;
    for(int i = 0; i < n; ++i)
    {
        cout << dist[i] << " " ;
    }
    cout << endl;
}

void relax(int u, int v, int w)
{
    int tmp = dist[u] + w;
    dist[v] = (dist[v] > tmp) ? tmp : dist[v];
    cout << u << "--" << v << "--" << dist[v] <<endl;
}

bool Bellman_Ford()
{
    for(int i = 0; i < n -1; ++i)
    {
        for(int e = 0; e < m; ++e)
        {
            relax(edge[e].u, edge[e].v, edge[e].w);
        }
    }
    bool flag = 1;
    for(int e = 0; e < m; ++e)
    {
        if(dist[edge[e].v] > dist[edge[e].u] + edge[e].w)
        {
            cout << edge[e].u << "--" << edge[e].v << "--" << dist[edge[e].v] << "--" << edge[e].u + edge[e].w << endl;
            flag = 0; break;
        }
    }
    return flag;
}

int main()
{
    read();
    if(Bellman_Ford())
    {
        for(int i = 0; i < n; ++i)
        {
            if(dist[i] == INF) cout << "INF ";
            else cout << dist[i] << " ";
        }
        cout << endl;
    }

    else cout << "Have negative circle." << endl;
    return 0;
}
/*
non-neg
4 4 0
0 1 1
1 2 2
2 3 -3
3 1 5

neg-cir
4 4 0
0 1 1
1 2 2
2 3 -10
3 1 5
*/
