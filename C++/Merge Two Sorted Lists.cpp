/*Merge Two Sorted Lists 
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
 *
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        if(l1==NULL)
          return l2;
        else if(l2==NULL)
          return l1;
        
        ListNode res(-1);
        ListNode *tmp = &res;//链表赋初值的办法，要掌握一下
        while(l1!=NULL&&l2!=NULL){
            if(l1->val<=l2->val){
                tmp->next = l1;
                l1 = l1->next;
            }
            else{
                tmp->next = l2;
                l2 = l2->next;
            }
            tmp = tmp->next;
        }
        
        if(l1!=NULL)
          tmp->next = l1;
        else if(l2!=NULL)
          tmp->next = l2;
        
        return res.next;
    }
};