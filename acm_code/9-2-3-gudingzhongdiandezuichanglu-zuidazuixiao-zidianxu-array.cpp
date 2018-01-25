#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

#define Maxn 100+10
#define INF 0x3f3f3f3f

int Max[Maxn],Min[Maxn];
int V[Maxn];
int n;

void print_ans(int* d,int S)
{
	while(S)
	{
		cout << V[d[S]] << " ";
		S -= V[d[S]];
	}
}

int main()
{
    int S;
	cout << "Please input n and S:" <<endl;
	cin >> n >> S;

	int min_coin[S];
	int max_coin[S];

	for(int i = 0; i < n; i++)
	{
		cin >> V[i];
	}

	sort(V, V + n);

	Max[0] = Min[0] = 0;
	for(int i = 1; i <= S; ++i)
	{
		Min[i] = INF;
		Max[i] = -INF;
	}

	for(int i = 1; i <= S; ++i)
	{
		for(int j = 0; j < n; ++j)
		{
			if(i >= V[j])
			{
				if(Min[i] > Min[i - V[j]] + 1)
				{
					Min[i] = Min[i-V[j]] + 1;
					min_coin[i] = j;
				}
				if(Max[i] < Max[i - V[j]] + 1)
				{
					Max[i] = Max[i - V[j]] + 1;
					max_coin[i] = j;
				}
			}
		}
	}

	cout << "Min: " << Min[S] << ";" <<endl;
	cout << "Max: " << Max[S] << ";" <<endl;
	cout << "Max_dic: ";  print_ans(max_coin, S); cout << endl;
	cout << "Min_dic: ";  print_ans(min_coin, S); cout << endl;
	return 0;
}
