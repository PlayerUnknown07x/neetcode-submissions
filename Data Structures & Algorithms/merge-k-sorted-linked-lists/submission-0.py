# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        
        # 2. Initialise the heap array
        min_heap = []
        counter = 0  # Crucial tie-breaker to prevent node comparison crashes
        
        # 3. Push the head node of every non-empty linked list into the heap
        for head_node in lists:
            if head_node:
                # Store: (node_value, unique_counter, node_object)
                heapq.heappush(min_heap, (head_node.val, counter, head_node))
                counter += 1
                
        # 4. Process the heap until it's completely empty
        while min_heap:
            # Pop the smallest element currently available
            val, _, node = heapq.heappop(min_heap)
            
            # Link our running tail pointer to this smallest node
            tail.next = node
            tail = tail.next  # Move our tail pointer forward
            
            # If this popped node has a next node, push that into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
                
        # 5. Return the true start of our freshly wired list
        return dummy.next