/*Binary Tree Maximum Path Sum 
Given a binary tree, find the maximum path sum.

The path may start and end at any node in the tree.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
*/

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

这个题难度很大，因为是从任意一个节点到任意一个连着的节点，主要思路还是利用dfs()，把左右边算出来的处理一下，如果做正贡献则加上，负贡献就不加
 */
class Solution {
public:
    int maxPathSum(TreeNode *root) {
        max_sum = INT_MIN; 
        dfs(root); //深度优先遍历
        return max_sum;
    }
    
private:
    int max_sum;
    int dfs(const TreeNode *root){
        if(root==NULL) return 0;
        int l=dfs(root->left);
        int r=dfs(root->right);
        int sum=root->val;
        
        if (l > 0) sum += l; 
        if (r > 0) sum += r;
        
        max_sum = max(max_sum, sum);
        return max(r, l) > 0 ? max(r, l) + root->val : root->val;
    }
};