#include <iostream>
using namespace std;

#define maxn 10000
int X[maxn];

int gcd(int a, int b)
{
    return b == 0 ? a : gcd(b, a % b);
}

int judge(int* x, int k)
{
    x[2] /= gcd(x[2],x[1]);
    for(int i = 3; i <= k; ++i) x[2] /= gcd(x[i], x[2]);
    return x[2] == 1;
}

int main()
{
    int k;
    cin >> k;
    for(int i = 1; i <= k; ++i)
    {
        cin >> X[i];
    }

    if(judge(X, k) == true) cout << "YES" <<endl;
    else cout << "NO" <<endl;
    return 0;
}
