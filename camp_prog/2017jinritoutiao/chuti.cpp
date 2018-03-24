#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 1000000
int d[maxn];


int ques(int* d, int n)
{
    int ans = 0;
    int i = 0;
    while(i + 2 < n)
    {
        if(d[i + 1] - d[i] <= 10 && d[i + 2] - d[i + 1] <= 10)
        {
            i += 3; continue;
        }
        else if(d[i + 1] - d[i] <= 10 && d[i + 2] - d[i + 1] > 10)
        {
            ans++;
            i += 2;
            continue;
        }
        else if(d[i + 1] - d[i] > 10)
        {
            if(d[i + 2] - d[i] <= 20)
            {
                ans++;
                i += 2;
                continue;
            }
            else
            {
                ans += 2;
                i++;
                continue;
            }
        }
    }

    if(i == n - 2)
    {
        if(d[i + 1] - d[i] <= 10) ans++;
        else if(d[i + 1] - d[i] <= 20) ans++;
        else ans += 4;
    }
    if(i == n - 1)
        ans += 2;
    return ans;

}

int main()
{
    int n;
    while(cin >> n)
    {
        for(int i = 0; i < n; ++i)
            cin >> d[i];
        sort(d, d + n);
        int ans = ques(d, n);
        cout << ans << endl;
    }

    return 0;
}
