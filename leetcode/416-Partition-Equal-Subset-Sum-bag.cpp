class Solution {
public:
    bool canPartition(vector<int>& nums) {
        const int sum = std::accumulate(nums.begin(), nums.end(), 0);
        if(sum % 2 != 0) return false;
        vector<int> dp(sum + 1, 0);
        dp[0] = 1;
        for(const int num : nums)
        {
            for(int i = sum; i >= 0; --i)
                if(dp[i]) dp[i + num] = 1;  
                //从sum -> 0 遍历：保证用的是上一次循环的结果
            if(dp[sum / 2]) return true;
        }
        return false;
    }
};

// Description:
// Given a non-empty array containing only positive integers, 
// find if the array can be partitioned into two subsets 
// such that the sum of elements in both subsets is equal.

// Note:
// Each of the array element will not exceed 100.
// The array size will not exceed 200.
// Example 1:

// Input: [1, 5, 11, 5]

// Output: true

// Explanation: The array can be partitioned as [1, 5, 5] and [11].
// Example 2:

// Input: [1, 2, 3, 5]

// Output: false

// Explanation: The array cannot be partitioned into equal sum subsets.
///////////////////////////////////////////////////////////////////

// Solution:
// http://zxi.mytechroad.com/blog/dynamic-programming/leetcode-416-partition-equal-subset-sum/

// DP:
// dp[i][j]: whether can sum to j using first i numbers
// dp[i][j] = true if dp[i - 1][j - num]
// check dp[n - 1][sum / 2]
// int d[-1][0] = true
// Time complexity: O(n^2 * sum) -> O(n * sum)
// Space complexity: O(sum)

// num  dp[i - 1] == true           dp[i] == true
// 1    {0}                         {0, 1}
// 5    {0, 1}                      {0, 5, 6}
// 11   {0, 5, 6}                   {0, 5, 6, 11, 16, 17}
//                                            **
// 5    {0, 5, 6, 11, 16, 17}       {0, 5, 6, 11, 16, 21, 22}
//                                            **                      

// Beats: 79.87%
// Runtime: 24ms
// medium
