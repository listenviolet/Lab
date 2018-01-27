#include <iostream>
using namespace std;

#define max_c 10000+10
int f[max_c];

int main()
{
    int n,C;
    cout << "Please input n, C:" <<endl;
    cin >> n >>C;
    int v, w;

    for(int i = 1; i <= n; ++i)
    {
        cin >> v >> w;
        for(int j = C; j >= 0; --j)
        {
            if(j >= v)
            {
                f[j] = f[j] > f[j-v] + w ? f[j] : f[j-v] + w;
            }
        }
    }

    cout << f[n, C] << endl;

    return 0;
}
