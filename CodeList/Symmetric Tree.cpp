/*Symmetric Tree


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

*/

/**
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
    bool isSymmetric(TreeNode *root) {
        
       if(root==NULL)
         return true;
         
     return isSym(root->left,root->right);
        
    }
    bool isSym(TreeNode *left,TreeNode *right){
        if(left==NULL)
          return right==NULL;
        if(right==NULL)
          return left==NULL;
        if(left->val!=right->val)
          return false;
        if(!isSym(left->left,right->right))
          return false;
        if(!isSym(left->right,right->left))
          return false;
        
        return true;
    }
};