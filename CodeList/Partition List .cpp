/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

//思路是先准备两个链表，一个存比partition小的值，small，一个存比partition大的值，large，最后把他们连起来即可，写的时候{1,2},2这个case一直过不了，一直说超时，后来看了评论才知道，需要把large的尾指针置null，不然最后结果是一个loop。
class Solution {
public:
    ListNode *partition(ListNode *head, int x) {
        
        ListNode *small=new ListNode(0),*large=new ListNode(0),*ptr=head;
        ListNode *sp=small;
        ListNode *lp=large;
    
         for(;ptr!=NULL;ptr=ptr->next){
             
             if(ptr->val<x){
              sp->next=ptr;
              sp=ptr;
             }
               
             else{
              lp->next=ptr;
              lp=ptr;
             }
         }
         
         sp->next=large->next;
         lp->next=NULL; 
 
      return small->next;       

  
        
    }
};