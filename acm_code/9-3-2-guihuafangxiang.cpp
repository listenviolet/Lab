#include <iostream>

using namespace std;
#define max_n 100+2
#define max_c 10000+10
int f[max_n][max_c];

int main()
{
    int n,C;
    cout << "Please input n, C:" <<endl;
    cin >> n >>C;
    int v, w;

    for(int i = 1;i <= n;++i)
    {
        cin >> v >> w;
        for(int j = 0; j <= C; ++j)
        {
            f[i][j] = (i == 1 ? 0 : f[i-1][j]);
            if(j >= v) f[i][j] = f[i][j] > f[i-1][j-v] + w ? f[i][j] : f[i-1][j-v] + w;
        }
    }
    cout << f[n][C] <<endl;
    return 0;
}
