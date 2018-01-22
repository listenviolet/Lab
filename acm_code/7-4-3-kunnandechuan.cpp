#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define maxn 100

int dfs(int cur,int n,int L,int* S)
{
    if(cur==n)
    {
        for(int i=0;i<n;i++) printf("%c",'A'+S[i]);
        cout<<endl;
        return 0;
    }
    for(int i=0;i<L;i++)
    {
        S[cur]=i;
        int ok=1;
        for(int j=1;j*2<=cur+1;j++)
        {
            int equal=1;
            for(int k=0;k<j;k++)
            {
                if(S[cur-k]!=S[cur-k-j])
                {
                    equal=0;
                    break;
                }
            }
            if(equal) {ok=0; break;}
        }
        if(ok) if(!dfs(cur+1,n,L,S)) return 0;
    }
    return 1;
}

int main()
{
    int n,L,k;
    cout<<"Please input n,L:"<<endl;
    int S[maxn];
    while(scanf("%d %d",&n,&L)!=EOF)
    {
        memset(S,0,sizeof(int)*n);
        k=dfs(0,n,L,S);
    }
    return 0;
}
