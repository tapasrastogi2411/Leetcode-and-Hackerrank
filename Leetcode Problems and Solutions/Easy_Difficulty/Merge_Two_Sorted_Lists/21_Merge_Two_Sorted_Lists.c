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

    // Initialising the head of the new merged linked list
    struct ListNode *mergedHead = initialiser(0);

    // Using a dummy temporary listnode for building the merged list
    struct ListNode *dummy = mergedHead;
    
    // We loop through the l1, l2 and merged lists till either one the l1 or l2 lists becomes empty
    while(l1 != NULL && l2 != NULL){
        
        // If the value we are is smaller at l1 than l2, we create a node with the l1_val and add to the merged list
        if(l1 -> val < l2 -> val){
            
            // The value that we will add to mergedHead is the value at l1
            struct ListNode *newMergedNode = initialiser(l1 -> val);

            // Connecting this newly created node to our merged list
            dummy -> next = newMergedNode; // Instead of this, we just do a dummy -> next = l1
            
            // Moving along in the l1 list. A condition necessary for termination
            l1 = l1 -> next;
        
        }
        
        // The second case: When the value at l2 is smaller than the corresponding value in l1
        else {
            
            // Create a new node with l2_val to be added to our merged list
            struct ListNode *newMergedNode = initialiser(l2 -> val);

            // Add this node to the merged list
            dummy -> next = newMergedNode; // Instead of this, we can just do a dummy -> next = l2
            
            // Move along to the next node in the l2 list
            l2 = l2 -> next;
        }
        
        // Move along in the merged list after one node has been added
        dummy = dummy -> next;
            
        }
    
    // There are two ways for the above while loop to terminate. Either l1 is empty or l2 is empty

    // If l1 is empty, then we add the remaining of the l2 list to our merged list
    if(l1 == NULL){
        
        dummy -> next = l2;
    }
    
    // If l2 is empty, we add the remaining of the l1 list to the end of our merged list
    if(l2 == NULL){
        dummy -> next = l1;
    }

    // Recall how we created dummy ListNode only to reference the whole merged linked list at the end. mergedHead -> next is what starts the beginning of the dummy list, which actually is our final merged list
    return mergedHead -> next;
    
}

// Implementing a recursive method to this problem
struct ListNode *mergeTwoListsRecursive(struct ListNode * l1, struct ListNode *l2){

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


