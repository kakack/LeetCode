
/*

Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.

Note:
Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
//现在真是各种熟练写逆序链表，找到要逆序的部分和前后端衔接的部分即可，难度不大
class Solution {
public:
    ListNode *reverse(ListNode *head, int n){
        ListNode *pre=head,*pretail,*tail=head;
        
        for(int i=1;i<n;i++)
           tail=tail->next;
           
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

    ListNode *reverseBetween(ListNode *head, int m, int n) {
        
        ListNode *pr=head;
        
        if(m==n)
           return head;
           
        else if(m==1)
           return reverse(head, n);
           
           
        else{
            for(int i=1;i<m-1;i++)
              pr=pr->next;
              
             pr->next=reverse(pr->next,n-m+1);
             
             return head;
            
        }
        
    }
};