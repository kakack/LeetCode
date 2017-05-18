/**
Binary Tree Postorder Traversal
Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

先写个递归再说

Note: Recursive solution is trivial, could you do it iteratively?

 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> postorderTraversal(TreeNode *root) {
        vector<int> ans;
        
        if(root==NULL)
          return ans;
        
        vector<int> left=postorderTraversal(root->left);
        vector<int> right=postorderTraversal(root->right);
        ans.insert(ans.end(),left.begin(),left.end());
        ans.insert(ans.end(),right.begin(),right.end());
        ans.push_back(root->val);
        
        return ans;
    }
};