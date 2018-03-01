#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

#define VertexData unsigned int
#define INFINITE 0xFFFFFFFF
#define vexCounts 6

char vertex[] = {'A','B','C','D','E','F'};

struct node
{
    VertexData data;
    unsigned int lowestcost;
}closeedge[vexCounts];

void AdjMatrix(unsigned int adjMat[][vexCounts])
{
    for(int i = 0; i < vexCounts; ++i)
    {
        for(int j = 0; j < vexCounts; ++j)
        {
            adjMat[i][j] = INFINITE;
        }
    }
    VertexData u, v; unsigned int cost;
    while(scanf("%d",&u) != EOF)
    {
        cin >> v >>cost;
        adjMat[u][v] = cost;
    }
}

int Minmum(struct node * closeedge)
{
    unsigned int min = INFINITE;
    int index = -1;
    for(int i = 0; i < vexCounts; ++i)
    {
        if(closeedge[i].lowestcost < min && closeedge[i].lowestcost != 0)
        {
            min = closeedge[i].lowestcost;
            index = i;
        }
    }
    return index;
}

/* Prim */
void MinSpanTree_Prim(unsigned int adjMat[][vexCounts], VertexData s)
{
    for(int i = 0; i <vexCounts; ++i)
    {
        closeedge[i].lowestcost = INFINITE;
    }
    closeedge[s].data = s;
    closeedge[s].lowestcost = 0;

    for(int i = 0; i < vexCounts; ++i)
    {
        if(i != s)
        {
            closeedge[i].data = s;
            closeedge[i].lowestcost = adjMat[s][i];
        }
    }

    for(int e = 1; e <= vexCounts - 1; ++e)
    {
        int k = Minmum(closeedge);
        cout << vertex[closeedge[k].data] << "--" << vertex[k] << endl;
        closeedge[k].lowestcost = 0;
        for(int i = 0; i < vexCounts; ++i)
        {
            if(adjMat[k][i] < closeedge[i].lowestcost)
            {
                closeedge[i].data = k;
                closeedge[i].lowestcost = adjMat[k][i];
            }
        }
    }
}

int main()
{
    unsigned int adjMat[vexCounts][vexCounts] = {0};
    AdjMatrix(adjMat);
    MinSpanTree_Prim(adjMat, 0);
    return 0;
}

/*
0 1 6
0 2 1
0 3 5
1 0 6
1 2 5
1 4 3
2 0 1
2 1 5
2 3 5
2 4 6
2 5 4
3 0 5
3 2 5
3 5 2
4 1 3
4 2 6
4 5 6
5 2 4
5 3 2
5 4 6
*/
