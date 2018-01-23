#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 10000

struct Extent
{
    int a,b;
    bool operator < (const Extent& S)const
    {
        return b < S.b;
    }
}A[maxn + 2];

int main()
{
    int n;
    cout<<"The number of extents:"<<endl;
    cin >> n;
    for(int i = 0; i < n;i++)
    {
        cin >> A[i].a >> A[i].b;
    }
    sort(A, A + n);
    for(int i =0;i< n;i++)
    {
        cout<<A[i].a<<" "<<A[i].b<<endl;
    }

    int cnt = 0;
    int end = -1;
    for(int i =0; i < n; i++)
    {
        if(end <= A[i].a)
        {
                 end = A[i].b;
                 ++cnt;
        }
    }
    cout<<cnt<<endl;

    return 0;
}
