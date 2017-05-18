/*Path Sum II 
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
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
    vector<vector<int> > pathSum(TreeNode *root, int sum) {
        
        vector<vector<int> > result;
        vector<int> cur;//保存中间值
        
        pathSum(root, sum, cur, result);
        return result;
    }
    
    void pathSum(TreeNode *root, int sum, vector<int> &cur, vector<vector<int> > &result){
        if(root==NULL) return;
        
        cur.push_back(root->val);
        
        if(root->left==NULL&&root->right==NULL){
            if(root->val==sum)
              result.push_back(cur);
        }
        
        pathSum(root->left, sum-root->val, cur, result);
        pathSum(root->right, sum-root->val, cur, result);
        
        cur.pop_back();//该节点极其子节点都遍历过后就把它pop掉
    }
};