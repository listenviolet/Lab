class Solution {
public:
    string dfs(string s, int &k)
    {
        string ans;
        int cnt = 0;
        while(k < s.size())
        {
            if(isdigit(s[k])) cnt = cnt * 10 + (s[k++] - '0');
            else if(s[k] == '[')
            {
                string tem = dfs(s, ++k);
                for(int i = 0; i < cnt; ++i) ans += tem;
                cnt = 0;
            }
            else if(s[k] == ']')
            {
                k++;
                return ans;
            }
            else ans += s[k++];
        }
        
        return ans;
    }
    
    
    
    string decodeString(string s) {
        int k = 0;
        return dfs(s, k);
    }
};

// Description:
// Given an encoded string, return it's decoded string.

// The encoding rule is: k[encoded_string], 
// where the encoded_string inside the square brackets 
// is being repeated exactly k times. 
// Note that k is guaranteed to be a positive integer.

// You may assume that the input string is always valid; 
// No extra white spaces, square brackets are well-formed, etc.

// Furthermore, you may assume that the original data 
// does not contain any digits and 
// that digits are only for those repeat numbers, k. 
// For example, there won't be input like 3a or 2[4].

// Examples:

// s = "3[a]2[bc]", return "aaabcbc".
// s = "3[a2[c]]", return "accaccacc".
// s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

// Solution:
// https://blog.csdn.net/qq508618087/article/details/52439114
// 思路: 一个DFS的题目, 给定的字符串可能会有嵌套很多层,
// 在每一层我们只要在碰到正常的字符就保存到当前层的结果中, 
// 如果碰到数字就另外保存起来作为倍数, 
// 碰到'[' 就进入下层递归, 
// 碰到']' 就将当前层结果返回,
// 这样在返回给上层之后就可以用倍数加入到上层结果字符串中.
// 最终当所有层都完成之后就可以得到结果. 在不同层次的递归中, 
// 我们可以维护一个共同的位置索引, 
// 这样在下层递归完成之后上层可以知道已经运算到哪里了.

// Beats: 87.53%
// Runtime: 3ms
// medium