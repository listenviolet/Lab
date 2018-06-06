class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> t, res(nums.size());
        for(int i = nums.size() - 1; i >= 0; --i)
        {
            int d = distance(t.begin(), lower_bound(t.begin(), t.end(), nums[i]));
            res[i] = d;
            t.insert(t.begin() + d, nums[i]);
        }
        return res;      
    }
};

// Solution:
// 思路同二分搜索插入，但利用了C++ STL函数：
// distance, lower_bound

// Beats: 48.86%
// Runtime: 44ms
// hard