#include <iostream>
using namespace std;
#define maxn 100

int b_search(int*A,int x, int y,int key)
{
    int m;
    while(x<y)
    {
        m = x + (y-x)/2;
        if(A[m]==key) return m+1;
        else if(A[m]>key) y=m;
        else x = m+1;
    }

    return -1;
}

int main()
{
    int A[maxn],n;
    cout<<"Please input n:"<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>A[i];

    cout<<"Please input key value:"<<endl;
    int key;
    cin>>key;
    int k;
    k=b_search(A,0,n,key);
    cout<<k<<endl;
    return 0;
}
