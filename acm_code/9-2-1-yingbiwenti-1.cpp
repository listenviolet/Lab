#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;
#define maxn 100+10
#define INF 0x3f3f3f3f
struct Coin
{
    int v;
    int count;
    bool operator < (const Coin& T)const
    {
        return (v < T.v);
    }
};

struct Coin C[maxn];
int n; //coin types
//int road[1000], m = 1;

int dp(int i)
{
    int ans = i;
    if(i == 0)
    {
        /*
        for(int k = 1; k < m; ++k)
        {
            cout << road[k] << " ";
        }
        cout <<endl;
        */
        for(int k = 0; k < n; ++k)
        {
            cout << C[k].v << " : " << C[k].count << endl;
        }
        cout << "------------------" << endl;
        return 0; //end
    }

    else if(i < C[0].v) return INF; //fails ->set infinite

    for(int j = 0; j < n; ++j)
    {
        int tmp;
        if(C[j].v <= i)
        {
            
            /*road[m] = C[j].v;
            m++;
            */
            C[j].count++;
            tmp = dp(i - C[j].v);
            C[j].count--;
            //ans = ans < (tmp + 1) ? ans : (tmp + 1);
            if(ans > tmp + 1)
            {
                ans = tmp + 1;
            }



        }
        else break;
    }

    return ans;
}

int main()
{
    int S;
    cout << "Please input n and S:" <<endl;
    cin >> n >> S;
    cout << "Please input V" <<endl;
    for(int i = 0; i < n; ++i)
    {
        cin >> C[i].v;
        C[i].count = 0;
    }
    sort(C, C + n);
    cout << dp(S) <<endl;
    return 0;
}
