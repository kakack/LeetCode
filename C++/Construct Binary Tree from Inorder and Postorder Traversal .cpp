/*Construct Binary Tree from Inorder and Postorder Traversal 
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
 *
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * 
 * 跟之前的Inorder、Preorder的区别在于，后序序列postorder几乎是preorder的逆序，上一个代码的思路还是能用
 */
class Solution {
public:
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) {
        
        TreeNode *root;
        
        if(inorder.size()!=postorder.size())
          return NULL;
          
        return BuildTree(inorder, 0, inorder.size()-1, postorder, 0, postorder.size()-1);
        
    }
    
    TreeNode *BuildTree(vector<int> &inorder, int inStart, int inEnd, vector<int> &postorder,int postStart, int postEnd){
        
        if(postStart>postEnd||inStart>inEnd)
           return NULL;
           
         TreeNode *root = new TreeNode(postorder[postEnd]);
         
         if(postStart==postEnd&&inStart==inEnd)
           return root;
         
         //又要在inorder里找root了
         int rootIndex;
         for(int i=inStart; i<=inEnd; i++)
            if(inorder[i]==postorder[postEnd]){
              rootIndex=i;
              break;    
            }
        
        int numLeft = rootIndex - inStart;      
        root->left = BuildTree(inorder, inStart, rootIndex-1, postorder, postStart, postStart+numLeft-1);
        root->right= BuildTree(inorder, rootIndex+1, inEnd, postorder, postStart+numLeft, postEnd-1);
        
        return root;
    }
};