# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head == None or head.next == None:
            return
        slow = head
        fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow.next
        slow.next = None
        while(current):
            later = current.next
            current.next = prev
            prev = current 
            current = later
       
        slow = head
        dummy_head = ListNode(0)
        tail = dummy_head
        s1 = True
        while(slow and prev):
            if(s1):
                tail.next = slow
                slow = slow.next
                s1 = False
            else:
                tail.next = prev
                prev = prev.next
                s1 = True
            tail = tail.next
        tail.next = slow if slow else prev
        head = dummy_head.next
        return
            
        