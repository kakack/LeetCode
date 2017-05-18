/**

Binary Tree Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

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
    vector<int> preorderTraversal(TreeNode *root) {
        vector<int> ans;
        
        if(root==NULL)
          return ans;
        
        vector<int> left=preorderTraversal(root->left);
        vector<int> right=preorderTraversal(root->right);
        
        ans.push_back(root->val);
        ans.insert(ans.end(),left.begin(),left.end());
        ans.insert(ans.end(),right.begin(),right.end());

        
        
        
        return ans;
    }
};