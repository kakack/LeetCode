/*
Validate Binary Search Tree 
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
 *
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

我总归觉得这个题有点扯淡，原先的test case好好的非得去做修改极限值，int、long这种上掐人根本没什么意思
 */
class Solution {
public:
    // bool isValidBST(TreeNode *root) {
    //     return isValid(root, long.MIN_VALUE, long.MAX_VALUE);
        
    // }
    
    // bool isValid(TreeNode *root, int min, int max){
        
    //     if(root == NULL||(root->left==NULL&&root->right==NULL)) 
    //       return true;
        
    //     if(root->left==NULL&&root->right!=NULL)
    //       return root->val<root->right->val&&isValid(root->right, root->val,max);
          
    //     else if(root->left!=NULL&&root->right==NULL)
    //       return root->val>root->left->val&&isValid(root->left, min, root->val);
          
    //     else if(root->val>min&&root->val<max&&isValid(root->left, min, root->val)&&isValid(root->right, root->val, max))
    //      return true;
         
    //     else
    //      return false;
    // }


/*
 *这个解法用了中序遍历，用两个全局变量来控制，每次中间的root跟左子树中最大值比
 */    
     bool first = true;
    int prev = 0;
public:
    bool isValidBST(TreeNode *root) {
        if(root == NULL) return true;

        return (
            isValidBST(root->left)
            && check(root->val)
            && isValidBST(root->right));
    }

    bool check(int val)
    {
        if(first)
        {
            first = false;
            prev = val;
            return true;
        }

        if(prev >= val) return false;

        prev = val;
        return true;
    }

    
};