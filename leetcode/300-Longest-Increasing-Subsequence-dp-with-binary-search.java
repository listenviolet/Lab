public class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        int len = 0;
        for (int num : nums) {
            int i = Arrays.binarySearch(dp, 0, len, num);
            if (i < 0) {
                i = -(i + 1);
            }
            dp[i] = num;
            if (i == len) {
                len++;
            }
        }
        return len;
    }
}

// Solution:
// In this approach, we scan the array from left to right. 
// We also make use of a dpdp array initialized with all 0's. 
// This dpdp array is meant to store the increasing subsequence 
// formed by including the currently encountered element. 
// While traversing the numsnums array, 
// we keep on filling the dpdp array with the elements encountered so far. 
// For the element corresponding to the jth index (nums[j]), 
// we determine its correct position in the dp array(say ith index) 
// by making use of Binary Search
// (which can be used since the dp array is storing increasing subsequence) 
// and also insert it at the correct position. 
// An important point to be noted is that for Binary Search, 
// we consider only that portion of the dp array 
// in which we have made the updates by inserting some elements at their correct positions(which remains always sorted). 
// Thus, only the elements upto the ith index in the dp array 
// can determine the position of the current element in it. 
// Since, the element enters its correct position(ii) in an ascending order in the dpdp array, 
// the subsequence formed so far in it is surely an increasing subsequence. 
// Whenever this position index ii becomes equal to the length of the LIS formed so far(lenlen), 
// it means, we need to update the lenlen as len = len + 1.

// Note: dpdp array does not result in longest increasing subsequence, but length of dpdp array will give you length of LIS.

// Consider the example:

// input: [0, 8, 4, 12, 2]

// dp: [0]

// dp: [0, 8]

// dp: [0, 4]

// dp: [0, 4, 12]

// dp: [0 , 2, 12] which is not the longest increasing subsequence, 
// but length of dpdp array results in length of Longest Increasing Subsequence.

// Beats: 72.90%
// Runtime: 3ms
// medium
