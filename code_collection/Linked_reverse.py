class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # Base case: If the list is empty or has only one node
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        current = self.reverseList(head.next)
        
        # Reverse the current node
        front = head.next
        front.next = head
        head.next = None
        
        return current
