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

public class LRUCache {

    // Definition of a doubly linked list node - where each node has two pointers, next and previous and the data field is key and value pairs 
    public static class doublyLinkedListNode{

        // The next and previous pointers for a node
        doublyLinkedListNode next;
        doublyLinkedListNode previous;

        // The data fields for the node - a key value pair
        int key;
        int value;
    }
    
    int LRUcapacity;

    // Initialize the LRU cache with positive size capacity.
    public LRUCache(int capacity) {

        this.LRUcapacity = capacity;
        
    }

    // Return the value of the key if the key exists, otherwise return -1.
    public int get(int key) {

        return 0;
        
    }
    
    // Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
    public void put(int key, int value) {
        
    }

    public static void main(String[] args) {
        
        // Instantiating and calling the LRUCache object
        LRUCache obj = new LRUCache(10);
        // int param_1 = obj.get(3);
        obj.put(4, 6);
    }
    
}
