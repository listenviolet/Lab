#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

#define maxn 10
#define max_arr 200

int tmp[maxn];              // record the string to int
int multi_result[max_arr];  // record the int multiply result

int loc(string s)
{
    for(int i = 0; i < s.size(); ++i)
    {
        if(s[i] == '.') return i;  //location of "." in string index
    }
    return -1; //整数没有小数点
}

int transToInt(string s)
{
    /* delete the point */
    int locpoint = loc(s);
    int for_fir = 0;
    int index_arr = 0;

    if(locpoint == -1)  //整数--不加点
    {
        while(s[for_fir] == '0' && for_fir < s.size()) for_fir++;
        if(for_fir == s.size()) {tmp[0] = 0; return 1;}
        while(index_arr < s.size() - for_fir)
        {
            tmp[index_arr] = s[s.size() - 1 - index_arr] - '0';
            index_arr++;
        }
        return index_arr;
    }

    int len_new = s.size() - 1;
    for(int i = locpoint; i < len_new; ++i)
    {
        s[i] = s[i + 1];
    }

    /* without 0 */
    int back_fir = len_new - 1;
    int len_arr;

    while(s[for_fir] == '0' && for_fir < len_new) for_fir++;
    while(s[back_fir] == '0' && back_fir >=0) back_fir--;

    if(for_fir == len_new) {tmp[0] = 0; return 1;}  //全0
    else
    {
        int index_end = (back_fir < locpoint) ? locpoint - 1 : back_fir;
        //int len_arr = back_fir - for_fir + 1;
        int len_arr = index_end - for_fir + 1;
        while(index_arr < len_arr)
        {
            //tmp[index_arr] = s[back_fir - index_arr] - '0';
            tmp[index_arr] = s[index_end - index_arr] - '0';
            index_arr++;
        }
        return len_arr;
    }
}

int multiply(int* a, int len_arr, int n) //不可以用multi指向result数组，二者将同时变化
{
    int multi[max_arr], result[max_arr];
    for(int i = 0; i < len_arr; ++i)
        multi[i] = a[i];
    int len_multi = len_arr;
    int len_result;

    if(n == 1)
    {
        for(int i = 0; i < len_arr; ++i)
        {
            multi_result[i] = a[i];
        }
        return len_arr;
    }

    while(n >= 2)
    {
        memset(result, 0, sizeof(result));
        for(int i = 0; i < len_arr; ++i)
        {
            for(int j = 0; j < len_multi; ++j)
            {
                result[i + j] += a[i] * multi[j];
            }
        }
        int ncarry = 0;
        for(int i = 0; i < len_arr + len_multi - 1; ++i)
        {
            int c = result[i] + ncarry;
            result[i] = c %10;
            ncarry = c / 10;
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

    for(int i = 0; i < len_result; ++i)
    {
        multi_result[i] = result[i];
    }

    return len_result;
}

void addDot(int* a, int len, int loc, int n) // loc : 小数点后面有几位
{
    int new_loc = n * loc;
    int back_first = 0;
    while(a[back_first] == 0) back_first++;
    if(new_loc <= back_first) // 整数
    {
        for(int i = len - 1; i >= new_loc; --i)
            cout << a[i];
        cout << endl;
    }
    else if (new_loc <= len - 1) //new_loc > back_first  x.xxxx xx.x
    {
        for(int i = len - 1; i >= new_loc; --i)
        {
            cout << a[i];
        }
        cout << ".";
        for(int i = new_loc - 1; i >= back_first; --i)
        {
            cout << a[i];
        }
        cout << endl;
    }
    else if(new_loc >= len)
    {
        cout << ".";
        for(int i = new_loc - 1; i >= len; --i)
        {
            cout << "0";
        }
        for(int i = len - 1; i >= back_first; --i)
        {
            cout << a[i];
        }
        cout << endl;
    }
}

int reLoc(string s)
{
    int back_zero = s.size() - 1;
    while(back_zero >= loc(s) && s[back_zero] == '0')
    {
        back_zero--;
    }

    return back_zero - loc(s);
}

int main()
{
    int n;
    string s;
    while(cin >> s >> n)
    {
        int len_arr = transToInt(s);
        if(len_arr == 1 && tmp[0] == 0) cout << "0" << endl;
        else if(n == 0) cout << "1" << endl;
        else
        {
            int len_result = multiply(tmp, len_arr, n); // record in multi_result
            int re_loc = (loc(s) == -1) ? 0 : reLoc(s);
            addDot(multi_result, len_result, re_loc, n);
        }
    }
    return 0;
}
