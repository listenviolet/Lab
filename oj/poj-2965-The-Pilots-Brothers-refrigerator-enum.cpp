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
    handle ^= 0x000F << (i << 2);  // i 时 改第 4-i 行
    handle ^= 0x1111 << j;         // j 时 改第 4-j 列
    handle ^= (0x1 << j) << (i << 2); //4 - i,4 - j 改了两遍 再改回
}

bool find(int n, int&k, int i, int j) // k 记录一共改了几个 n 记录还有几个要改
{
    if(n == 0) return check() && cout << k << endl;
    if(j == 4) ++i, j = 0;        //进到下一行
    for(; i < 4; ++i)
    {
        for(; j < 4; ++j)
        {
            change(i, j);
            if(find(n - 1, k, i, j + 1))  //之后的，从j + 1 处，即下一个位置开始找。
            {
                cout << 4 - i << " " << 4 - j << endl;  //若之后可找到， 则打印当前改变的坐标
                return true;
            }
            change(i, j);             //若之后不能找到，则改回颜色
        }

        j = 0;                        //每找完一行，j 清零找下一行
    }
    return false;                     //不能找到
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
