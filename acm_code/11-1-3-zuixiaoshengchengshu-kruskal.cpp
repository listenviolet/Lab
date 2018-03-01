#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define VertexData unsigned int
#define vexCounts 6
#define INFINITE 0xFFFFFFFF

char vertex[] = {'A','B','C', 'D','E','F'};

typedef struct Arc
{
    VertexData u;
    VertexData v;
    VertexData cost;
}Arc;

void AdjMatrix(VertexData adjMat[][vexCounts])
{
    for(int i = 0; i < vexCounts; ++i)
    {
        for(int j = 0; j < vexCounts; ++j)
        {
            adjMat[i][j] = INFINITE;
        }
    }
    VertexData u, v, cost;
    while(cin >> u)
    {
        cin >> v >> cost;
        adjMat[u][v] = cost;
    }
}

void ReadArc(VertexData adjMat[][vexCounts], vector<Arc> &vertexArc)
{
    Arc *temp = NULL;
    for(VertexData i = 0; i < vexCounts; ++i)
    {
        for(VertexData j = 0; j < i; ++j)
        {
            if(adjMat[i][j] != INFINITE)
            {
                temp = new Arc;
                temp -> u = i;
                temp -> v = j;
                temp -> cost = adjMat[i][j];
                vertexArc.push_back(*temp);
            }
        }
    }
}

bool cmp(Arc A, Arc B)
{
    return A.cost < B.cost ? true : false;
}

bool FindTree(VertexData u, VertexData v, vector<vector<VertexData> > &Tree)
{
    VertexData index_u = INFINITE;
    VertexData index_v = INFINITE;
    for(VertexData i = 0; i < Tree.size(); ++i) //find in i tree
    {
        if(find(Tree[i].begin(), Tree[i].end(), u) != Tree[i].end())
            index_u = i;
        if(find(Tree[i].begin(), Tree[i].end(), v) != Tree[i].end())
            index_v = i;
    }

    if(index_u != index_v)
    {
        for(VertexData i = 0; i < Tree[index_v].size(); ++i)
        {
            Tree[index_u].push_back(Tree[index_v][i]);
        }

        Tree[index_v].clear();
        return true;
    }
    return false;
}

void MinSpanTree_Kruskal(VertexData adjMat[][vexCounts])
{
    vector<Arc> vertexArc;
    ReadArc(adjMat, vertexArc);
    sort(vertexArc.begin(), vertexArc.end(), cmp);

    vector<vector<VertexData> > Tree(vexCounts);
    for(VertexData i = 0; i < vexCounts; ++i)
    {
        Tree[i].push_back(i);
    }

    for(VertexData i = 0; i < vertexArc.size(); ++i)
    {
        VertexData u = vertexArc[i].u;
        VertexData v = vertexArc[i].v;
        if(FindTree(u, v, Tree))
        {
            cout << vertex[u] << "---" <<vertex[v] << endl;
        }
    }
}

int main()
{
    VertexData adjMat[vexCounts][vexCounts] = {0};
    AdjMatrix(adjMat);
    MinSpanTree_Kruskal(adjMat);
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
