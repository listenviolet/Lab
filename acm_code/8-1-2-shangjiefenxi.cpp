#include <iostream>
using namespace std;
#define maxn 100
int main()
{
    int A[maxn],n;
    cout<<"Please input n: "<<endl;
    cin>>n;
    for(int i = 1;i<=n;i++)
    {
        cin>>A[i];
    }

    int S[maxn];
    S[0] = 0;
    for(int i = 1;i<=n;i++) S[i] = S[i-1] +A[i];
    int best=S[1];
    for(int i=1;i<=n;i++)
    {
        for(int j=i;j<=n;j++)
        {
            //if(best < (S[j] - S[i-1])) best = S[j] - S[i-1];
            best =(best < (S[j] - S[i-1])) ? (S[j] - S[i-1]) : best;
        }
    }
    cout<<"Best: "<<best<<endl;
    return 0;
}
