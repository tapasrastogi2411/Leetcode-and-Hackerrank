package Easy_Difficulty.ReverseALinkedList;

public class ReverseALinkedList {

    public static class ListNode {
        int val;
        ListNode next;

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

    public ListNode head1;

    public void printList(ListNode head){
        ListNode temp = head;

        while(temp != null){
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public ListNode reverseList(ListNode head){

        ListNode myNode = new ListNode(3, null);
        return myNode;
    }

    public static void main(String[] args) {
        
        ReverseALinkedList linkedList = new ReverseALinkedList();

        linkedList.head1 = new ListNode(1);
        linkedList.head1.next = new ListNode(2);
        linkedList.head1.next.next = new ListNode(3);
        linkedList.head1.next.next.next = new ListNode(4);
        linkedList.head1.next.next.next.next = new ListNode(5);

        ListNode result = linkedList.reverseList(linkedList.head1);

        linkedList.printList(result);

    }

    
}