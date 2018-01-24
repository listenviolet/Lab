#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 100
int A[maxn][maxn];

int main()
{
    int n;
    int d[maxn][maxn];
    memset(A,0,sizeof(A));
    memset(d,0,sizeof(d));
    cout << "Please input n:"<<endl;
    cin >> n;
    for(int i = 1; i <= n; ++i)
    {
        for(int j = 1; j <= i; ++j)
        {
            cin >> A[i][j];
        }
    }
    for(int j = 1; j <= n; j++)
    {
        d[n][j] = A[n][j];
    }

    for(int i = n -1; i >= 1; --i)
    {
        for(int j = 1; j <=i; ++j)
        {
            d[i][j] = A[i][j] + max(d[i + 1][j], d[i + 1][j + 1]);
        }
    }
    cout << d[1][1] << endl;
    return 0;
}
