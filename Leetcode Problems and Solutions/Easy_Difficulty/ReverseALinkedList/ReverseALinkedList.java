package Easy_Difficulty.ReverseALinkedList;

public class ReverseALinkedList {

    // Definition of a node of our linked list
    public static class ListNode {
        int val;
        ListNode next;
        
        // Constructor to create ListNodes in our driver code to test
        ListNode(){
        }

        ListNode(int val){
            this.val = val;
        }

        ListNode(int val, ListNode next){
            this.val = val;
            this.next = next;
        }
    }

    // A variable to instantiate a linkedList for the driver code
    public ListNode head1;

    // A method to print and view our linke list to see if the method works as expected
    public void printList(ListNode head){
        ListNode temp = head;

        while(temp != null){
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    // The main method to implement
    public ListNode reverseListIterative(ListNode head){

        // The comments explaining this code is in the C implementation of this problem :)

        ListNode previous = null;
        ListNode current = head;
        ListNode next;

        while(current != null){

            next = current.next;
            current.next = previous;
            
            previous = current;
            current = next;
        }

        return previous;
    }

    public ListNode reverseListRecursive(ListNode head){

        if(head == null || head.next == null){
            return head;
        }
        
        ListNode newHead = reverseListRecursive(head.next);
        
        ListNode temp = head.next;
        temp.next = head;
        head.next = null;
        
        return newHead;


    }

    public static void main(String[] args) {
        
        ReverseALinkedList linkedList = new ReverseALinkedList();

        linkedList.head1 = new ListNode(1);
        linkedList.head1.next = new ListNode(2);
        linkedList.head1.next.next = new ListNode(3);
        linkedList.head1.next.next.next = new ListNode(4);
        linkedList.head1.next.next.next.next = new ListNode(5);
        
        ListNode result = linkedList.reverseListRecursive(linkedList.head1);

        linkedList.printList(result);

    }

    
}