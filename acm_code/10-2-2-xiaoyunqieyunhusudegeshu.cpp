#include <iostream>
#include <cmath>
using namespace std;

#define maxn 100

int euler_phi(int n)
{
    int m = (int)sqrt(n + 0.5);
    int ans = n;
    for(int i = 2; i <= m; ++i)
    {
        if(n % i == 0)
        {
            ans = ans /i * (i - 1);
            while(n % i == 0) n /= i;
        }
    }
    if(n > 1) ans = ans / n * (n - 1);
    return ans;
}

void phi_table(int n, int* phi)
{
    for(int i = 2; i <= n; ++i) phi[i] = 0;
    phi[1] = 1;
    for(int i = 2; i <= n; ++i)
    {
        if(!phi[i])
        {
            for(int j = i; j <= n; j += i) //j 为 i 的倍数，i 为 j 的因数
            {
                if(!phi[j]) phi[j] = j;
                phi[j] = phi[j] / i * (i - 1);
            }
        }
    }
}

int main()
{
    int n;
    int phi[maxn];
    cout << "Please input n:" << endl;
    cin >> n;
    int ans = euler_phi(n);
    cout << ans << endl;
    phi_table(n, phi);
    cout << "Table: " << endl;
    for(int i = 1; i <= n; ++i)
    {
        cout << phi[i] << " ";
    }
    cout << endl;
    return 0;
}
