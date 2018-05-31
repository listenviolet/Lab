class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int l = 0, r = 0;
        for (const char ch: s)
        {
            l += (ch == '(');
            if(l == 0)
                r += (ch == ')');
            else
                l -= (ch == ')');
        }
        
        vector<string> ans;
        dfs(s, 0, l, r, ans);
        return ans;
    }
private:
    bool isValid(const string& s)
    {
        int count = 0;
        for(const char ch : s)
        {
            if(ch == '(') ++count;
            if(ch == ')') --count;
            if(count < 0) return false;
        }
        return count == 0;
    }
    
    void dfs(const string& s, int start, int l, int r, vector<string>& ans)
    {
        if(l == 0 && r == 0)
        {
            if(isValid(s)) ans.push_back(s);
            return;
        }
        
        for(int i = start; i < s.length(); ++i)
        {
            if(i != start && s[i] == s[i - 1]) continue;
            
            if(s[i] == '(' || s[i] == ')')
            {
                string curr = s;
                curr.erase(i, 1);
                if(r > 0 && s[i] == ')')
                    dfs(curr, i, l, r - 1, ans);
                else if(l > 0 && s[i] == '(')
                    dfs(curr, i, l - 1, r, ans);
            }
        }
    }
};

// Description:
// Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

// Note: The input string may contain letters other than the parentheses ( and ).

// Example 1:

// Input: "()())()"
// Output: ["()()()", "(())()"]
// Example 2:

// Input: "(a)())()"
// Output: ["(a)()()", "(a())()"]
// Example 3:

// Input: ")("
// Output: [""]

// Solution:
// http://zxi.mytechroad.com/blog/searching/leetcode-301-remove-invalid-parentheses/

// 1.  Check whether a input string is valid:
//     count(')') <= count('('), i < n - 1
//     count(')') == count('('), i = n - 1
// 2.  Compute min number of '(' and ')' to remove:
//     l: #'(' to remove
//     r: #')' to remove
// 3.  Try all possible ways to remove r ')' and l '('.
//     Remove ')' first to make prefix valid

//     dfs(s, l, r):
//         if l == 0 and r == 0 and valid(s):
//             ans.add(s)

//     Avoid duplications:
//     Only remove the first parentheses if there are consecutive ones.

//     Time complexity: O(2^(l + r))
//     Space complexity: O((l + r) ^ 2) - O(n^2)

// Beats: 69.54%
// Runtime: 5ms
// hard