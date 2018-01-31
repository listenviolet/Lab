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
	for(int i = 0; i < n; ++i)
	{
		if(S >= V[i] && d[S] == d[S- V[i]] + 1)
		{
			cout << V[i] << " ";
			print_ans(d, S - V[i]);
			break;
		}
	}
}

int main()
{
    int S;
	cout << "Please input n and S:" <<endl;
	cin >> n >> S;

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
			int tmp_Min = Min[i - V[j]];
			int tmp_Max = Max[i - V[j]];
			Min[i] = Min[i] < tmp_Min + 1 ? Min[i] : tmp_Min + 1;
			Max[i] = Max[i] > tmp_Max + 1 ? Max[i] : tmp_Max + 1;
		}
	}

	cout << "Min: " << Min[S] << ";" <<endl;
	cout << "Max: " << Max[S] << ";" <<endl;
	cout << "Max_dic: ";  print_ans(Max, S); cout << endl;
	cout << "Min_dic: ";  print_ans(Min, S); cout << endl;
	return 0;
}