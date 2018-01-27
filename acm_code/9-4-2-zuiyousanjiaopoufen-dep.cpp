#include <iostream>
using namespace std;

#define maxn 100+2
int tr[maxn];
int n;

int dep(int i, int j)
{
	if((i + 1) % n == j) return 0;
	int ans = 0;
	if(i < j)
	{
		for(int k = (i + 1) % n; k < j; ++k)
		{
			int tmp = dep(i, k) + dep(k,j) + tr[i] + tr[k] + tr[j];
			ans = ans > tmp ? ans : tmp;
		}
	}
	else if(i > j)
	{
		for(int k = (j + 1) % n; k < n + i; ++k)
		{
			int tmp = dep(j, k % n) + dep(k % n, i) + tr[i] + tr[k] + tr[k % n];
			ans = ans > tmp ? ans : tmp;
		}
	}
	return ans;
}

int main()
{
    cout << "Please input n:"<<endl;
    cin >> n;
    cout << "The weight on each point:" <<endl;
    for(int i =0; i < n; i++)
    {
        cin >> tr[i];
    }

    int ans = 0;
    cout << dep(0, n-1)<<endl;
    return 0;

 }
