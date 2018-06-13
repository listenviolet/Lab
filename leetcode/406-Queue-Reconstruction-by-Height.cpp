class Solution {
public:
    vector<pair<int, int>> reconstructQueue(vector<pair<int, int>>& people) {
        sort(people.begin(), people.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.first > b.first || (a.first == b.first && a.second < b.second);
        });
        vector<pair<int, int>> res;
        for (auto a : people) {
            cout << a.first << "->" << a.second << endl;
            res.insert(res.begin() + a.second, a);
            
        }
        return res;
    }
};

// Description:
// Suppose you have a random list of people standing in a queue. 
// Each person is described by a pair of integers (h, k), 
// where h is the height of the person 
// and k is the number of people in front of this person 
// who have a height greater than or equal to h. 
// Write an algorithm to reconstruct the queue.

// Note:
// The number of people is less than 1,100.


// Example

// Input:
// [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

// Output:
// [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

// Solution:
// 将people先按照从大到小排序，然后依次插入到目标数组中。
// 这样做的原因是，对于大的元组，再向后遍历的过程中，
// 遇到的都比其“小”，对于[i,j]中的j的相对次序没有影响。

// Beats: 15.05%
// Runtime: 57ms
// medium