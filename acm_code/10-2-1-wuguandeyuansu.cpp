#include <iostream>
#include <cstring>
using namespace std;

#define maxn 100
int tr[maxn];

int main()
{
    int n, m;
    cout << "Please input n and m:" << endl;
    cin >> n >> m;
    n = n - 1;
    tr[0] = 1;
    for(int i = 1; i <= n; ++i)
        tr[i] = tr[i - 1] * (n - i + 1) / i;
    for(int i = 0; i <= n; ++i)
    {
        //cout << tr[i] << " ";
        if(tr[i] % m == 0) cout << "a" << i + 1 << " ";
    }
    cout << endl;

    return 0;
}
