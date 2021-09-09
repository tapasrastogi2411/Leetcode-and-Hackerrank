/*
Link to problem: https://leetcode.com/problems/merge-two-sorted-lists/
Difficulty level: Easy

Leetcode problem number 21: Merge Two Sorted Lists: Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists

*/

#include <stdio.h>
# include <stdlib.h>

struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode *initialiser(int nodeValue){

    struct ListNode *newNode = (struct ListNode *)calloc(1, sizeof(struct ListNode*));

    newNode -> val = nodeValue;
    newNode -> next = NULL;

    return newNode;
}

struct ListNode *printList(struct ListNode *head){

    struct ListNode *temp = head;

    while(temp != NULL){

        printf("%d ", temp -> val);
        temp = temp -> next;
    }

    printf("\n");
}

struct ListNode *addAtHead(struct ListNode *head, struct ListNode *nodeToAdd){

    // Making the next pointer of nodeToAdd point to head
    nodeToAdd -> next = head;

    // nodeToAdd is our new head, so we return that
    return nodeToAdd;
}

// The main method that we have to implement
struct ListNode *mergeTwoLists(struct ListNode *l1, struct ListNode *l2){

    struct ListNode *mergedHead = initialiser(0);
    struct ListNode *dummy = mergedHead;
    
    while(l1 != NULL && l2 != NULL){
        
        if(l1 -> val < l2 -> val){
            
            // The value that we will add to mergedHead is the value at l1
            struct ListNode *newMergedNode = initialiser(l1 -> val);
            dummy -> next = newMergedNode;
            
            l1 = l1 -> next;
        
        }
        
        
        else {
            
            struct ListNode *newMergedNode = initialiser(l2 -> val);
            dummy -> next = newMergedNode;
            
            l2 = l2 -> next;
        }
        
        dummy = dummy -> next;
            
        }
    
    
    if(l1 == NULL){
        
        dummy -> next = l2;
    }
    
    if(l2 == NULL){
        dummy -> next = l1;
    }

    return mergedHead -> next;
    
}


int main(){

    // Writing driver code to run and test our method

    // Creating the first linked list
    struct ListNode *head1 = NULL;

    struct ListNode *head1Node1 = initialiser(1);
    struct ListNode *head1Node2 = initialiser(2);
    struct ListNode *head1Node3 = initialiser(4);

    // Conecting these three nodes together
    head1 = addAtHead(head1, head1Node3);
    head1 = addAtHead(head1, head1Node2);
    head1 = addAtHead(head1, head1Node1);

    // Creating the second linked list
    struct ListNode *head2 = NULL;

    // Creating the nodes of the linked list
    struct ListNode *head2Node1 = initialiser(1);
    struct ListNode *head2Node2 = initialiser(3);
    struct ListNode *head2Node3 = initialiser(4);

    // Connecting these nodes together
    head2 = addAtHead(head2, head2Node3);
    head2 = addAtHead(head2, head2Node2);
    head2 = addAtHead(head2, head2Node1);

    // Calling the mergeTwoSortedLists method

    struct ListNode *mergedHead = NULL;

    mergedHead = mergeTwoLists(head1, head2);

    printList(mergedHead);
    
}


