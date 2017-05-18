/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

*/



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

//逻辑和算法很简单，只是操作链表的时候记得先new一个ListNode再去操作，然后不要破坏数组原有的形状，用一个新的指针去指向需要操作的数组的头部，然后操作指针来计算
class Solution {
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        int carry = 0;
        
        ListNode *ans = new ListNode(0);

        ListNode *p1=l1,*p2=l2,*curr=ans;
        
        while(p1!=NULL||p2!=NULL){
            int x=(p1!=NULL)?p1->val:0;
            int y=(p2!=NULL)?p2->val:0;
            int res=carry+x+y;
            carry=res/10;
            curr->next=new ListNode(res%10);
            curr=curr->next;
            
            if(p1!=NULL)
               p1 = p1->next;
            
            if(p2!=NULL)
               p2 = p2->next;
        }
        
        if(carry>0)
          curr->next = new ListNode(carry);
          
        return ans->next;

    }
    
};