#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
#define maxn 1000

struct Good
{
    int id;
    double w;
    double v;
};

bool cmp(Good a, Good b)
{
    if(a.v / a.w > b.v / b.w)
        return true;
    return false;
}

int main()
{
    struct Good goods[maxn];
    int n;
    double C;
    cout << "Please input n, C"<<endl;
    cin >> n >> C;
    for(int i = 0; i < n; ++i)
    {
        goods[i].id = i;
        cin >> goods[i].w >> goods[i].v;
    }
    sort(goods, goods + n, cmp);
    double leftW = C,totalV = 0;
    for(int i = 0; i < n; ++i)
    {
        if(leftW >= goods[i].w)
        {
            leftW -= goods[i].w;
            totalV += goods[i].v;
            printf("Choose good[id = %d], %.1f weight, make %.1f value.\n",goods[i].id,goods[i].w,goods[i].v);
        }

        else
        {
            totalV += leftW / goods[i].w * goods[i].v;
            printf("Choose good[id= %d], %.1f weight, make %.1f value.\n", goods[i].id, leftW, leftW / goods[i].w * goods[i].v);
            leftW = 0;
            break;
        }
    }

    cout << "Max total value: "<< totalV << endl;
    return 0;
}
