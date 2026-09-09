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
             ListNode* removeNthFromEnd(ListNode* head, int n) {
                     // 1. Create a dummy node pointing to the head
                             ListNode* dummy = new ListNode(0, head);
                                     ListNode* fast = dummy;
                                             ListNode* slow = dummy;
                                                     
                                                             // 2. Move the fast pointer n steps ahead
                                                                     for (int i = 0; i < n; ++i) {
                                                                                 fast = fast->next;
                                                                                         }
                                                                                                 
                                                                                                         // 3. Move both pointers together until fast reaches the last node
                                                                                                                 while (fast->next != nullptr) {
                                                                                                                             fast = fast->next;
                                                                                                                                         slow = slow->next;
                                                                                                                                                 }
                                                                                                                                                         
                                                                                                                                                                 // 4. slow->next is the node to be deleted.
                                                                                                                                                                         ListNode* nodeToDelete = slow->next;
                                                                                                                                                                                 slow->next = slow->next->next; // Bypass the node
                                                                                                                                                                                         
                                                                                                                                                                                                 delete nodeToDelete; // Free the memory
                                                                                                                                                                                                         
                                                                                                                                                                                                                 // 5. Get the actual head (handles cases where original head is deleted)
                                                                                                                                                                                                                         ListNode* newHead = dummy->next;
                                                                                                                                                                                                                                 delete dummy; // Free the dummy node memory
                                                                                                                                                                                                                                         
                                                                                                                                                                                                                                                 return newHead;
                                                                                                                                                                                                                                                     }
                                                                                                                                                                                                                                                     };
                                                                                                                                                                                                                                                     
