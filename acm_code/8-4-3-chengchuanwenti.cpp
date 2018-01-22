#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
#define maxn 1000

struct Person
{
    int id;
    double w;
};

bool cmp(Person p1,Person p2)
{
    if(p1.w < p2.w) return true;
    return false;
}

int main()
{
    int n;
    double C;
    struct Person person[maxn];
    cout << "Please input n and C:"<<endl;
    cin >> n >> C;
    for(int i = 0;i < n; i++)
    {
        person[i].id = i;
        cin >> person[i].w;
    }
    sort(person, person + n, cmp);
    int light = 0,heavy = n - 1,num = 0;
    while(light <= heavy)
    {
        if(light == heavy)
        {
            ++num;
            printf("Person id = %d takes the ship.\n", person[light].id);
            break;
        }
        if(person[light].w + person[heavy].w > C)
        {
            ++num;
            printf("Person id = %d takes the ship.\n", person[heavy].id);
            heavy--;
        }
        else
        {
            ++num;
            printf("Person id = %d and %d take the ship.\n", person[light].id,person[heavy].id);
            ++light;
            --heavy;
        }
    }
    cout<<"The total number of ships: "<<num<<endl;
    return 0;
}
