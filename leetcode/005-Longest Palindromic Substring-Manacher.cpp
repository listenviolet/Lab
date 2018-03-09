#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;

string preProcessing(string s)
{
    int n = s.length();
    if(n == 0) return "^$";
    string ret = "^";
    for(int i = 0; i < n; ++i)
        ret += "#" + s.substr(i, 1);
    ret += "#$";
    return ret;
}

string longestPalindrome(string s)
{
    string T = preProcessing(s);
    int n = T.length();

    int C = 0, R = 0;
    int *p = new int[n];

    for(int i = 1; i < n - 1; ++i)
    {
        int i_mirror = 2 * C - i;
        p[i] = (R > i) ? min(R - i, p[i_mirror]) : 0;

        while(T[i + 1 + p[i]] == T[i - 1 - p[i]])
            p[i]++;

        if(i + p[i] > R)
        {
            C = i;
            R = i + p[i];
        }
    }

    int maxlen = 0;
    int centerIndex = 0;
    for(int i = 1; i < n - 1; ++i)
    {
        if(p[i] > maxlen)
        {
            maxlen = p[i];
            centerIndex = i;
        }
    }

    delete[] p;

    return s.substr((centerIndex - maxlen - 1) / 2, maxlen);
}

int main()
{
    string s;
    cin >> s;
    string sub;
    sub = longestPalindrome(s);
    cout << sub << endl;
}
