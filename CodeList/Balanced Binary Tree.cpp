/*
Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

For this problem, a height-bal
*
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

这个题我是用最傻的模拟法做的，居然没超时！如果空树则是平衡的，先判左边平衡，再算左右数的depth是否绝对值比1大，再判右边平衡，如果都满足则是平衡树
 */
class Solution {
public:
    bool isBalanced(TreeNode *root) {
        if(root==NULL) 
          return true;
        else if(!isBalanced(root->left))
          return false;
        else if(abs(getDepth(root->left)-getDepth(root->right))>1)
          return false;
        else if(!isBalanced(root->right))
          return false;
        else
          return true;
    }
    
    int getDepth(TreeNode *root){
        if(root==NULL)
          return 0;
        else
          return getDepth(root->left)>getDepth(root->right)?getDepth(root->left)+1:getDepth(root->right)+1;
         
    }
    
};