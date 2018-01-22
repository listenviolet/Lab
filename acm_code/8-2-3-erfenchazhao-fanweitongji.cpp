#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

int v[1000];

int main()
{
    int n,m;
    int a,b;
    cout<<"Please input the number of integers n and the number of queries m:"<<endl;
    cin>>n>>m;
    for(int i=0;i<n;i++)
         cin>>v[i];

    sort(v,v+n);
    for(int i=0; i<m;i++)
    {
        cout<<"Please input a b:"<<endl;
        cin>>a>>b;
        cout<<upper_bound(v,v+n,b) - lower_bound(v,v+n,a)<<endl;
    }
    return 0;
}
