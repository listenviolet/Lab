#include <iostream>
#include <cstdlib>
using namespace std;

void combine(int *arr_change, int len, int *result, int num, int start, int counter, int &ans)
{
    if(counter == 0)
    {
        for(int i = 0; i < num; ++i)
        {
            cout << result[i] << " ";
            //changeColor(arr_change, len, result[i]);
        }
        cout << endl;
    }
    else
    {
        for(int i = start; i <= len - counter; ++i)
        {
            result[num - counter] = i;
            combine(arr_change, len, result, num, i + 1, counter - 1, ans);
        }
    }

}

int main()
{
    int arr_change[6] = {0,1,2,3,4,5};
    int num = 3;
    int *result = (int*) malloc (sizeof(int) * num);
    int ans = 0;
    combine(arr_change,6, result, num, 0, num, ans);
}
