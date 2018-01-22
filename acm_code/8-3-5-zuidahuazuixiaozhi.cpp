#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <queue>
#include <vector>
#define f(i,a,b) for(i = a;i<=b;i++)
#define fi(i,a,b) for(i = a;i>=b;i--)

using namespace std;
#define SIZE 100000
typedef long long ll;

ll a[SIZE+10];
int n,m;

int Cnt(ll M){
    int sum = 0,cnt = 1;
    int i;
    f(i,1,n){
        sum+=a[i];
        if(sum>M){
            cnt++;
            sum = a[i];
        }
    }
    return cnt;
}

int main()
{
    while(~scanf("%d%d",&n,&m)){
        int i;
        ll sum = 0,Max = -0x3f3f3f3f;
        f(i,1,n){
            scanf("%lld",a+i);
            sum+=a[i];
            if(a[i]>Max) Max = a[i];
        }

        ll L = Max,R = sum,M;
        while(L<=R){
            M = (L+R)/2;
            int k = Cnt(M);
            if(k<=m){
                R = M-1;
            }else
                L = M+1;
        }
        printf("%lld\n",M);
    }
    return 0;
}
