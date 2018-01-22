#include <iostream>
#include <cstring>
using namespace std;
int vis[16];
int isp[32];

int is_prime(int n)
{
    if(n==2) return 1;
    else
    {
        for(int i=2;i<=n/2;i++)
        {
            if(n%i==0) return 0;
        }
        //cout<<n<<" ";
        return 1;
    }
}

void dfs(int cur,int n,int* A)
{
    if(cur==n && isp[A[n-1]+A[0]])
    {
        for(int i=0;i<n;i++) cout<<A[i]<<" ";
        cout<<endl;
    }
    else
    {
        for(int i=2;i<=n;i++)
        {
            if(!vis[i] && isp[i+A[cur-1]])
            {
                A[cur]=i;
                vis[i]=1;
                dfs(cur+1,n,A);
                vis[i]=0;
            }
        }
    }
}

int main()
{
    int A[16],n;
    cout<<"Please input n: "<<endl;
    cin>>n;
    memset(A,0,sizeof(int)*n);
    A[0]=1;
    vis[1]=1;
    for(int i=2;i<=n*2;i++) isp[i]=is_prime(i);
    dfs(1,n,A);
    return 0;
}
