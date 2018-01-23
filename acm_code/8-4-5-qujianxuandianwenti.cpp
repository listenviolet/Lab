#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 10000

struct Extent
{
    int a,b;
    bool operator < (const Extent& S)const
    {
        return (b < S.b) || (b == S.b && a > S.a);
    }
}A[maxn + 2];

int main()
{
    int n;
    cout << "Please input the number of extents:" <<endl;
    cin >> n;
    for(int i =0; i < n;++i)
    {
        cin >> A[i].a >> A[i].b;
    }
    sort(A, A + n);
    int end = -1;
    int cnt = 0;

    for(int i = 0; i < n; ++i)
    {
            ++cnt;
            int k = A[i].b;
            cout << "The "<< cnt << " point is "<<k <<"."<<endl;
            while(k >= A[++i].a)
            {

            }
            --i;
    }
    cout<<cnt<<endl;
    return 0;
}
