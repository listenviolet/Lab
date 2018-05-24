class Solution{
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) 
	{
		deque<int> q;
		vector<int> ans;

		for(int i = 0; i < nums.size(); ++i)
		{
			while(!q.empty() && nums[i] > q.back()) q.pop_back();
			q.push_back(nums[i]);

			const int s = i - k + 1;
			if(s < 0) continue;
			ans.push_back(q.front());
			if(nums[s] == q.front()) q.pop_front();
		}
		return ans;
	}
};

/*
 * Solution
 * http://zxi.mytechroad.com/blog/heap/leetcode-239-sliding-window-maximum/

window position                        Monotonic Queue            max
-----------------                      ---------------            ----
[1] 3  -1  -3  5  3  6  7                    [1]                        -
[1  3] -1  -3  5  3  6  7                    [3]                        -
[1  3  -1] -3  5  3  6  7                    [3 -1]                     3
1  [3  -1  -3] 5  3  6  7                    [3 -1 -3]                  3
1   3 [-1  -3  5] 3  6  7                    [5]                        5
1   3  -1 [-3  5  3] 6  7                    [5 3]                      5
1   3  -1  -3 [5  3  6] 7                    [6]                        6
1   3  -1  -3  5 [3  6  7]                   [7]                        7

*/

// Beats: 99.36%
// Runtime: 65ms
// hard