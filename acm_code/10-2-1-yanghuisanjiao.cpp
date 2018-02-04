#include <iostream>
#include <cstring>
using namespace std;

#define maxn 100

int tr[maxn][maxn];
int tr_2[maxn];

int main()
{
    memset(tr, 0, sizeof(tr));
    int n;
    cout << "Please input n:" << endl;
    cin >> n;
    for(int i = 0; i <= n; ++i)
    {
        tr[i][0] = 1;
        for(int j = 1; j <= i; ++j)
            tr[i][j] = tr[i - 1][j - 1] + tr[i - 1][j];
    }
    for(int i = 0; i <= n; ++i)
    {
        for(int j = 0; j < n; ++j)
            cout << tr[i][j] << " " ;
        cout << endl;
    }

    cout << "Way 2: " << endl;
    tr_2[0] = 1;
    for(int i = 1; i <= n; ++i)
        tr_2[i] = tr_2[i - 1] * (n - i + 1) / i;
    for(int i = 0; i <= n; ++i)
        cout << tr_2[i] << " ";
    cout << endl;
    return 0;
}
