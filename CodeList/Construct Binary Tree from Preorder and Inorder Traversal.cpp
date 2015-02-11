/*Construct Binary Tree from Preorder and Inorder Traversal
Given preorder and inorder traversal of a tree, construct the binary tree.

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

先在中序中找到成为root的节点（也就是当前先序的第一个节点），然后其前面的节点都是在左子树，后面的都是右子树，计算好个数后应用到前序序列，然后就能递归了
 */
class Solution {
public:
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
        
        TreeNode* root;
        
        if(preorder.size()!=inorder.size()) 
           return NULL;
        root = BuildTree(preorder,0,preorder.size()-1,inorder,0,inorder.size()-1);
        return root;
        
    }
    
    TreeNode *BuildTree(vector<int> &preorder, int preStart, int preEnd, vector<int> &inorder, int inStart, int inEnd){
        if(preStart>preEnd||inStart>inEnd)
          return NULL;
          
          TreeNode *root = new TreeNode(preorder[preStart]);
          
          if(preStart==preEnd&&inStart==inEnd)
             return root;
             
          //找到当前root在中序中的位置，这样之前的都丢到root左子树里，之后的都丢到root右子树里
          
          int rootIndex;
          
          for(int i=inStart;i<=inEnd;i++)
            if(inorder[i]==preorder[preStart])
              rootIndex=i;
              
          int numLeft = rootIndex - inStart;
          
          root->left = BuildTree(preorder,preStart+1,preStart+numLeft,inorder,inStart,rootIndex-1);
          
          root->right = BuildTree(preorder,preStart+numLeft+1,preEnd,inorder,rootIndex+1,inEnd);
          
          return root;
    }
};