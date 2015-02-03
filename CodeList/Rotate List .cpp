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
    ListNode *rotateRight(ListNode *head, int k) {
        
         if (head == nullptr || k == 0) return head;
        ListNode *ptr=head;
        int len=1;
        while(ptr->next!=NULL){
            len++;
            ptr=ptr->next;
        }//计算出总长度len
        
        k=len-k%len;//算出实际从左往右数的步数
        
        ptr->next=head;//首尾相连
        
        
        for(int i=0;i<k;i++)
          ptr=ptr->next;//再往后走k步
          
         head=ptr->next;
         ptr->next=NULL;
         return head;
        
        
    }
};