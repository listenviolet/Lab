#include <iostream>

using namespace std;
#define maxn 1000

void print_permutation(int n, int* A, int cur)
{
	if (cur == n)
	{
		for (int i = 0; i < n; i++)
		{
			cout << A[i];
		}
		cout << endl;
	}

	else for (int i = 1; i <= n; i++)
	{
		int ok = 1;
		for (int j = 0; j < cur; j++)
		{
			if (A[j] == i) ok = 0;
		}
		if (ok)
		{
			A[cur] = i;
			print_permutation(n, A, cur + 1);
		}
	}
}

int main()
{
	int A[maxn];
	int n;
	cout << "Please input n: " << endl;
	cin >> n;
	for (int i = 1; i <= n; i++)
	{
		A[i]=i;
	}
	print_permutation(n, A, 0);
	system("pause");
	return 0;
}