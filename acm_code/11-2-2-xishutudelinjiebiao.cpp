#include <iostream>
using namespace std;

#define maxn 1000
int n, m; //points number ; edges number
int first[maxn]; //maxn: points  //first[i] : the first edge number of point i
int next[maxn]; //maxn :edges  // the next edge number of edge i
int u[maxn], v[maxn], w[maxn];

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

void display()
{
    for(int i = 0; i < n; ++i)
    {
        int temp_edge = first[i];
        while(temp_edge != -1)
        {
            cout << u[temp_edge] << "--" << v[temp_edge] << "--" << w[temp_edge] << "--" << temp_edge << endl;
            temp_edge = next[temp_edge];
        }
    }
}

int main()
{
    read();
    display();
    return 0;
}


