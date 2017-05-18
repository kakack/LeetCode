/**Sum Root to Leaf Numbers
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.


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
    //int sum=0;
    int sumNumbers(TreeNode *root) {
        //先深度优先遍历，然后再加值
        
        return dfs(root, 0);
        
    }
    
    int dfs(TreeNode *root, int prev){
        
        if(root==NULL) return 0;
        
        if(root->left==NULL&&root->right==NULL)
          return prev*10+root->val;
        
        return dfs(root->left, prev*10+root->val)+dfs(root->right,prev*10+root->val);
    }
};