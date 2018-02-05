#include <iostream>
using namespace std;

int Hanoi(int n)
{
    if(n == 1) return 1;
    else return 2 * Hanoi(n - 1) + 1;
}

int main()
{
    int n;
    cout << "Please input n: " << endl;
    cin >> n;
    int ans = Hanoi(n);
    cout << ans << endl;
    return 0;
}
