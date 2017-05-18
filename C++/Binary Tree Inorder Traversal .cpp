/*Binary Tree Inorder Traversal 


Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.


OJ's Binary Tree Serialization:
The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:
   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}".
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
    vector<int> inorderTraversal(TreeNode *root) {
        
        vector<int> v,v_left,v_right;
        
        if(root!=NULL){
         v_left=inorderTraversal(root->left);
         v_right=inorderTraversal(root->right);

         v.insert(v.end(),v_left.begin(),v_left.end());
                  
         v.push_back(root->val);
         
         v.insert(v.end(),v_right.begin(),v_right.end());
        }
        return v;
        
    }
};