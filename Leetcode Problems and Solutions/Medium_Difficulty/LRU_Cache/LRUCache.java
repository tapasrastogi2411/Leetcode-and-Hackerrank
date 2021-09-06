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

import jdk.internal.jimage.ImageReader.Node;

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

        // The main reason we decided to keep a hashmap is to help us in the get and put methods

        // If the hashmap has the key for which we are trying to get the value for, make it the LRU node, change its position in the doubly linked list by removing it from its position, inserting it at the head, and returning the value

        if(mapping.containsKey(key)){

            // Get the node pointed by this key first
            doublyLinkedListNode nodePointedbyKey = mapping.get(key);

            // Make the node pointed by this key at the beginning as mentioned above
            deleteNode(nodePointedbyKey);
            insertAthead(nodePointedbyKey);

            // Return the value for this key
            return nodePointedbyKey.value;

        }

        // Else there is no such key in the LRU cache, and we can return -1
        else{
            return -1;
        }
        
    }
    
    // Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    public void put(int key, int value) {

        // Case 1,: The key already exists in the mapping, so we have to update the value of the key

        if(mapping.containsKey(key)){

            // If the key already exists in the LRU cache, then remove it from doubly Linked List and insert a new one key-value pair with the updated value
            deleteNode(mapping.get(key));
            
            doublyLinkedListNode newNodeWithUpdtatedValues = new doublyLinkedListNode(key, value);
            insertAthead(newNodeWithUpdtatedValues);
        }

        // Case 2: If you are trying to put a key-value in the LRU but the capacity is already full, then remove the LRU node and insert the new key-value pair

        if(mapping.size() == LRUcapacity){

            // Remove the LRU node
            deleteNode(tail.previous);

            // Add the new key-value pair node to the LRU at the head

            doublyLinkedListNode newNodeToAdd = new doublyLinkedListNode(key, value);
            insertAthead(newNodeToAdd);
        }
        
    }

    // A method to add a node at the head of a doubly linked list - to be used in get() and put() method
    // An image depicting the process of inserting a DLL node at the head: https://user-images.githubusercontent.com/56613320/132157592-b571ad16-bbd0-40ce-9699-e89a8268edab.png
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

        // Dont forget to add this key-node pair to the hashmap, as our insert function also inserts the node to the doubly linked list and also puts key-node pairs into the hashmap
        mapping.put(nodeToInsert.key, nodeToInsert);
    }

    // A method to delete a node from a doubly Linked List: Link to visual image: https://user-images.githubusercontent.com/56613320/132157486-a82a841e-2aa5-4a66-a3fe-c2a541a71c76.png
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
