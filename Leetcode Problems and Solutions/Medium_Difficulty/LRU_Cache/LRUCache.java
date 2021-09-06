/*
# Link to Problem: https://leetcode.com/problems/lru-cache/
# Difficulty - Medium

# Leetcode Problem number 146: LRU Cache: Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class with the following methods:

LRU Cache(int capacity)
int get(int key) 
void put(int key, int value)

The functions get and put must each run in O(1) average time complexity.
*/

/*
Thought Process for implementing an LRU Cache
- Use a hashmap and a doubly linked list for this question for the following reason - Hashmap will store the key and the address of the key in the doubly linked list as a value. Doubly Linked List is for maintaining that we always know the position of the least recently used key-value pair */
package Medium_Difficulty.LRU_Cache;

import java.util.HashMap;

public class LRUCache {

    // Definition of a doubly linked list node - where each node has two pointers, next and previous and the data field is key and value pairs 
    public static class doublyLinkedListNode{

        // The next and previous pointers for a node
        doublyLinkedListNode next;
        doublyLinkedListNode previous;

        // The data fields for the node - a key value pair
        int key;
        int value;

        // A constructor which makes new DLL nodes using the key and value integers

        public doublyLinkedListNode(int givenKey, int givenValue){

            this.key = givenKey;
            this.value = givenValue;   
    }

}
    
    // Defining the static variables that will is a part of any LRUCache Object

    int LRUcapacity;

    // The head and tail of the doubly LinkedList
    doublyLinkedListNode head = new doublyLinkedListNode(0, 0);
    doublyLinkedListNode tail = new doublyLinkedListNode(0, 0);

    // A hashmap to store the key-address pairs of keys that are put in the cache
    HashMap<Integer, doublyLinkedListNode> mapping = new HashMap<>();


    // Initialize the LRU cache with positive size capacity along with the head and tail of the doubly LinkedList.
    public LRUCache(int capacity) {

        this.LRUcapacity = capacity;

        // Connecting the head and tail of the DLL together as an LRU is initialised for the first time
        head.next = tail;
        tail.previous = head;
    }

    // Return the value of the key if the key exists, otherwise return -1.
    public int get(int key) {

        return 0;
        
    }
    
    // Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    public void put(int key, int value) {
        
    }

    // A method to add a node at the head of a doubly linked list - to be used in get() and put() method
    public void insertAthead(doublyLinkedListNode nodeToInsert){

        // Setting up the next pointer link of the nodeToInsert

        // Making the next pointer of the nodeToInsert point to what is pointed to at by head, since this node comes up immediately after head
        nodeToInsert.next = head.next;

        // Making the previous pointer of the node to the right of nodeToInsert, to point to nodeToinsert
        nodeToInsert.next.previous = nodeToInsert;

        // Setting up the previous pointer link of the nodeToInsert

        // Setting up the previous pointer link to nodeToInsert to point to head
        nodeToInsert.previous = head;

        // Making the next pointer of head point to nodeToInsert
        head.next = nodeToInsert;
    }

    // A method to delete a node from a doubly Linked List:
    public void deleteNode(doublyLinkedListNode nodeToDelete){
        
        // Setting the next pointer of the node to the left of nodeTdelete to point to the node after nodeToDelete
        nodeToDelete.previous.next = nodeToDelete.next;

        // Setting the previous pointer of the node to the right of nodeToDelete to the node before nodeToDelete
        nodeToDelete.next.previous = nodeToDelete.previous;

        // Remove the key-node pair from the hashmap since it no longer is needed
        mapping.remove(nodeToDelete.key);
    }

    public static void main(String[] args) {
        
        // Instantiating and calling the LRUCache object
        LRUCache obj = new LRUCache(10);
        // int param_1 = obj.get(3);
        obj.put(4, 6);
    }
    
}
