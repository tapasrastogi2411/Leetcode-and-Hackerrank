// Link to Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
// Difficulty - Medium

// Leetcode Problem number 2: Add two numbers - You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

#include <stdio.h>
#include <stdlib.h>

//  Definition for singly-linked list.
struct ListNode
{
    int val;
    struct ListNode *next;
};

struct ListNode *initialiser(int val)
{

    struct ListNode *newNode = (struct ListNode *)malloc(sizeof(struct ListNode));
    newNode->val = val;
    newNode->next = NULL;
}

struct ListNode *addAtHead(struct ListNode *head, struct ListNode *nodeToInsert){
    nodeToInsert -> next = head;
    return nodeToInsert;

}

void printList(struct ListNode *head){
    struct ListNode *temp = head;
    while(temp != NULL){
        printf("%d  ", temp -> val);
        temp = temp -> next;
    }
    printf("\n");
}

struct ListNode *addTwoNumbers(struct ListNode *l1, struct ListNode *l2)
{

    struct ListNode *result = initialiser(0);
    struct ListNode *dummy = result;

    int carry = 0;
    int l1_val, l2_val;

    
    printList(l1);
    printList(l2);
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

        int sum = carry + l1_val + l2_val;
            carry = sum / 10;
        int last_digit = sum % 10;


        dummy -> next = initialiser(last_digit);
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

    if(carry > 0){
        dummy -> next = initialiser(carry);
        dummy = dummy -> next;
    }

    return result -> next;
}

int main()
{
    return 0;
}