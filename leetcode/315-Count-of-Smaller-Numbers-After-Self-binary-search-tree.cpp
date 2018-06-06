class Solution {
public:
    struct Node
    {
        int val, smaller;
        Node *left, *right;
        Node(int v, int s): val(v), smaller(s), left(NULL), right(NULL) {}
    };
    
    int insert(Node *&root, int v)
    {
        if(!root) return (root = new Node(v, 0)), 0;
        else if (root->val > v) return root -> smaller++, insert(root -> left, v);
        else return insert(root -> right, v) + root -> smaller + (root ->val < v ? 1 : 0);
    }
    
    
    vector<int> countSmaller(vector<int>& nums) {
        vector<int> res(nums.size());
        Node *root = NULL;
        for(int i = nums.size() - 1; i >= 0; --i)
        {
            res[i] = insert(root, nums[i]);
        }
        return res;
    }
};

// Solution:
// 利用二分搜索树来解的方法，我们来构造一棵二分搜索树，
// 稍有不同的地方是
// 需要加一个变量smaller来记录比当前节点值小的所有节点的个数，
// 我们每插入一个节点，会判断其和根节点的大小，
// 如果新的节点值小于根节点值，则其会插入到左子树中，
// 此时要增加根节点的smaller，
// 并继续递归调用左子节点的insert。
// 如果节点值大于根节点值，
// 则需要递归调用右子节点的insert并加上根节点的smaller。

// Beats: 94.80%
// Runtime: 30ms
// hard