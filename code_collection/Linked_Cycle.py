class Node:
    def __init__(self, a) -> None:
        self.val = a
        self.next = None
class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None

class CycleSearch:
    def hasCycle(self, head):
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next
        
        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True
        """
        1) This bellow solution works too
        
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False
        """
        
        
newLinked = ListNode()
newLinked.head = Node(1)
second = Node(5)
thired = Node(7)
last = Node(8)
newLinked.head.next = second
second.next = thired
thired.next = last
last.next = second # creating cycle.
search = CycleSearch()
print(search.hasCycle(newLinked.head))