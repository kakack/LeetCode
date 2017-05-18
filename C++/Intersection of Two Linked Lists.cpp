/*Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

因为没有环，所以先算出A、B的长度，取差值dis，然后让较长的那个链表先往前走dis步，然后同时遍历，第一个到的相同的点就是要求的交汇点
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
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int lenA=0,lenB=0,dis;
        
        ListNode *pa=headA, *pb=headB;
        
        while(pa!=NULL){
            lenA++;
            pa=pa->next;
        }
        
        while(pb!=NULL){
            lenB++;
            pb=pb->next;
        }
        
        dis=lenA>=lenB?lenA-lenB:lenB-lenA;
        pa=headA;
        pb=headB;
        
        if(lenA>=lenB){
            while(dis--)
              pa=pa->next;
        }
        else
           while(dis--)
             pb=pb->next;
             
        while(pa!=pb){
            pa=pa->next;
            pb=pb->next;
        }     
        
        return pa;  
        
    }
};