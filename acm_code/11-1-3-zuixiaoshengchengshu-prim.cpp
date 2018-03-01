#include <iostream>
using namespace std;

#define INFINITE 0xFFFFFFFF
#define vexCounts 6
#define VertexData unsigned int
char vertex[] = {'A', 'B', 'C', 'D', 'E', 'F'};

struct node
{
	VertexData data;
	VertexData lowestcost;
}lowestedge[vexCounts];

void AdjMat(VertexData adjMat[][vexCounts])
{
	for(int i = 0; i < vexCounts; ++i)
	{
		for(int j = 0; j < vexCounts; ++j)
		{
			adjMat[i][j] = INFINITE;
		}
	}

	VertexData u, v;
	VertexData cost;
	while(cin >> u)
	{
		cin >> v >> cost;
		adjMat[u][v] = cost;
	}
}

int Minmum(struct node * lowestedge)
{
	VertexData min = INFINITE;
	int index = -1;
	for(int i = 0; i < vexCounts; ++i)
	{
		if(lowestedge[i].lowestcost < min && lowestedge[i].lowestcost != 0)
		{
			min = lowestedge[i].lowestcost;
			index = i;
		}
	}
	return index;
}

void MinSpanTree_Prim(VertexData adjMat[][vexCounts], VertexData s)
{
	lowestedge[s]. data = s;
	lowestedge[s].lowestcost = 0;

	for(int i = 0; i < vexCounts; ++i)
	{
		if(i != s)
		{
			lowestedge[i].data = s;
			lowestedge[i].lowestcost = adjMat[s][i];
		}
	}

	for(int e = 1; e <= vexCounts - 1; ++e)
	{
		int k = Minmum(lowestedge);
		cout << vertex[lowestedge[k].data] << "--" << vertex[k] << endl;

		lowestedge[k].lowestcost = 0;
		for(int i = 0; i < vexCounts; ++i)
		{
			if(adjMat[k][i] < lowestedge[i].lowestcost)
			{
				lowestedge[i].data = k;
				lowestedge[i].lowestcost = adjMat[k][i];
			}
		}
	}
}

int main()
{
	VertexData adjMat[vexCounts][vexCounts] = {0};
	AdjMat(adjMat);
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
