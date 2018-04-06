class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if(matrix.size() == 0) return 0;
        int m = matrix.size(), n = matrix[0].size();
        int ret = 0;
        vector<int> heights(n, 0);
        for(int i = 0; i < m; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                if(matrix[i][j] == '0')
                {
                    heights[j] = 0;
                    continue;
                }
                heights[j]++;
                int min_height = heights[j];
                for(int k = j; k >= 0; --k)
                {
                    min_height = min(heights[k], min_height);
                    ret = max(ret, (j - k + 1) * min_height);
                }
            }
        }
        return ret;
        
    }
};

/*
** 暴力枚举法：一行一行的遍历数组，维护每个位置到顶部的高度，
** 如果某位置高度大于0，就往回扫描到首列，同时维护一个当前最低的高度，
** 这样就可以求出从这个位置到第一列的最大面积了。时间复杂度是O(m*n*n)，
** 当然通过转置可以优化到O(m*n*min(m, n))，但数量级不变。空间复杂度是O(n)。
*/