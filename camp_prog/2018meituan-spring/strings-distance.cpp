#include <iostream>
#include <cstring>
using namespace std;
char s[100001], t[100001];

/*
** 维护一个(ls - lt +1)大小的窗口，
** a, b, 分别统计当前窗口中a, b的个数
** ans 统计总距离
** i表示移动到s串的第i位，即当前滑动窗口的最后一位
** t[i - ls + lt] 表示对应当前窗口的t，
** t为'a'时，当前窗口（即之后t需要与窗口中每一位对比）与t的距离
** 即为当前窗口中b的个数；反之为a的个数
** 窗口向右移动前，首先减去s 当前窗口第一位a/b值，
** 移动后加上新加入的s的a/b值
** 同理，在用与之对应的t --> t[i - ls + lt] 与新窗口对比
** 当窗口末位移动过ls后，终止，
** ans 即保留最终字符串距离值。
*/

int main()
{
    cin >> s >> t;
    int ls = strlen(s), lt = strlen(t);
    int a = 0, b = 0, ans = 0;
    for(int i = 0; i < ls - lt + 1; ++i)
    {
        if(s[i] == 'a') a++;
        else b++;
    }
    for(int i = ls - lt; i < ls;)
    {
        if(t[i - ls + lt] == 'a') ans += b; else ans += a;
        if(s[i - ls + lt] == 'a') a--; else b--;   //去掉s当前窗口第一个，之后窗口向右移
        if(s[++i] == 'a') a++; else b++;
    }
    cout << ans << endl;
    return 0;
}

/*
** 给出两个相同长度的由字符 a 和 b 构成的字符串，
** 定义它们的距离为对应位置不同的字符的数量。
** 如串”aab”与串”aba”的距离为 2；串”ba”与串”aa”的距离为 1；
** 串”baa”和串”baa”的距离为 0。
** 下面给出两个字符串 S 与 T，
** 其中 S 的长度不小于 T 的长度。我们用|S|代表 S 的长度，|T|代表 T 的长度，
** 那么在 S 中一共有|S|-|T|+1 个与 T 长度相同的子串，
** 现在你需要计算 T 串与这些|S|-|T|+1 个子串的距离的和。
**************************************************************
** input:
** 第一行包含一个字符串 S。
** 第二行包含一个字符串 T。
** S 和 T 均由字符 a 和 b 组成，1 ≤ |T| ≤ |S| ≤105
*/

/*
** 题解：
** 这个题目的数据量是|T|<|S|<10^5
** 所以直接暴力的解法是O（|S|*|T|）肯定会超时的。
** 我的解法是O（|S|）的，肯定不会超时了。
** 关键词：反演
** 具体思路：对于T中的每个字符，都是要和S中的连续|S|-|T|+1个字符相比较的。
** 比如T中的第1个字符，要和S的前|S|-|T|+1个字符相比较
** T中的第2个字符，要和S的第2个字符到第|S|-|T|+2个字符相比较
** 。。。。。。
** 每次统计T中的1个字符和S中的|S|-|T|+1个字符有多少个是不一样的，
** 当统计T中的下一个字符时，S中的|S|-|T|+1个字符只要往右移一步就行，
** 就是去掉第一个字符，再在最后一个字符后面补一个新的字符。
*/
