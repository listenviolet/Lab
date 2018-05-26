class Solution {
public:
    int numSquares(int n) {
        while(n % 4 == 0)
        {
            n /= 4;
        }
        
        if (n % 8 == 7)
        {
            return 4;
        }
        
        for(int a = 0; a * a <= n; ++a)
        {
            int b = sqrt(n - a * a);
            if(a * a + b * b == n)
                return !!a + !!b;
        }
        return 3;
    }
};

// Description
// Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

// Example 1:

// Input: n = 12
// Output: 3 
// Explanation: 12 = 4 + 4 + 4.
// Example 2:

// Input: n = 13
// Output: 2
// Explanation: 13 = 4 + 9.

// Solution
// 数论（Number Theory）
// 时间复杂度：O(sqrt n)
// 四平方和定理(Lagrange's Four-Square Theorem):
// 所有自然数至多只要用四个数的平方和就可以表示。

// Beats: 98.13%
// Runtime: 5ms
// medium