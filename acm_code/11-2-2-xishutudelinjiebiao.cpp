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

    cout << "------The better code: ---------------" << endl;

    for(int i = 0 ; i < n; ++i)
    {
        for(int e = first[i]; e != -1; e = next[e])
        {
            cout << u[e] << "--" << v[e] << "--" << w[e] << "--" << e << endl;
        }
    }
}

int main()
{
    read();
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

