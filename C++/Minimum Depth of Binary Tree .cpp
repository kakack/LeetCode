/*
Minimum Depth of Binary Tree 

*Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    int minDepth(TreeNode *root) {
        return minDepth(root, false);
    }
    
    int minDepth(TreeNode *root, bool hasbrother){
        if(root==NULL) return hasbrother? INT_MAX:0;
        
        return 1+min(minDepth(root->left, root->right!=NULL), minDepth(root->right, root->left!=NULL));
    }
};