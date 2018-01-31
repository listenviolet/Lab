#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool standardizeNumNoDot(string &s)                        //对原字符串直接修改，删去 前后无意义的0 和 整数后面的'.' 返回原字符串有无小数点
{
    while (!s.empty() && '0' == s[0]) s.erase(s.begin());  //去掉开头无意义的0 ：001230
    if (s.empty()) s = "0";//防止n==1的时候，要输出0       //000000    return true -- 无点
    bool notDot = true;                                    //notDot:没有点，默认为真
    for (unsigned i = 0; i < s.size() && notDot; i++)      //若有点，则终止
    {
        if ('.' == s[i]) notDot = false;
    }
    if (notDot) return true;                               //没有点

    while (!s.empty() && '0' == s[s.size()-1]) s.erase(s.end()-1);   //有点的情况下，从末尾擦去无意义的0： 12.100 ->12.1  12.000 -> 12.
    if (!s.empty() && '.' == s[s.size()-1]) s.erase(s.end()-1);      //擦去整数后面的点 12. -> 12   . - > empty (点前后有若干0，从前、后擦去0后，只剩'.')
    if ( s.empty() ) s = "0";                                        //若为空，证明原为0  return false --有点？
    return false;
}

int handleDecimalPoint(string &s)                          //删去小数点后的s，返回原来s小数点后有几位
{
    if (standardizeNumNoDot(s)) return 0;                  //若notDot = true 没有点，返回0
    int fraction = 0;
    int j = 0;
    for (unsigned i = 0; i < s.size() ; i++)
    {
        if (fraction > 0) fraction++;
        if (s[i] != '.') s[j++] = s[i];                    //去掉小数点后的s 即跳过'.'，后面字符前移
        else fraction++;
    }
    s.erase(s.end()-1);                                    //删去最后一个字符：去掉小数点后，字符前移，最后一个字符多余
    return fraction - 1;                                   //返回小数点后面的位数
}

string mulStr(string a, string b)                          //a * b
{
    if ("0" == a || "0" == b) return "0";
    int ap = handleDecimalPoint(a);

    int bp = handleDecimalPoint(b);

    string ans(a.size()+b.size(), '0');                    //初始化全为0
    for (int i = a.size() - 1; i >= 0 ; i--)
    {
        int carry = 0;
        int an = a[i] - '0';
        for (int j = b.size() - 1; j >= 0 ; j--)
        {
            int bn = b[j] - '0';
            int sum = an * bn + carry + ans[i+j+1] - '0';  // 考虑进位总长为 a + b + 1
            carry = sum / 10;
            ans[i+j+1] = sum % 10 + '0';
        }
        if (carry) ans[i] += carry;                        //最高位有进位则为进位数，否则为0，在下面NoDot函数中处理掉0
    }
    if (ap > 0 || bp > 0) ans.insert(ans.end() - ap - bp, '.');  //若a或b为小数点后有位数，则加上小数点，否则不加小数点
    standardizeNumNoDot(ans);                              //去掉无意义的0
    return ans;
}

string sPow(string s, int n)
{
    if (s.empty() || "0" == s) return "0";//为了程序的健壮性，一定要加上
    if (0 == n) return "1";
    if (1 == n) return s;

    string divideStr = sPow(s, n/2);
    divideStr = mulStr(divideStr, divideStr);
    if (n % 2) divideStr = mulStr(divideStr, s);
    return divideStr;
}

void Exponentiation()
{
    string s;
    int n;
    while(cin>>s>>n)
    {
        standardizeNumNoDot(s);//当n==1的时候
        cout<<sPow(s, n)<<endl;
    }
}

int main()
{
    Exponentiation();
    return 0;
}
