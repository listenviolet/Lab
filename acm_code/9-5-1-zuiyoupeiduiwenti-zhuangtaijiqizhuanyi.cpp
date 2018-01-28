#include <cstdio>
#include <cstring>
#include <cmath>
const int nMax=21;
const double INF=1e10;
int n;
struct Node
{
    int x,y,z;
}node[nMax];
double d[nMax][1<<nMax];
void init()
{
    scanf("%d",&n);
    for(int i=0;i<n;i++)
        scanf("%d %d %d",&node[i].x,&node[i].y,&node[i].z);
}
double min(double a,double b)
{
    return a<b?a:b;
}
double dis(Node &a,Node &b)
{
    return sqrt((double)(a.x-b.x)*(a.x-b.x)+(a.y-b.y)*(a.y-b.y)+(a.z-b.z)*(a.z-b.z));
}
void solve()
{
    for(int i=0;i<n;i++)
    {
        for(int s=0;s<(1<<(i+1));s++)
        {
            if(s==0) d[i][s]=0;
            else d[i][s]=INF;
            if((s & (1<<i)))
            {
                for(int j=i-1;j>=0;j--)
                if((s & (1<<j)))
                    d[i][s]=min(d[i][s],dis(node[i],node[j])+d[i-1][s^(1<<i)^(1<<j)]);
            }
            else if(i!=0)
            {
                d[i][s]=d[i-1][s];
            }
        }
    }
}
int main()
{
    //freopen("f://data.in","r",stdin);
    init();
    solve();
    printf("%.3lf\n",d[n-1][(1<<n)-1]);
    return 0;
}

/* Test data
4
0 0 0
0 0 1
0 1 0
1 0 0
*/
