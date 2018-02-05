#include <iostream>
#include <vector>
using namespace std;

#define maxn 100

vector<int> G[maxn];
int p[maxn];  //p[i] = j : node i's parent is j
int n;   //n : node number; edges : n - 1

void read()
{
    int u, v;
    cout << "Node number: " << endl;
    cin >> n;
    cout << "Please input the non-root tree:" << endl;
    for(int i = 0; i < n - 1; ++i)
    {
        cin >> u >> v;
        G[u].push_back(v);
        G[v].push_back(u);
    }
}

void dfs(int u, int fa) //u is the root of subtree; fa is u's parent node
{
    int len = G[u].size();
    for(int i = 0; i < len; ++i)
    {
        int v = G[u][i];
        if(v != fa) dfs(v, p[v] = u);
    }
}

int main()
{
    read();
    int root;
    cout << "Please input root:" << endl;
    cin >> root;
    p[root] = -1;
    dfs(root, -1);
    for(int i = 1; i < n; ++i)
    {
        cout << p[i] << "->" << i << endl;
    }
    return 0;
}
