/**
Binary Tree Level Order Traversal
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]

用最简单的递归法，先塞进去中间的，然后左边遍历，再右边遍历


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
    void traverse(TreeNode *root, int level, vector<vector<int>> &result) { 
        if (!root) return;
        if (level > result.size()) 
           result.push_back(vector<int>());
           
        result[level-1].push_back(root->val); 
        traverse(root->left, level+1, result); 
        traverse(root->right, level+1, result);
    }

    vector<vector<int> > levelOrder(TreeNode *root) {
        
        vector<vector<int> > result;
        traverse(root, 1, result); 
        return result;
        
    }
};