#include <iostream>
#include <cstring>
#include <cstdlib>
using namespace std;
#define cbNum 16
#define rowNum 4
int arr_origin[cbNum];

void initArr()
{
    string str;
    int index = 0;
    while(index < cbNum)
    {
        cin >> str;
        for(int i = 0; i < rowNum; ++i)
        {
            arr_origin[index++] = (str[i] == 'b') ? 1 : 0;
        }
    }
}

bool success(int *arr, int len)
{
    for(int i = 0; i < len - 1; ++i)
        if(arr[i] != arr[i + 1]) return false;
    return true;
}

void changeColor(int *arr_change, int len, int index)
{
    arr_change[index] = !arr_change[index];
    int x = index / rowNum;
    int y = index % rowNum;
    /* top */
    if(x > 0) arr_change[index - rowNum] = !arr_change[index - rowNum];
    /* bottom */
    if(x < rowNum - 1) arr_change[index + rowNum] = !arr_change[index + rowNum];
    /* left */
    if(y > 0) arr_change[index - 1] = !arr_change[index - 1];
    /* right */
    if(y < rowNum - 1) arr_change[index + 1] = !arr_change[index + 1];
}

void combine(int *arr_copy, int len, int *result, int num, int start, int counter, int &ans)
{
    if(counter == 0)
    {
        /* 一定要在这里新开一个和传进来一样的数组，
        ** 否则再次迭代时，原数组改变，传的是上次改变后的数组 */
        int *arr_change = (int*) malloc (sizeof(int) * len);
        for(int i = 0; i < len; ++i)
            arr_change[i] = arr_copy[i];

        for(int i = 0; i < num; ++i)
        {
            changeColor(arr_change, len, result[i]);
        }
        if(success(arr_change, len) == true)
        {
            ans = num;
        }
        free(arr_change);
    }
    else
    {
        for(int i = start; i <= len - counter; ++i)
        {
            result[num - counter] = i;
            combine(arr_copy, len, result, num, i + 1, counter - 1, ans);
        }
    }

}

void flip(int *arr_copy, int len)
{
    int num;
    for(num = 1; num <= len; ++num)
    {
        int *result = (int*) malloc (sizeof(int) * num); //records the index be chosen
        int ans = 0;
        combine(arr_copy, len, result, num, 0, num, ans);
        free(result);
        if(ans == 0) continue;
        else
        {
            cout << ans << endl;
            break;
        }
    }
    if(num == len + 1) cout << "Impossible" << endl;
}

int main()
{
    initArr();
    int *arr_copy = (int*) malloc (sizeof(int) * cbNum);
    for(int i = 0; i < cbNum; ++i)
        arr_copy[i] = arr_origin[i];
    if(success(arr_copy, cbNum) == true) cout << "0" << endl;
    else
    {
        flip(arr_copy, cbNum);
    }
    return 0;
}
