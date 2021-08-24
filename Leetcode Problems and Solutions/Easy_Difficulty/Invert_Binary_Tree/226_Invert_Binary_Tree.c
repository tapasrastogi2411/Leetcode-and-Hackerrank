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

void postOrderTraversalForInversion(struct TreeNode *root){
    
    // Base condition check if we reach a leaf node
    
    if(root == NULL){
        return;
    }
    
    // Traverse the left subtree
    postOrderTraversalForInversion(root -> left);
    
    // Traverse the right subtree
    postOrderTraversalForInversion(root -> right);
    
    // Swap the left and the right subtrees
    struct TreeNode *temp = NULL;
    temp = root -> left;
    root -> left = root -> right;
    root -> right = temp;
}

// The main method to implement
struct TreeNode* invertTreeMethod1(struct TreeNode* root){
    
    /* Do a post-order traversal of the tree and the root operation is where you switch the left
       and the right subtrees at a level, since that is what inverting a binary tree is
       Recall that a post-order traversal is left, right and then desired operation
       
       Inversion of a binary tree is basically when you visit a node you swap its left and right
       child nodes
       
       We do a post-order traversal since we have to begin swapping the left and the right child
       from the bottom of the binary tree all the way to the up, which is something that
       postorder traversal achieves */
    
    postOrderTraversalForInversion(root);
    
    // The root remains unchanged when you invert a binary tree
    return root; 
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

    postOrderTraveral(root);
    printf("\n");
    root = invertTreeMethod1(root);

    postOrderTraveral(root);
    printf("\n");

}