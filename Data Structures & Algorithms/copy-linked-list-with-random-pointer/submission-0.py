"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return head
        elif head.next == None:
            copy = Node(0)
            copy.val = head.val
            if head.random:
                copy.random = copy
            return copy
        hash_map = {}
        i = 0
        cur = head
        while(head):
            hash_map[head] = i
            head = head.next
            i += 1
        copy = [Node(0) for _ in range(i)]
        for node in copy:
            node.val = cur.val
            if cur.next:
                node.next = copy[hash_map[cur.next]]
            if cur.random:
                node.random = copy[hash_map[cur.random]]
            cur = cur.next
        return copy[0]
