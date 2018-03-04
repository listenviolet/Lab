#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define maxn 1000
#define INF 0x3F3F3F3F

int n, m; //points number ; edges number
int first[maxn]; //maxn: points  //first[i] : the first edge number of point i
int next[maxn]; //maxn :edges  // the next edge number of edge i
int u[maxn], v[maxn], w[maxn];

typedef pair<int, int> pii;

priority_queue<pii, vector<pii>, greater<pii> > q;

int d[maxn];

void read()
{
    cin >> n >> m;
    for(int i = 0; i < n; ++i) first[i] = -1;
    for(int e = 0; e < m; ++e)
    {
        cin >> u[e] >> v[e] >> w[e];
        next[e] = first[u[e]];
        first[u[e]] = e;
    }
}

void Dijkstra()
{
    for(int i = 0; i < n; ++i)
    {
        d[i] = (i == 0) ? 0 : INF;
    }
    q.push(make_pair(d[0], 0));

    while(!q.empty())
    {
        pii u = q.top();
        q.pop();
        int x = u.second;              //get the No in pair: (dis, No)
        if(u.first != d[x]) continue;  //replace: if(done[x]) continue; done[x] = true;
        for(int e = first[x]; e != -1; e = next[e])
        {
            int temp = d[x] + w[e];
            if(d[v[e]] > temp)
            {
                d[v[e]] = temp;
                q.push(make_pair(d[v[e]], v[e]));
            }
        }
    }
}

void display()
{
    cout << d[0];
    for(int i = 1; i < n; ++i)
    {
        if(d[i] == INF) cout << " INF";
        else cout << " " << d[i];
    }
    cout << endl;
}

int main()
{
    read();
    Dijkstra();
    display();
    return 0;
}




