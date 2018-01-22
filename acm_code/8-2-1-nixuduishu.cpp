#include <iostream>
using namespace std;
#define maxn 100
int cnt=0;
void merge_sort(int *A, int* T, int x,int y)
{
    if(y-x>1)
    {
        //cnt=0;
        int m = x+(y-x)/2;
        merge_sort(A, T, x, m);
        merge_sort(A, T, m, y);

        int p=x, q=m,i=x;
        while(p<m || q<y)
        {
            if(q>=y || (p<m && A[p] <= A[q])) T[i++] = A[p++];
            else
            {
                T[i++] = A[q++];
                cnt+=m-p;
            }

        }
        cout<<"cnt:"<<cnt<<endl;
        for(i=x; i<y;i++) A[i] = T[i];
        for(i=x;i<y;i++) cout<<A[i]<<" ";
        cout<<endl;
    }
}

int main()
{
    int n;
    int A[maxn],T[maxn];
    cout<<"Please input n:"<<endl;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        cin>>A[i];
    }
    merge_sort(A,T,1, n+1);
    for(int i=1;i<=n;i++) cout<<A[i]<<" ";
    cout<<endl;
    cout<<cnt<<endl;
    return 0;
}
