#include <stdio.h>
#include <stdlib.h>


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    // Result list-in thodakkathai kurikka oru dummy head node
    struct ListNode dummy;
    dummy.val = 0;
    dummy.next = NULL;
    
    struct ListNode* current = &dummy;
    int carry = 0;
    
    // l1, l2, or carry ethavathu onru irundhalum loop odum
    while (l1 != NULL || l2 != NULL || carry > 0) {
        int sum = carry;
        
        // l1 node irundhal athan val-ai kootti, adhutha node-ku chellavum
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }
        
        // l2 node irundhal athan val-ai kootti, adhutha node-ku chellavum
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }
        
        // Puthiya carry-ai kandupidikka (e.g., 12 / 10 = 1)
        carry = sum / 10;
        
        // Puthiya node-gatha memory allocate seithu, val-ai tharavum (e.g., 12 % 10 = 2)
        struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
        newNode->val = sum % 10;
        newNode->next = NULL;
        
        // Puthiya node-ai list-udan inaikkavum
        current->next = newNode;
        current = current->next;
    }
    
    // Dummy node-in adhutha node thaan unmaiyana result list-in head
    return dummy.next;
}
