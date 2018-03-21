#include <iostream>
#include <algorithm>
using namespace std;

typedef long long int64;

int64 getSum(int64 k, int64 n, int64 m)
{
    int64 sum = 0;
    for(int i = 1; i <= n; ++i)
    {
        if(i > k) break;
        sum += (m <= k / i) ? m : k / i;
    }
    return sum;
}

int64 binarySearch(int64 n, int64 m, int64 k, int64 low, int64 high)
{
    while(low < high)
    {
        int64 mid = (low + high) / 2;
        if(getSum(mid, n, m) == k)
        {
            return mid;
        }
        else if(getSum(mid, n, m) < k)
        {
            return binarySearch(n, m, k, mid + 1, high);
        }
        else
        {
            if(getSum(mid - 1, n, m) < k)
                return mid;
            return binarySearch(n, m, k, low, mid - 1);
        }
    }
    return low;
}

int main()
{
    int64 n, m, k;
    while(cin >> n >> m >> k)
    {
        cout << binarySearch(n, m, k, 1, n*m) << endl;
    }
    return 0;
}
