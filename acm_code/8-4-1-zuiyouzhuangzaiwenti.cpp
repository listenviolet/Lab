#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 1000

int main()
{
    int n,C;
    int w[maxn];
    cout <<"Please input the total number and the total weight:"<<endl;
    cin >> n >> C;
    for(int i = 0;i < n;++i)
    {
        cin >> w[i];
    }
    sort(w,w+n);
    int weight=0;
    for(int i = 0; i < n; ++i)
    {
        weight += w[i];
        if(weight <= C) cout<<w[i]<<" ";
        else break;
    }
    cout<<endl;
    return 0;
}
