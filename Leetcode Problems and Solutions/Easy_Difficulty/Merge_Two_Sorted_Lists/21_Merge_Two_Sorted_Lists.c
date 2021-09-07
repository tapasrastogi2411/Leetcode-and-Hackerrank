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
