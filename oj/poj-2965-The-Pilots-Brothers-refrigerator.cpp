#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;

#define matrix 16
#define row 4
int handles[matrix + 1];  //最初输入字符串转换的01-table

void initHandles()
{
    string str;
    int counter = 1;
    while(counter <= matrix)
    {
        cin >> str;
        for(int i = 0; i < row; ++i)
            handles[counter++] = (str[i] == '-') ? 1 : 0;
    }
}

bool isOpened(int *arr, int len)
{
    for(int i = 1; i <= len; ++i)
    {
        if(arr[i] == 0) return false;
    }
    return true;
}

void changeState(int *handles_change, int index)
{
    int x = (index - 1) / row; //前面有几行 不包括所在行
    int y = (index - 1) % row + 1; //在第几列 包括所在列
    for(int j = 1; j <= row; ++j) handles_change[x * row + j] = !handles_change[x * row + j];
    for(int i = 0; i < row; ++i) handles_change[i * row + y] = !handles_change[i * row + y];
    handles_change[index] = !handles_change[index];
}

void display(int num, int *result)
{
    cout << num << endl;
    for(int i = 1; i <= num; ++i)
    {
        int x = result[i] / 4 + 1;
        int y = result[i] % 4;
        cout << x << " " << y << endl;
    }
}

void combine(int *handles_copy, int len, int *result, int num, int start, int counter, int &ans)
{
    if(counter == 0)
    {
        int *handles_change = (int*)malloc(sizeof(int) * (len + 1));
        for(int i = 1; i <= len; ++i)
            handles_change[i] = handles_copy[i];
        for(int i = 1; i <= num; ++i)
        {
            changeState(handles_change, result[i]);
        }
        if(isOpened(handles_change, len) == true)
        {
            ans = num;
        }
        free(handles_change);
    }
    else
    {
        for(int i = start; i <= len - counter + 1; ++i)
        {
            result[num - counter + 1] = i;
            combine(handles_copy, len, result, num, start + 1, counter - 1, ans);
        }
    }
}

void open(int *handles_copy, int len)
{
    int num = 1; // 打开handles 的数量
    for(num = 1; num <= len; ++num)
    {
        int ans = 0;
        int *result = (int*) malloc(sizeof(int) * (num + 1));
        combine(handles_copy, len, result, num, 1, num, ans);
        if(ans == 0) {free(result); continue;}
        else
        {
            display(num, result);
            free(result);
            break;
        }
    }
}

int main()
{
    initHandles();
    int *handles_copy = (int*) malloc(sizeof(int) * (matrix + 1));
    for(int i = 1; i <= matrix; ++i)
        handles_copy[i] = handles[i];
    if(isOpened(handles_copy, matrix) == true) cout << "0" << endl;
    else
    {
        open(handles_copy, matrix);
    }
    return 0;
}
