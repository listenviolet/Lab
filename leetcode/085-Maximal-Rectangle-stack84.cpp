class Solution {  
public:  
    int maximalRectangle(vector<vector<char>>& matrix) {  
        if(matrix.size() == 0) return 0;
        int m = matrix.size(), n = matrix[0].size();
        int ret = 0;
        vector<vector<int> > ones(m + 1, vector<int>(n, 0));
        for(int i = 1; i <= m; ++i)
        {
            for(int j = 0; j < n; ++j)
            {
                if(matrix[i - 1][j] == '1') ones[i][j] = ones[i - 1][j] + 1;
                else ones[i][j] = 0;
            }
            ret = max(ret, largestRectangleArea(ones[i]));
        }
        return ret;
    }  
private:
    int largestRectangleArea(vector<int>& heights)
    {
        if(heights.size() == 0) return 0;
        stack<int> s;
        heights.push_back(0);
        int sum = 0;
        for(int i = 0; i < heights.size(); ++i)
        {
            if(s.empty() || heights[i] > heights[s.top()]) s.push(i);
            else 
            {
                int tmp = s.top();
                s.pop();
                int width = s.empty() ? i : i - s.top() - 1;
                sum = max(sum, heights[tmp] * width);
                i--;
            }
        }
        return sum;
    }
};  