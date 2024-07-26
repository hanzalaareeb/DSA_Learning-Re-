class Node:
    def __init__(self, a) -> None:
        self.val = a
        self.next = None
class ListNode:
    def __init__(self):
        self.head = None
        self.tail = None

def countNodesinLoop(head):
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            length = 0
            current = slow
            while True:
                current = current.next
                length += 1
                if current == slow:
                    break
            return length
        
newList = ListNode()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(13)
node5 = Node(32)
node6 = Node(51)
node7 = Node(15)
node8 = Node(73)
node9 = Node(36)
node10 = Node(22)
node11 = Node(90)
node12 = Node(65)
node13 = Node(72)
node14 = Node(31)

newList.head = node1
newList.head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10
node10.next = node11
node11.next = node12
node12.next = node13
node13.next = node14
node14.next = node7

print(countNodesinLoop(newList.head))