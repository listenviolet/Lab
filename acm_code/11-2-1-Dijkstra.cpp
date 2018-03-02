#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 1000
#define INFINITE 0x3F3F3F3F
int n, m; //n : points number ; m : edges number
int G[maxn][maxn];
int dist[maxn];
int vis[maxn]= {0};
void read()
{
    cout << "Please input the number o points and edges: " << endl;
    cin >> n >> m;
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
        {
            if(i == j) G[i][j] = 0;
            else G[i][j] = INFINITE;
        }
    }
    int u, v, cost;
    int i = 0;
    cout << "Please input the u, v, cost: " << endl;
    while(i++ < m)
    {
        cin >> u >> v >> cost;
        G[u][v] = cost;
    }
}

void dijkstra(int s)
{
    for(int i = 0; i < n; ++i)
    {
        dist[i] = G[s][i];
    }
    vis[s] = 1;

    for(int i = 0; i < n; ++i)
    {
        // find the shortest point k
        int min = INFINITE, k = s;
        for(int i = 0; i < n; ++i)
        {
            if(!vis[i] && dist[i] < min)
            {
                min = dist[i];
                k = i;
            }
        }
        vis[k] = 1;  // add k to T
        for(int i = 0; i < n; ++i)
        {
            if(!vis[i])
            {
                int temp = dist[k] + G[k][i]; // s->k + k->i
                dist[i] = temp < dist[i] ? temp : dist[i]; //(s->k + k->i) <  (s->i) ?
            }
        }
    }
}

void display()
{
    cout << dist[0];
    for(int i = 1; i < n; ++i)
    {
        if(dist[i] == INFINITE) cout << " INFINITE";
        else cout << " " << dist[i];
    }

    cout << endl;
}
int main()
{
    read();
    cout << "Please input the source: " << endl;
    int s;
    cin >> s;
    dijkstra(s);
    display();
    return 0;
}

/*
6 8
0 2 10
0 4 30
0 5 100
1 2 5
2 3 50
3 5 10
4 3 20
4 5 60
*/

