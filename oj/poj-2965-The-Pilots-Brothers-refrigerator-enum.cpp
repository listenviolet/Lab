#include <iostream>
#include <cstdio>
using namespace std;

int handle;

void read()
{
    for(int i = 0; i < 4; ++i)
    {
        for(int j = 0; j < 4; ++j)
        {
            handle <<= 1;
            if(getchar() == '-')
                handle |= 1;
        }
        getchar();
    }
}

bool check()
{
    return handle == 0xFFFF;
}

void change(int i, int j)
{
    handle ^= 0x000F << (i << 2);  // i ʱ �ĵ� 4-i ��
    handle ^= 0x1111 << j;         // j ʱ �ĵ� 4-j ��
    handle ^= (0x1 << j) << (i << 2); //4 - i,4 - j �������� �ٸĻ�
}

bool find(int n, int&k, int i, int j) // k ��¼һ�����˼��� n ��¼���м���Ҫ��
{
    if(n == 0) return check() && cout << k << endl;
    if(j == 4) ++i, j = 0;        //������һ��
    for(; i < 4; ++i)
    {
        for(; j < 4; ++j)
        {
            change(i, j);
            if(find(n - 1, k, i, j + 1))  //֮��ģ���j + 1 ��������һ��λ�ÿ�ʼ�ҡ�
            {
                cout << 4 - i << " " << 4 - j << endl;  //��֮����ҵ��� ���ӡ��ǰ�ı������
                return true;
            }
            change(i, j);             //��֮�����ҵ�����Ļ���ɫ
        }

        j = 0;                        //ÿ����һ�У�j ��������һ��
    }
    return false;                     //�����ҵ�
}

void work()
{
    for(int i = 0; i <= 16; ++i)
    {
        if(find(i, i, 0, 0))
            return;
    }
}

int main()
{
    read();
    work();
    return 0;
}
