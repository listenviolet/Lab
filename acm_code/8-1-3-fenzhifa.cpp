#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
#define maxn 100

int maxsum(int* A,int x,int y)
{
    if(y-x==1) return A[x];
    int m = x+(y-x)/2;
    int max = maxsum(A,x,m) > maxsum(A,m,y) ? maxsum(A,x,m): maxsum(A,m,y);

    int v = 0;
    int L = A[m-1];
    for(int i = m-1;i>=x;i--)
    {
        v+=A[i];
        L=L>v?L:v;
    }

    v=0;
    int R=A[m];
    for(int i=m;i<y;i++)
    {
        v+=A[i];
        R = R > v? R : v;
    }

    return max = max > (L+R)? max:(L+R);
}

int main()
{
    int A[maxn];
    int n;
    cout<<"Please input n:"<<endl;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>A[i];
    }
    int best = maxsum(A,1,n+1);
    cout<<best<<endl;
    return 0;
}
