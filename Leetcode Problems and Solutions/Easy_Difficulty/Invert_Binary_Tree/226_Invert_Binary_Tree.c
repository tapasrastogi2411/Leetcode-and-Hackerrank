/* Link to Problem: https://leetcode.com/problems/reverse-linked-list/
Difficulty - Easy

Leetcode Problem number 226: Invert a Binary Tree - Given the root of a binary tree, invert the tree, and return its root.

*/

#include <stdio.h>
#include <stdlib.h>

// Definition of a binary tree node

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

struct TreeNode *initialiser(int value){

    struct TreeNode *newNode = (struct TreeNode *)malloc(sizeof(struct TreeNode));
    newNode -> data = value;
    newNode -> left = NULL;
    newNode ->right = NULL;

    return  newNode;
}

void postOrderTraveral(struct TreeNode *root){

    if(root == NULL){
        return;
    }

    postOrderTraveral(root -> left);
    postOrderTraveral(root -> right);
    printf("%d ", root -> data);


}

void inOrdertraversal(struct TreeNode *root){

    if(root == NULL){
        return;
    }

    inOrdertraversal(root -> left);
    printf("%d ", root -> data);
    inOrdertraversal(root -> right);
}

struct TreeNode *insert(struct TreeNode *root, struct TreeNode *nodeToInsert){

    // Base case. This is the point where we will insert our node into the tree
    if(root == NULL){
        return nodeToInsert;
    }

    // Inserting into the right subtrees
    if(nodeToInsert -> data > root -> data){
        root -> right = insert(root -> right, nodeToInsert);
    }

    else if(nodeToInsert -> data < root -> data){
        root -> left =  insert(root -> left, nodeToInsert);
    }

    return root;
}


// The main method to implement
struct TreeNode *invertTree(struct TreeNode *root){

}

// The driver code to test the method
int main(){

    struct TreeNode *root = NULL;

    struct TreeNode *node1 = initialiser(4);
    struct TreeNode *node2 = initialiser(2);
    struct TreeNode *node3 = initialiser(7);
    struct TreeNode *node4 = initialiser(1);
    struct TreeNode *node5 = initialiser(3);
    struct TreeNode *node6 = initialiser(6);
    struct TreeNode *node7 = initialiser(9);

    root = insert(root, node1);
    root = insert(root, node2);
    root = insert(root, node3);
    root = insert(root, node4);
    root = insert(root, node5);
    root = insert(root, node6);
    root = insert(root, node7);

    // postOrderTraveral(root);
    inOrdertraversal(root);

    printf("\n");







}