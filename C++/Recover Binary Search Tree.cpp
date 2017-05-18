/**Recover Binary Search Tree
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

这个是用空间复杂度O(n)的办法，先中序遍历后排序，然后重新插入val
 */
class Solution {
public:
    void Travel(TreeNode* root,vector<int> &vals, vector<TreeNode*> &nodes){
        if(root==NULL) 
           return;
        Travel(root->left, vals, nodes);
        vals.push_back(root->val);
        nodes.push_back(root);
        Travel(root->right, vals, nodes);
    }
    
    void recoverTree(TreeNode *root) {
        vector<TreeNode*> nodes;
        vector<int> vals;
        
        Travel(root, vals, nodes);
        
        sort(vals.begin(),vals.end());
        
        for(int i = 0;i<nodes.size();i++)
           nodes[i]->val = vals[i];
    
    }
};