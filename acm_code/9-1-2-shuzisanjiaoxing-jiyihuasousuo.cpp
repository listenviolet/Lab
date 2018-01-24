#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 100
int A[maxn][maxn];
int d[maxn][maxn];

int dis(int i, int j, int n)
{
    if(d[i][j] >= 0) return d[i][j];
    return d[i][j] = A[i][j] + (i == n ? 0 : max(dis(i + 1, j, n), dis(i + 1, j + 1, n)));
}

int main()
{
    int n;
    memset(A,0,sizeof(A));
    memset(d,-1,sizeof(d));
    cout << "Please input n:"<<endl;
    cin >> n;
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cin >> A[i][j];
        }
    }
    cout << dis(1,1, n) << endl;
    return 0;
}
