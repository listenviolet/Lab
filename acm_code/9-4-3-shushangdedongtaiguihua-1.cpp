#include <iostream>
#include <vector>
#include <algorithm>
#include <cstring>
using namespace std;
#define maxn 1000 + 5

int parent[maxn];       //i's parent 
int hight[maxn];        //i's hight
int max_hight;          //hight of the whole tree
int d[maxn];            //maximum independent set
int gs[maxn];           //i's grandsons' independent set
int s[maxn];            //i's sons' independent set
int n;                  //nodes number
vector<int > G[maxn];   //graph table

void readTree()
{
	cin >> n;
	//input n-1 edges
	for(int i = 0; i < n - 1; ++i)
	{
		int u, v;
		cin >> u >> v;
		G[u].push_back(v);
		G[v].push_back(u);
	}
}

void dfs(int u, int father)
{
	//update the hight of the node and the height of the tree
	hight[u] = (father == -1) ? 0 : hight[father] + 1; 
	max_hight = max_hight > hight[u] ? max_hight : hight[u];

	//update the tree table -- delete the parent node in chain
	int d = G[u].size();
	for(int i = 0; i < d; ++i)
	{
		int v = G[u][i];
		if(v != father)
			dfs(v, parent[v] = u);
	}
}

int RootDP(int root)
{
	parent[root] = -1;
	max_hight = -1;
	dfs(root, -1);

	for(int i = max_hight; i >= 0; --i)
	{
		for(int j = 0; j < n; ++j)
		{
			if(hight[j] == i)
			{
				d[j] = max(gs[j] + 1, s[j]);
				if(i >= 1) s[parent[j]] += d[j];
				if(i >= 2) gs[parent[parent[j]]] += d[j];
			}
		}
	}

	return d[root];
}

int Solve()
{
	int ans = 0;
	for(int i = 0; i < n; ++i)
	{
		memset(gs, 0, sizeof(gs));
		memset(s, 0, sizeof(s));
		int tmp = RootDP(i);
		ans = ans > tmp ? ans : tmp;
	}

	return ans;
}

int main()
{
	readTree();
	int ans = Solve();
	cout << ans << endl;
	return 0;
}



