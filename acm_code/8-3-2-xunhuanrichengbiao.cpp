#include <iostream>
using namespace std;
#define maxn 10000
int A[maxn][maxn];

void block(int size, int tr, int tc)
{
    cout<<"tr: "<<tr<<" tc: "<<tc<<endl;
	if(size == 2) return;
	int s = size / 2;
	//left top
	block(s, tr, tc);

	//left bottom
	for(int i = 0; i < s; i++)
	{
		for(int j = 0; j < s; j++)
		{
			A[tr + s + i][tc + j] = A[tr + i][tc + j] + s;
		}
	}
	block(s, tr + s, tc);
	//right top
	for(int i = 0; i < s; i++)
	{
		for(int j = 0; j < s; j++)
		{
			A[tr + i][tc + s + j] = A[tr + i][tc + j] + s;
		}
	}
	block(s, tr, tc + s);
	//right bottom
	for(int i = 0; i < s; i++)
	{
		for(int j = 0; j < s; j++)
		{
			A[tr + s + i][tc + s + j] = A[tr + i][tc + j];
		}
	}
	block(s, tr + s, tc + s);
}

int main()
{
    A[0][0] = 1;
    A[0][1] = 2;
    A[1][0] = 2;
    A[1][1] = 1;
	int size;
	cout << "Please input size:"<<endl;
	cin >> size;
	block(size, 0, 0);
	for(int i = 0; i < size; i++)
	{
		for(int j = 0; j < size; j++)
			cout << A[i][j]<<" ";
		cout<<endl;
	}
	return 0;
}
