/*Binary Tree Zigzag Level Order Traversal
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]

*
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
        if(level%2==1)   
          result[level-1].push_back(root->val);
        else
          result[level-1].insert(result[level-1].begin(),root->val);
        
        travel(root->left,level+1,result);
        travel(root->right,level+1,result);

        
    }
    
    vector<vector<int> > zigzagLevelOrder(TreeNode *root) {
        
        vector<vector<int> > result;
        
        travel(root, 1, result);
        
        return result;
        
    }
};