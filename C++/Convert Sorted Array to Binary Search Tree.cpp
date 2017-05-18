/*Convert Sorted Array to Binary Search Tree
 *Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
 *
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };

RandomAccessIterator真是容器中的神器，请务必要会用，这个题没啥难度，也是递归
 */
class Solution {
public:
    TreeNode *sortedArrayToBST(vector<int> &num) {
        
        return sortedArrayToBST(num.begin(), num.end());
        
    }
    
    template<typename RandomAccessIterator>
    
    TreeNode *sortedArrayToBST(RandomAccessIterator first, RandomAccessIterator last){
        const auto length = distance(first, last);
        if(length==0) return NULL;
        if (length == 1) return new TreeNode(*first);
        
        auto mid = first + length / 2;
        TreeNode* root = new TreeNode (*mid); 
        root->left = sortedArrayToBST(first, mid); 
        root->right = sortedArrayToBST(mid + 1, last);
        
        return root;
    }
};