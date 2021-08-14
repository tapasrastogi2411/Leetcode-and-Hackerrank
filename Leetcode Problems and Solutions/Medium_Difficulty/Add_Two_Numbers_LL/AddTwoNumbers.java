public class AddTwoNumbers {    
    /**
     * InnerAddTwoNumbers
     */
    public static class ListNode {

        int val;
        ListNode next;

        ListNode(int value){
            this.val = value;
        }

        ListNode(int value, ListNode next){
            this.val = value;
            this.next = next;
        } 
    }

    public ListNode head1;
    public ListNode head2;

    public void printList(ListNode head){
        ListNode temp = head;

        while(temp != null){
            System.out.print(temp.val + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2){

        ListNode result = new ListNode(-1);
        ListNode dummy = result;

        int l1_val, l2_val;
        int carry = 0;

        while(l1 != null || l2 != null){

            if(l1 != null){
                l1_val = l1.val;
            }

            else{
                l1_val = 0;
            }

            if(l2 != null){
                l2_val = l2.val;
            }

            else {
                l2_val = 0;
            }

            int sum = carry + l1_val + l2_val;
            carry = sum / 10;

            int last_digit = sum % 10;

            ListNode temp = new ListNode(last_digit);
            dummy.next = temp;
            
            // Updating
            dummy = dummy.next;

            if(l1 != null){
                l1 = l1.next;
            }
            if(l2 != null){
                l2 = l2.next;
            }
        }

        if(carry > 0){
            ListNode temp = new ListNode(carry);
            dummy.next = temp;
        }

        return result.next;
    }
    public static void main(String[] args) {

        AddTwoNumbers linkedList = new AddTwoNumbers();

        linkedList.head1 = new ListNode(2);
        linkedList.head1.next = new ListNode(4);
        linkedList.head1.next.next = new ListNode(3);

        linkedList.head2 = new ListNode(5);
        linkedList.head2.next = new ListNode(6);
        linkedList.head2.next.next = new ListNode(4);

        ListNode result = linkedList.addTwoNumbers(linkedList.head1, linkedList.head2);

        linkedList.printList(result);





    }
    
}
