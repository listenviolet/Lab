#include <iostream>
using namespace std;

void print_subset(int n, int* A, int cur)
{
    for(int i=0;i<cur;i++) cout<<A[i];
    cout<<endl;
    int s=cur? A[cur-1]+1:0;
    for(int i=s;i<n;i++)
    {
        A[cur]=i;
        print_subset(n,A,cur+1);
    }
}

int main()
{
    int A[5]={0,1,2,3,4};
    print_subset(5,A,0);
    return 0;
}
