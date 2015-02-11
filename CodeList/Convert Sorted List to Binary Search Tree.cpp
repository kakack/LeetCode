/*Convert Sorted List to Binary Search Tree
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 * //List不能随机访问，所以这个办法是写一个按照index访问list的办法，以及计算List长度的办法，时间复杂度O(n^2)
 */
class Solution {
public:
    TreeNode *sortedListToBST(ListNode *head) {
        return sortedListToBST (head, listLength (head));
    }
    
    TreeNode *sortedListToBST (ListNode *head, int length){
        if(length==0) return NULL;
        if(length==1) return new TreeNode(head->val);
        
        TreeNode *root = new TreeNode(nth_node(head,length/2+1)->val);
        root->left = sortedListToBST(head, length/2);
        root->right= sortedListToBST(nth_node(head, length/2+2), (length-1)/2);
        
        return root;
    }
    
    int listLength(ListNode *node){
        
        int n=0;
        while(node){
            n++;
            node=node->next;
        }
        return n;
    }
    
    ListNode *nth_node(ListNode *node, int n){
        while(--n){//n==1，时候就可以return node了
          node=node->next;
        }
          
        return node;
    }
};