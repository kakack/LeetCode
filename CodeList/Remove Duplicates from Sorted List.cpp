/*
Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
*/


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *deleteDuplicates(ListNode *head) {
        
        ListNode *p=head;
        
        while(p!=NULL&&p->next!=NULL){
            if(p->val==p->next->val)
               p->next=p->next->next;
               
            else
               p=p->next;
        }
        
        return head;
    }
};