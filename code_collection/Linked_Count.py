# Definition for singly-linked list node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        i = 0
        while head is not None:
            head = head.next
            i += 1
        return i

# Example usage:
# Creating a linked list with 3 nodes.
linked_list = LinkedList()
linked_list.head = Node(1)
second = Node(2)
third = Node(3)

linked_list.head.next = second
second.next = third

# Create a Solution object and use the getCount method
solution = Solution()
print(solution.getCount(linked_list.head))  # Output should be 3
