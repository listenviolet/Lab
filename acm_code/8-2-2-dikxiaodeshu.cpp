#include <iostream>
using namespace std;
#define maxn 100

void find_min_k(int* A, int x,int y,int k)
{
    if(x>=y) return;
    int i,j,key;
    key=A[x];
    i=x;j=y;
    while(i<j)
    {
        while(i<j && A[j]>=key) j--;
        A[i] = A[j];
        while(i<j && A[i]<=key) i++;
        A[j] = A[i];
    }
    A[i] = key;
    if((i-x+1)==k)
    {
        cout<<A[i]<<endl;
        return;
    }
    else if((i-x+1)>k) find_min_k(A,x,i-1,k);
    else if((i-x+1)<k) find_min_k(A,i+1,y,k-i-1+x);
}

int main()
{
    int A[maxn],n,k;
    cout<<"Please input n:"<<endl;
    cin>>n;
    cout<<"Please input k:"<<endl;
    cin>>k;
    for(int i=0;i<n;i++)
        cin>>A[i];
    find_min_k(A,0,n-1,k);

    for(int i=0;i<n;i++)
        cout<<A[i]<<" ";
    cout<<endl;

    return 0;
}
