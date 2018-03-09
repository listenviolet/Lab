class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> searched;  
        vector<int> res;  
        for (int i = 0; i < nums.size(); ++i){  
            if (searched.count(target - nums[i])){  
                res.push_back(searched[target - nums[i]]);  
                res.push_back(i);  
                return res;  
            } else {  
                searched[nums[i]] = i;  
            }  
        }  
        res.push_back(-1);  
        res.push_back(-1);  
        return res;  
    }
};