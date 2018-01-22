#include <iostream>
using namespace std;
#define maxn 100

void quick_sort(int* A, int x,int y)
{
    if(x>=y) return;
    int i,j,k;
    k=A[x];
    i=x;j=y;
    while(i<j)
    {
        while(i<j && A[j]>=k) j--;
        A[i] = A[j];
        while(i<j && A[i]<=k) i++;
        A[j] = A[i];
    }
    A[i] = k;
    quick_sort(A,x,i-1);
    quick_sort(A,i+1,y);
}

int main()
{
    int A[maxn],n;
    cout<<"Please input n:"<<endl;
    cin>>n;
    for(int i=0;i<n;i++)
        cin>>A[i];
    quick_sort(A,0,n-1);
    for(int i=0;i<n;i++)
        cout<<A[i]<<" ";
    cout<<endl;
    return 0;
}
