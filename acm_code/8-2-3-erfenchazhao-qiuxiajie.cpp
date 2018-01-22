#include <iostream>
using namespace std;
#define maxn 100

int lower_bound(int* A, int x, int y, int v)
{
    int m;
    while(x<y)
    {
        m = x + (y-x)/2;
        if(A[m]>=v) y = m;
        else x=m+1;
    }

    return x;
}

int main()
{
    int A[maxn],n;
    cout<<"Please input n:"<<endl;
    cin>>n;
    for(int i=1;i<=n;i++)
        cin>>A[i];

    cout<<"Please input key value:"<<endl;
    int key;
    cin>>key;
    int k;
    k=lower_bound(A,1,n+1,key);
    cout<<k<<endl;
    return 0;
}
