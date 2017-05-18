/**
Binary Tree Level Order Traversal II 

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

跟之前那题一样，之后把结果反一反就行了，我去


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
    void travel(TreeNode *root, int level, vector<vector<int> > &result){
        if(!root) return;
        if(level>result.size())
          result.push_back(vector<int>());
          
        result[level-1].push_back(root->val);
        travel(root->left,level+1,result);
        travel(root->right,level+1,result);
    }
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        vector<vector<int> > result;
        travel(root,1,result);
        
        vector<vector<int> > result_;
        
        while(!result.empty()){
            result_.push_back(result[result.size()-1]);
            result.pop_back();
        }
        
        return result_;
    //    return result;
    }
};