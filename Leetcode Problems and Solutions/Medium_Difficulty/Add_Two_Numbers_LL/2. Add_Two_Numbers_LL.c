/* Link to Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
Difficulty - Medium

Leetcode Problem number 2: Add two numbers - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. */

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
struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{

    // Initialising a result node to store our added result in
    struct ListNode *result = initialiser(0);

    // Creating a temporary dummy node to hold the final results in
    struct ListNode *dummy = result;

    // Variables for carry over and the values of the two linked lists
    int carry = 0;
    int l1_val, l2_val;

    // We loop through each node of both the linked lists until either one of them is not empty
    while (l1 != NULL || l2 != NULL)
    {

        if (l1 != NULL)
        {   
            l1_val = l1->val;
        }

        else
        {
            l1_val = 0;
        }

        if (l2 != NULL)
        {
            l2_val = l2->val;
        }
        else
        {
            l2_val = 0;
        }
        
        // Calculating the sum, carry and the last digit for the addition
        int sum = carry + l1_val + l2_val;
        carry = sum / 10;
        int last_digit = sum % 10;

        // Adding the new node to our linked list
        dummy -> next = initialiser(last_digit);

        // Traversing to the next set of nodes to continue this process
        dummy = dummy -> next;

        if (l1 != NULL)
        {
            l1 = l1->next;
        }
        if (l2 != NULL)
        {
            l2 = l2->next;
        }
    }
    
    // For the one edge case where we have a carry over but both the lists have been exhausted: Eg: 8 + 7
    if(carry > 0){
        dummy -> next = initialiser(carry);
        dummy = dummy -> next;
    }

    return result -> next;
}

int main()
{
    struct ListNode *head1 = NULL;
    struct ListNode *head2 = NULL;

    struct ListNode *result = NULL;
    
    struct ListNode *head1Node1 = initialiser(2);
    struct ListNode *head1Node2 = initialiser(4);
    struct ListNode *head1Node3 = initialiser(3);

    struct ListNode *head2Node1 = initialiser(5);
    struct ListNode *head2Node2 = initialiser(6);
    struct ListNode *head2Node3 = initialiser(4);

    head1 = addAtHead(head1,head1Node3);
    head1 = addAtHead(head1, head1Node2);
    head1 = addAtHead(head1, head1Node1);
    
    head2 = addAtHead(head2, head2Node3);
    head2 = addAtHead(head2, head2Node2);
    head2 = addAtHead(head2, head2Node1);
    
    result = addTwoNumbers(head1, head2);

    printList(result);
    
    return 0;
}