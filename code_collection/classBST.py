class Node:
    def __init__(self, data) -> None:
        self.val = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None
        
    def insert(self, x):
        if self.root is None:
            self.root = Node(x)
        else:
            self._insert(x, self.root)
        
    def _insert(self, x, node):
        if x < node.val:
            if node.left is None:
               node.left = Node(x)
            else:
                self._insert(x, node.left)
        else:
            if node.right is None:
                node.right = Node(x)
            else:
                self._insert(x, node.right)
        
    def search(self, value, node):
        if node is None:
            return False
        if value == node.val:
            return True
        elif value < node.val:
            return self.search(value, node.left)
        else:
            return self.search(value, node.right)
    
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder(self.root, "")

    def preorder(self, node, traversal):
        if node:
            traversal += (str(node.val) + "-> ")
            traversal = self.preorder(node.left, traversal)
            traversal = self.preorder(node.right, traversal)
        return traversal

    def inorder(self, node, traversal):
        if node:
            traversal = self.inorder(node.left, traversal)
            traversal += (str(node.val) + "-> ")
            traversal = self.inorder(node.right, traversal)
        return traversal

    def postorder(self, node, traversal):
        if node:
            traversal = self.postorder(node.left, traversal)
            traversal = self.postorder(node.right, traversal)
            traversal += (str(node.val) + "-> ")
        return traversal
            
        
newTree = BST()
newTree.insert(7)
newTree.insert(9)
newTree.insert(18)
newTree.insert(9)
newTree.insert(23)
newTree.insert(15)
print(newTree.print_tree('postorder'))