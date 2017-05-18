/**Flatten Binary Tree to Linked List 
Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:
   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6

 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

递归的办法，把左边右边的子树都变成要求的形状，然后再把左边的子树插入root和右子树之间
 */
class Solution {
public:
    void flatten(TreeNode *root) {
        
        if(root==NULL) return;
        
        flatten(root->left);
        flatten(root->right);
        
        if(root->left==NULL) return;
        
        TreeNode* ptr=root->left;
        while(ptr->right!=NULL)
          ptr=ptr->right;//到达左树的最底端
          
        ptr->right=root->right;
        root->right=root->left;
        root->left=nullptr;
        
    }
};