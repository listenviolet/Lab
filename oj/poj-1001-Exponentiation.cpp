#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define maxn 10
#define max_arr 200

int tmp[maxn];

int loc(string s)
{
    for(int i = 0; i < s.size(); ++i)
    {
        if(s[i] == '.') return i;  //location of "." in string index
    }
}

int transToInt(string s)
{
    /* delete the point */
    int locpoint = loc(s);
    int len_new = s.size() - 1;
    for(int i = locpoint; i < len_new; ++i)
    {
        s[i] = s[i + 1];
    }

    /* without 0 */
    int for_fir = 0;
    int back_fir = len_new - 1;
    int index_arr = 0;
    int len_arr;

    while(s[for_fir] == '0' && for_fir < len_new) for_fir++;
    while(s[back_fir] == '0' && back_fir >=0) back_fir--;

    if(for_fir == len_new) {tmp[0] = 0; return 1;}
    else
    {
        int len_arr = back_fir - for_fir + 1;
        while(index_arr < len_arr)
        {
            tmp[index_arr] = s[back_fir - index_arr] - '0';
            index_arr++;
        }
        return len_arr;
    }
}

int* multiply(int* a, int len_arr, int n) //不可以用multi指向result数组，二者将同时变化
{
    int multi[maxn], result[maxn];
    for(int i = 0; i < len_arr; ++i)
        multi[i] = a[i];
    int len_multi = len_arr;
    int len_result;

    while(n >= 2)
    {
        memset(result, 0, sizeof(result));
        for(int i = 0; i < len_arr; ++i)
        {
            for(int j = 0; j < len_multi; ++j)
            {
                result[i + j] += a[i] * multi[j];
                cout << a[i] << " * " << multi[j] << " = "<<result[i+j] << " ";
            }
        }
        cout <<endl;
        cout << "result:" << endl;
        for(int i = len_arr + len_multi - 2; i >= 0; --i)
            cout << i << ": " << result[i] << " ";
        cout <<endl;

        int ncarry = 0;
        for(int i = 0; i < len_arr + len_multi - 1; ++i)
        {
            result[i] = (result[i] + ncarry) %10;
            ncarry = (result[i] + ncarry) / 10;
        }
        len_result = len_arr + len_multi - 1;
        if(ncarry) { result[len_result] = ncarry; len_result++; }

        for(int i = 0; i < len_result; ++i)
        {
            multi[i] = result[i];
        }
        len_multi = len_result;
        n--;
    }

    return result;
}

int main()
{
    int n;
    string s;
    while(cin >> s >> n)
    {
        int len_arr = transToInt(s);
        /*
        for(int i = len_arr - 1; i >= 0; --i)
            cout << tmp[i];
        cout <<endl;
        */
        int *multi;
        multi = multiply(tmp, len_arr, n);
    }
}
