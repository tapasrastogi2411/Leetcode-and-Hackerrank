/* Link to Problem: https://leetcode.com/problems/reverse-linked-list/
Difficulty - Easy

Leetcode Problem number 206: Reverse a Linked List - Given the head of a singly linked list, reverse the list, and return the reversed list.
*/

#include <stdio.h>
#include <stdlib.h>

//  Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

// Helper function to initialise a new ListNode
struct ListNode *initialiser(int val)
{

    struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
}

// Helper function to add a Node at the head of Linked List - to be used in driver code to test function
struct ListNode *addAtHead(struct ListNode *head, struct ListNode *nodeToInsert){
    nodeToInsert -> next = head;
    return nodeToInsert;

}

// Helper function to print a list to check if the output received is correct or not
void printList(struct ListNode *head){

    struct ListNode *temp = head;

    while(temp != NULL){

        printf("%d  ", temp -> val);
        temp = temp -> next;
    }

    printf("\n");
}

/* The main function to implement
Method 1 - Reversing a linked list iteratively */
struct ListNode* reverseListIterative(struct ListNode* head){

    // An image to visualise the position of the three pointers at a given time: https://user-images.githubusercontent.com/56613320/130348015-ebced701-6677-4255-b52f-f198c06519f7.png

    /* We need three pointers -> previous to keep track of the previous node and pointer, so that we can make the current node  
                                 point to the previous node in an attempt to reverse the linked list
                              -> current to keep track of the node we are at in the traversal
                              -> next to keep  track of the next node and its pointer so that we can move forward in the     
                                 traversal once we have reversed the connection
    
    */
    struct ListNode *previous = NULL; // Previous pointer starts from a NULL value
    struct ListNode *current = head; // Current pointer starts from the head, since that is the node we start from
    struct ListNode *next; // This will be updated in the traversal loop

    while(current != NULL){ // This means that we have already reached the end and reversed all the nodes

        // We make next point to current's next so that still have a connection to the next node before we break it to reverse the connection. Basically storing current -> next before we set it to previous
        next = current -> next;
        
        // We reverse the connection. We make the node that we are at, to point to the previous node
        current -> next = previous;

        // We update the pointers to move forward
        previous = current;
        current = next; // Recall that next stores information about next node after current

    }

    /* After the loop has finished, current is at NULL and previous points to the last node in the linked list. Therefore we can just return previous as the new head of our reversed linked list */

    return previous;
}

// Method 2 - Reversing a linked list recursively
struct ListNode *reverseListRecursive(struct ListNode *head){
    struct ListNode *result = initialiser(0);
    return result;
}

int main(){

    struct ListNode *head1 = NULL;

    struct ListNode *head1Node1 = initialiser(1);
    struct ListNode *head1Node2 = initialiser(2);
    struct ListNode *head1Node3 = initialiser(3);
    struct ListNode *head1Node4 = initialiser(4);
    struct ListNode *head1Node5 = initialiser(5);


    head1 = addAtHead(head1, head1Node5);
    head1 = addAtHead(head1, head1Node4);
    head1 = addAtHead(head1, head1Node3);
    head1 = addAtHead(head1, head1Node2);
    head1 = addAtHead(head1, head1Node1);

    struct ListNode *result = NULL;
    result = reverseListIterative(head1);

    printList(result);

}
