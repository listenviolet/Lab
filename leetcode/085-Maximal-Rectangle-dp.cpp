class Solution {  
public:  
    int maximalRectangle(vector<vector<char>>& matrix) {  
        if (matrix.size() == 0) {  
            return 0;  
        }  
        int m = matrix.size(), n = matrix[0].size();  
        int ret = 0;  
        vector<int> heights(n,0), lefts(n, 0), rights(n, n);  
        for (int i = 0; i < m; ++i) {  
            int cur_left = 0, cur_right = n;  
            for(int j = 0; j < n; ++j) {  
                heights[j] = matrix[i][j] == '0' ? 0 : heights[j] + 1;  
                if (heights[j] > 0) {  
                    lefts[j] = max(lefts[j], cur_left);  
                }  
                else {  
                    lefts[j] = 0;  
                    cur_left = j + 1;  
                }  
            }  
            for(int j = n - 1; j >= 0; --j) {  
                if (heights[j] > 0) {  
                    rights[j] = min(rights[j], cur_right);  
                }  
                else {  
                    rights[j] = n;  
                    cur_right = j;  
                }  
            }  
            for(int j = 0; j < n; ++j) {  
                cout << lefts[j] << " " << rights[j] << ";";
                ret = max(ret, (rights[j] - lefts[j]) * heights[j]);  
            }  
            cout << endl;
        }  
        return ret;  
    }  
}; 

/* 动态规划法：
** 由于在暴力枚举法中我们每碰到一个高度不为0的情况
** 就往左搜索找到当前最低的高度然后更新面积，
** 所以会导致重复计算。
** 动态规划刚好可以通过记录原有信息来避免重复搜索。
** 那么每一行我们需要记录什么呢？
** 我们需要记录并维护的就是一行中每个位置高度的左右边界。
*/