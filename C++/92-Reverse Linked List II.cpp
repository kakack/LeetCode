/*
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.



Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]


Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode *reverse(ListNode *head, int n){
        ListNode *pre=head,*pretail,*tail=head;
        for(int i=1;i<n;i++){
           tail=tail->next;
        }
        pretail=tail->next;
        while(pre!=tail){
            ListNode *tmp=pre->next;
            pre->next=pretail;
            pretail=pre;
            pre=tmp;
        }
        tail->next=pretail;
        return tail;
    }

    ListNode* reverseBetween(ListNode* head, int m, int n) {
        ListNode *pr=head;
        if(m==n){
           return head;
        } else if(m==1){
           return reverse(head, n);
        }
        else{
            for(int i=1;i<m-1;i++) {
                pr=pr->next;
             }
             pr->next=reverse(pr->next,n-m+1);
             return head;
        }
    }
};