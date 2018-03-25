#include <iostream>
#include <cstring>
#include <unordered_map>
#include <vector>
using namespace std;

string  minWindow(string s, string t)
{
    unordered_map<char, int> hash;
    int num = t.size(), len = INT_MAX, start = 0, left = 0;

    for(auto val : t) hash[val]++;

    for(int i = 0; i < s.size(); ++i)
    {
        if(hash[s[i]]-- > 0) num--;
        while(num == 0)
        {
            len = (i - left + 1) < len ? (i - (start = left) + 1) : len;
            if(hash[s[left++]]++ == 0) num++;
        }
    }
    return len == INT_MAX ? "" : s.substr(start, len);
}

int main()
{
    string s,t;
    cin >> s >> t;
    cout << minWindow(s, t) << endl;
    return 0;
}
/*
ADOBECODEBANC
ABC
*/

/*
** unordered_map
** uses C++ 11
** select that in compiler
*/

/*
** hash初始值： 在T中出现过的为T中出现的次数
** T中没有的，S中的，赋初值为0
** 遍历S
** 遇到一个字符，该字符对应hash的value - 1
** S中有的，T中没有的，hash会变为负数
** T中有的，hash减在S中经过的字符串中出现该字符的个数
** 变为0，表示该段字符串以包含T中所有的该字符
** 再遇到该字符，hash会变为负数，意为不必要的字符
** num: 当hash 为正，证明找到一个有意义的T中的字符，num - 1
** 这个num就是总共有多少字符，我们需要这个来标记是不是找完了所有字符，
** 这也是能够在O(1)时间内判断当前窗口是不是覆盖了Ｔ的关键
** 这样当总的数量为０的时候我们就找到了一个覆盖Ｔ的子串窗口．
****************************
** 排除左端不必要字符：
** 这个窗口因为左端可能包含了一些不必要的字符，
** 因此我们需要将窗口的左端向右移动，使其正好包含Ｔ．
** 在窗口左端向右移动的过程中需要将碰到字符在hash表中＋１，
** 不必要的字符，其hash会从负数开始加
** 如果当前字符在hash表中的计数为０，而且我们又碰到了，
** 说明这个字符是出现在Ｔ中的，因此num要加一．
****************************
** 遍历完整个S，即找到len最小的start,len
*/
