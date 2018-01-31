#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool standardizeNumNoDot(string &s)                        //��ԭ�ַ���ֱ���޸ģ�ɾȥ ǰ���������0 �� ���������'.' ����ԭ�ַ�������С����
{
    while (!s.empty() && '0' == s[0]) s.erase(s.begin());  //ȥ����ͷ�������0 ��001230
    if (s.empty()) s = "0";//��ֹn==1��ʱ��Ҫ���0       //000000    return true -- �޵�
    bool notDot = true;                                    //notDot:û�е㣬Ĭ��Ϊ��
    for (unsigned i = 0; i < s.size() && notDot; i++)      //���е㣬����ֹ
    {
        if ('.' == s[i]) notDot = false;
    }
    if (notDot) return true;                               //û�е�

    while (!s.empty() && '0' == s[s.size()-1]) s.erase(s.end()-1);   //�е������£���ĩβ��ȥ�������0�� 12.100 ->12.1  12.000 -> 12.
    if (!s.empty() && '.' == s[s.size()-1]) s.erase(s.end()-1);      //��ȥ��������ĵ� 12. -> 12   . - > empty (��ǰ��������0����ǰ�����ȥ0��ֻʣ'.')
    if ( s.empty() ) s = "0";                                        //��Ϊ�գ�֤��ԭΪ0  return false --�е㣿
    return false;
}

int handleDecimalPoint(string &s)                          //ɾȥС������s������ԭ��sС������м�λ
{
    if (standardizeNumNoDot(s)) return 0;                  //��notDot = true û�е㣬����0
    int fraction = 0;
    int j = 0;
    for (unsigned i = 0; i < s.size() ; i++)
    {
        if (fraction > 0) fraction++;
        if (s[i] != '.') s[j++] = s[i];                    //ȥ��С������s ������'.'�������ַ�ǰ��
        else fraction++;
    }
    s.erase(s.end()-1);                                    //ɾȥ���һ���ַ���ȥ��С������ַ�ǰ�ƣ����һ���ַ�����
    return fraction - 1;                                   //����С��������λ��
}

string mulStr(string a, string b)                          //a * b
{
    if ("0" == a || "0" == b) return "0";
    int ap = handleDecimalPoint(a);

    int bp = handleDecimalPoint(b);

    string ans(a.size()+b.size(), '0');                    //��ʼ��ȫΪ0
    for (int i = a.size() - 1; i >= 0 ; i--)
    {
        int carry = 0;
        int an = a[i] - '0';
        for (int j = b.size() - 1; j >= 0 ; j--)
        {
            int bn = b[j] - '0';
            int sum = an * bn + carry + ans[i+j+1] - '0';  // ���ǽ�λ�ܳ�Ϊ a + b + 1
            carry = sum / 10;
            ans[i+j+1] = sum % 10 + '0';
        }
        if (carry) ans[i] += carry;                        //���λ�н�λ��Ϊ��λ��������Ϊ0��������NoDot�����д����0
    }
    if (ap > 0 || bp > 0) ans.insert(ans.end() - ap - bp, '.');  //��a��bΪС�������λ���������С���㣬���򲻼�С����
    standardizeNumNoDot(ans);                              //ȥ���������0
    return ans;
}

string sPow(string s, int n)
{
    if (s.empty() || "0" == s) return "0";//Ϊ�˳���Ľ�׳�ԣ�һ��Ҫ����
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
        standardizeNumNoDot(s);//��n==1��ʱ��
        cout<<sPow(s, n)<<endl;
    }
}

int main()
{
    Exponentiation();
    return 0;
}
