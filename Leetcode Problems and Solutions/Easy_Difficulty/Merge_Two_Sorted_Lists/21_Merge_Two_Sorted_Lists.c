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

    // TODO: Implement this correctly
    return l1;
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

    printList(head1);
    
    
}


