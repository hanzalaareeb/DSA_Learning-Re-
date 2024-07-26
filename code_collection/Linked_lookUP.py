# Node of a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, n, head, key):
        # Code here
        while head is not None:
            if head.data == key:
                return True
            head = head.next
        return False

# Example usage:
# Creating a linked list with 3 nodes.
linked_list = Node(1)
linked_list.next = Node(2)
linked_list.next.next = Node(3)

# Create a Solution object and use the searchKey method
solution = Solution()
key_to_search = 2
print(solution.searchKey(3, linked_list, key_to_search))  # Output should be True
