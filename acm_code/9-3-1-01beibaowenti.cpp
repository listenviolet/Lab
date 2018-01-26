#include <iostream>
using namespace std;
#define max_n 100+2
#define max_c 10000+10

struct  Goods
{
    int v;
    int w;
};
struct Goods goods[max_n];
int n;

int d[max_n][max_c];

int main()
{
    int C;
    cout << "Please input n and C:"<<endl;
    cin >> n >> C;
    for(int i = 1; i <= n; ++i)
    {
        cin >> goods[i].v >> goods[i].w;
    }
    for(int i = n; i >=1; --i)
    {
        for(int j = 0; j <= C; ++j)
        {
            d[i][j] = (i == n ? 0 : d[i + 1][j]);
            if(j >= goods[i].v)
            {
                int tmp = d[i + 1][j - goods[i].v] + goods[i].w;
                d[i][j] = d[i + 1][j] > tmp ? d[i + 1][j] : tmp;
                //cout << "d[" <<i <<"+ 1]["<<j<<"]:"<<d[i+1][j] <<endl;
            }
            //cout << "d["<<i<<"]["<<j<<"]: " << d[i][j] << " ";
        }
        //cout <<endl;
    }

    cout << d[1][C] <<endl;

    return 0;
}
