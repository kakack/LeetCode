/*
148. Sort List
Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-105 <= Node.val <= 105
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


using namespace std;
struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* sortList(ListNode* head) {
        return sortFunc(head, nullptr);
    }

    ListNode* sortFunc(ListNode* head, ListNode* tail) {
        if (head == nullptr) {
            return head;
        } else if (head->next == tail) {
            head->next = nullptr;
            return head;
        }
        ListNode* slow = head, *fast = head;
        while (fast != tail)
        {
            slow = slow->next;
            fast = fast->next;
            if(fast != tail) {
                fast = fast->next;
            }
        }
        ListNode* mid = slow;
        return mergeLists(sortFunc(head, mid), sortFunc(mid, tail));
    }

    ListNode* mergeLists(ListNode* head1, ListNode* head2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* tmp = dummyHead, *tmp1 = head1, *tmp2 = head2;
        while (tmp1 != nullptr && tmp2 != nullptr) {
            if (tmp1->val < tmp2->val) {
                tmp->next = tmp1;
                tmp1 = tmp1->next;
            } else {
                tmp->next =tmp2;
                tmp2 = tmp2->next;
            }
            tmp = tmp->next;            
        }
        if (tmp1 != nullptr) {
            tmp->next = tmp1;
        }
        else if (tmp2 != nullptr) {
            tmp->next = tmp2;
        }
    return dummyHead->next;
    }
};