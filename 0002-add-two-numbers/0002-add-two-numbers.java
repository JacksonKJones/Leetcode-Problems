/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode hold = new ListNode(0);
        ListNode previous = hold;
        int carrier = 0;

        while (l1 != null || l2 != null || carrier != 0) {
            int n1 = (l1 != null) ? l1.val : 0;
            int n2 = (l2 != null) ? l2.val : 0;

            int sum = n1 + n2 + carrier;
            int digit = sum%10;
            carrier = sum/10;

            ListNode newNode = new ListNode(digit);
            previous.next = newNode;
            previous = previous.next;

            l1 = (l1 != null) ? l1.next : null;
            l2 = (l2 != null) ? l2.next : null;
        }

        ListNode result = hold.next;
        hold.next = null;
        return result;
    }
}