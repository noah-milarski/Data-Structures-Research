class BinarySearchTree:
    # The constructor initializes the node with a given value,
    # and sets the left and right children to None.
    def __init__(self, value):
        self.value = value  # Set the value of the node
        self.left = None    # Left child of the node, initially None
        self.right = None   # Right child of the node, initially None

    # Time Complexity: O(log n) on average (balanced tree), O(n) in the worst case (unbalanced tree)
    # The insert method inserts a new value into the binary search tree.
    def insert(self, value):
        # If the value to insert is smaller than the current node's value, insert into the left subtree.
        if value < self.value:
            # If the left child is None, create a new node with the value.
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # Otherwise, recursively insert into the left subtree.
                self.left.insert(value)
        # If the value to insert is greater than or equal to the current node's value, insert into the right subtree.
        else:
            # If the right child is None, create a new node with the value.
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # Otherwise, recursively insert into the right subtree.
                self.right.insert(value)

    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # In-order traversal visits nodes in increasing order of value.
    def inorder_traversal(self):
        # Traverse the left subtree first.
        if self.left:
            self.left.inorder_traversal()
        # Print the current node's value (middle node in in-order traversal).
        print(self.value)
        # Traverse the right subtree after.
        if self.right:
            self.right.inorder_traversal()

    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Pre-order traversal visits the current node before its subtrees.
    def preorder_traversal(self):
        # Print the current node's value (root first in pre-order traversal).
        print(self.value)
        # Traverse the left subtree after printing the root.
        if self.left:
            self.left.preorder_traversal()
        # Then traverse the right subtree.
        if self.right:
            self.right.preorder_traversal()

    # Time Complexity: O(n), where n is the number of nodes in the tree.
    # Post-order traversal visits the subtrees before the current node.
    def postorder_traversal(self):
        # Traverse the left subtree first.
        if self.left:
            self.left.postorder_traversal()
        # Then traverse the right subtree.
        if self.right:
            self.right.postorder_traversal()
        # Print the current node's value (root last in post-order traversal).
        print(self.value)

    # Time Complexity: O(log n) on average (balanced tree), O(n) in the worst case (unbalanced tree)
    # The find method searches for a value in the binary search tree.
    def find(self, value):
        # If the value is smaller than the current node's value, search the left subtree.
        if value < self.value:
            # If there's no left child, the value is not in the tree, return False.
            if self.left is None:
                return False
            else:
                # Otherwise, recursively search the left subtree.
                return self.left.find(value)
        # If the value is greater than the current node's value, search the right subtree.
        elif self.value > value:
            # If there's no right child, the value is not in the tree, return False.
            if self.right is None:
                return False
            else:
                # Otherwise, recursively search the right subtree.
                self.right.find(value)
        else:
            # If the value matches the current node's value, return True.
            return True

    ''' 
    Example of inserting values into a Binary Search Tree
    
     Let's say we insert the following values in this order:
     50, 30, 70, 20, 40, 60, 80

     The resulting tree structure will look like this:

                50
              /    \
            30      70
           /  \    /  \
         20   40  60   80

     In this example:
     - The root node is 50.
     - Values smaller than 50 (like 30 and 20) go to the left.
     - Values greater than 50 (like 70, 60, and 80) go to the right.
     - For each node, the left subtree contains values smaller than the node, 
       and the right subtree contains values greater than or equal to the node.
    '''
