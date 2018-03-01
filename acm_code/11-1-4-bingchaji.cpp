#include <iostream>
#include <algorithm>
using namespace std;
#define vexCounts 6
#define maxn 40
#define INFINITE 0xFFFFFFFF
#define uint unsigned int
uint num_edge = 0;
uint u[maxn], v[maxn], w[maxn], r[maxn]; //u[], v[]: 边i的两端点; w[] 边i的边长; 边长第i小的边序号保存在r[]中
uint p[vexCounts];   //i的父节点: p[i]
char vertex[] = {'A', 'B', 'C', 'D', 'E', 'F'};

void read()
{
    uint p1, p2, cost;
    while(cin >> p1)
    {
        cin >> p2 >> cost;
        if(p1 > p2)
        {
            u[num_edge] = p1;
            v[num_edge] = p2;
            w[num_edge] = cost;
            num_edge++;
        }
    }
}

bool cmp(const int i, const int j)
{
    return w[i] < w[j] ? true : false;
}

uint find(uint x)
{
    return p[x] == x ? x : p[x] = find(p[x]);
}

int Kruskal()
{
    int ans = 0;
    for(uint i = 0; i < vexCounts; ++i) p[i] = i;
    for(uint i = 0; i < num_edge; ++i) r[i] = i;
    sort(r, r + num_edge, cmp);
    for(uint i = 0; i < num_edge; ++i)
    {
        uint e = r[i];             //边序号
        uint x = find(u[e]);
        uint y = find(v[e]);
        if(x != y)
        {
            cout << vertex[u[e]] << "--" << vertex[v[e]] << endl;
            ans += w[e];
            p[x] = y;
        }
    }
    return ans;
}

int main()
{
    read();
    int ans = Kruskal();
    cout << ans << endl;
    return 0;
}
