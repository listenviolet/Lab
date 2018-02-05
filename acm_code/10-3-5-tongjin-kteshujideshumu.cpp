#include <iostream>
using namespace std;

int f[200][500];  //��Ϊ�߾�����bign?

#define F(i, j) (f[(i) + 1][(j) + 1])  //�ú괦��֧�ָ����±�

int main()
{
    int n, k;
    cin >> n >> k;
    /* �߽� */
    for(int i = 0; i <= k; ++i)
    {
        F(-1, i) = F(0, i) = 0;
    }
    F(-1, -1) = F(0, -1) = 1;
    /* ���� */
    for(int i = 1; i <= n; ++i)
    {
        for(int j = -1; j <= k; ++j)
        {
            F(i, j) = F(i - 1, j);
            if(j - i < 0) F(i, j) += F(i - 2, -1);
            else F(i, j) += F(i - 2, j - i);
        }
    }
    cout << F(n, k) << endl;
    return 0;
}
