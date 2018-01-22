#include <iostream>
using namespace std;

int main()
{
    int A[100],n;
    cout<<"Please input n: "<<endl;
    cin>>n;
    for(int i = 1; i<=n;i++)
    {
        cin>>A[i];
    }
    int tot=0;
    int best;
    best = A[1];
    for(int i=1;i<=n;i++)
    {
        for(int j=i+1;j<=n;j++)
        {
            int sum = 0;
            for(int k=i;k<=j;k++)
            {
                sum+=A[k];
                tot++;
            }

            if(sum > best) best = sum;
        }

    }
    cout<<"Best: "<<best<<endl;
    return 0;
}
