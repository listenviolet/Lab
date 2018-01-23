#include <iostream>
#include <algorithm>
using namespace std;

#define maxn 10000

struct Extent
{
    int a,b;
    bool operator < (const Extent& S)const
    {
        return (b < S.a);
    }
}A[maxn + 2];

int main()
{
    int n;
    cout << "Please input the number of extents:" <<endl;
    cin >> n;
    cout<<"The extents:"<<endl;
    for(int i =0; i < n;++i)
    {
        cin >> A[i].a >> A[i].b;
    }
    sort(A, A + n);
    cout<<"Please input s and t:"<<endl;
    int s,t;
    cin >> s >> t;
    if(A[0].a > s || A[n-1].b < t)
    {
        cout << "No answer."<<endl;
        return 0;
    }

    int start = s;
    for(int i = 0; i < n, start <= t; ++i)
    {
        int k,end = start;
        while(start >= A[i].a && start <= A[i].b)
        {
            if(end < A[i].b)
            {
                end = A[i].b;
                k = i;
            }
            ++i;
        }
        cout<<"Choose: " << A[k].a<<" "<<A[k].b<<endl;
        --i;
        start = end + 1;
    }
    return 0;
}




