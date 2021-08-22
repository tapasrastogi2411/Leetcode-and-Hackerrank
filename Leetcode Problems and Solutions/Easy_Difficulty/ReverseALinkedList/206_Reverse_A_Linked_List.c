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

// The main function to implement
struct ListNode* reverseList(struct ListNode* head){

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
    result = reverseList(head1);

    printList(result);

}
