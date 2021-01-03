/*
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include "vector"
using namespace std;

struct ListNode {
      int val;
      ListNode *next;
      ListNode(int x) : val(x), next(NULL) {}
 };

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode* preLess = new ListNode(0);
        ListNode* less = preLess;
        ListNode* preMore = new ListNode(0);
        ListNode* more = preMore;

        while (head != nullptr)
        {
            if (head->val < x) {
                less->next = head;
                less = less->next;
            } else {
                more->next = head;
                more = more->next; 
            }
            head = head->next;
        }
        less->next = preMore->next;
        more->next = nullptr;
        return preLess->next;
    }
};