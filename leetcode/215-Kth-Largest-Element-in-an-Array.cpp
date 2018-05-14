class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        int l = 0, r = nums.size() - 1;
        int s = nums.size();
        int tr, tl;
        while(true)
        {
            tl = l;
            tr = r;
            int key = nums[tl];
            while(tr > tl)
            {
                while(tr > tl && nums[tr] >= key) tr--;
                nums[tl] = nums[tr];
                while(tr > tl && nums[tl] <= key) tl++;
                nums[tr] = nums[tl];
            }
            nums[tl] = key;
            
            if(tl == s - k) break;
            if(tl < s - k) 
            {
                tr = r;
                l = tl + 1;
            }
            else
            {
                tr = tl - 1;
                tl = l;
                r = tr;
            }
        }
        return nums[tl];
    }
};

// Beats: 38.91%
// Runtime: 23ms
// medium