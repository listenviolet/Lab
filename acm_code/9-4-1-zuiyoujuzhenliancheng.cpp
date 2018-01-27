#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 100+2
#define INF 0x3f3f3f3f
int p[maxn];
int n;
int f(int i,int j)
{
    if(i == j) return 0;
    int k;
    int ans = INF;
    for(int k = i; k < j; ++k)
    {
        int tmp = f(i,k) + f(k+1,j) + p[i]*p[k+1]*p[j+1];
        ans = ans > tmp ? tmp : ans;
    }
    return ans;
}

int main()
{
    cout << "Please input n:" <<endl;
    cin >>n;
    cout <<"P[]:" << endl;
    for(int i = 0; i <= n; ++i)
        cin >> p[i];
    cout << f(0, n-1) <<endl;
    return 0;
}
