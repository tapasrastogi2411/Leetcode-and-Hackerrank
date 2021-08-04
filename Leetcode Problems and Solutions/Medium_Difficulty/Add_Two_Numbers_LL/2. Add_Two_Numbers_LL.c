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


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    return;
}

int main()
{
    struct ListNode *node1 = NULL;
    struct ListNode *node2 = NULL;
    struct ListNode *nodeResult = NULL;

    nodeResult = addTwoNumbers(node1, node2);

    while(nodeResult != NULL){
        printf("%d ", nodeResult -> val);
        nodeResult = nodeResult -> next;
    }
    return 0;
}