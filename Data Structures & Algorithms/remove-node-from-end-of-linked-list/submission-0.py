# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            if n >= 0:
                return None
            return head
        slow = head
        fast = head
        count = 0
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            count += 1
        if fast:
            length = 2*count + 1
        else:
            length = 2*count
        n = n%length
        if n == 0:
            head = head.next
            return head
        slow = head
        for i in  range(length - n - 1):
            slow = slow.next
        slow.next = slow.next.next
        return head
        
        



        