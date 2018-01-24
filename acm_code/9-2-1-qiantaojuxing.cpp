#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 1000 + 10

typedef struct Rectangle
{
    int length;
    int width;
}Rectangle;

Rectangle rec[maxn];
int d[maxn];
int G[maxn][maxn];
int n;

void createGraph()
{
    memset(G, 0, sizeof(G));
    for(int i =0; i < n; ++i)
    {
        for(int j = 0; j < n; j++)
        {
            if((rec[i].length > rec[j].length && rec[i].width > rec[j].width) || (rec[i].length > rec[j].width && rec[i].width > rec[j].length))
            {
                G[i][j] = 1; //rec[i] contains rec[j]
            }
        }
    }
}

int dp(int i)
{
    int ans = 0;
    for(int j = 0; j < n; ++j)
    {
        if(G[i][j])
        {
            int tmp = dp(j);
            ans = ans > (tmp + 1) ? ans : (tmp +1);
        }
    }
    return ans;
}

void printGragh()
{
    for(int i =0; i < n; ++i)
    {
        for(int j = 0; j < n; ++j)
            cout << G[i][j]<<" ";
        cout<<endl;
    }
}

int main()
{
    int ans = 0;
    cout << "The number of rectangles:" << endl;
    cin >> n;
    for(int i = 0; i < n; ++i)
    {
        cin >> rec[i].length >> rec[i].width;
    }
    createGraph();

    memset(d, 0, sizeof(d));
    for(int i =0; i <n; ++i)
    {
        int tmp = dp(i);
        ans = ans > tmp ? ans : tmp;
    }
    cout << ans <<endl;
    //printGragh();
    return 0;
}




