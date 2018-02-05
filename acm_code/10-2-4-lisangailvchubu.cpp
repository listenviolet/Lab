#include <iostream>
#include <cstdio>
using namespace std;

double birthday(int n, int m)
{
    double ans = 1.0;
    for(int i = 0; i < m; ++i)
    {
        ans = ans * (n - i) / n;  //若写为 ans *= (n-i) / n 则计算得整数不是小数，
        //cout << ans << endl;    //因为先计算的 (n - i) / n 得整数 0 / 1
    }
    return 1 - ans;
}
int main()
{
    int n, m;
    cout << "Please input n and m: " << endl;
    cin >> n >> m;
    double ans = birthday(n, m);
    printf("%.2f%%", ans * 100);
    return 0;
}
