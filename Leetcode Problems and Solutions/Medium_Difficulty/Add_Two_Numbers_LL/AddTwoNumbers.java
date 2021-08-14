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

        return dummy.next;
    }
    public static void main(String[] args) {

    }
    
}
