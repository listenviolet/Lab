#include <iostream>
using namespace std;

#define INF 0x3F3F3F3F
#define maxn 1000

int a[maxn][maxn];
int n, m;

void read()
{
    cout << "Please input n, m:" << endl;
    cin >> n >> m;
    for(int i = 0; i < n; ++i)
        for(int j = 0; j < n; ++j)
            a[i][j] = (i == j) ? 0 : INF;
    int u, v, w;
    for(int i = 0; i < m; ++i)
    {
        cin >> u >> v >> w;
        a[u][v] = w;
    }
}

void floyd()
{
    for(int k = 0; k < n; ++k)
        for(int i = 0; i < n; ++i)
            for(int j = 0; j < n; ++j)
            {
                int tmp = a[i][k] + a[k][j];
                a[i][j] = (a[i][j] < tmp) ? a[i][j] : tmp;
            }
}

void display()
{
    cout << "----result---------" << endl;
    for(int i = 0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
            cout << a[i][j] << " ";
        cout << endl;
    }
}
int main()
{
    read();
    floyd();
    display();
    return 0;
}

/*
4 8
0 1 2
0 2 6
0 3 4
1 2 3
2 0 7
2 3 1
3 0 5
3 2 11
*/
