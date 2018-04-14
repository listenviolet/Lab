/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */


/**
 * Threaded Binary Tree
 * Morris Traversal
 */

class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List <Integer> res = new ArrayList <> ();
        TreeNode curr = root;
        TreeNode pre;
        while(curr != null)
        {
            if(curr.left == null)
            {
                res.add(curr.val);
                curr = curr.right;
            }
            else
            {
                pre = curr.left;
                while(pre.right != null) pre = pre.right;  //find the rightmost
                pre.right = curr;
                
                //generate new root and remove curr.left 
                TreeNode temp = curr;
                curr = curr.left;  // move cur to the top of the new tree (let curr.left to be the root)
                temp.left = null;  // remove the temp = ori_curr.left
            }
        }
        return res;
    }
}