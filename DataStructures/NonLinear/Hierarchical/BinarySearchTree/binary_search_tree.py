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

        # New Method: Calculate the Depth of a node
        # Time Complexity: O(log n) on average, O(n) in the worst case (unbalanced tree)
        def get_depth(self, value, current_depth=0):
            # If the current node contains the value we're looking for, return the current depth
            if value == self.value:
                return current_depth
            # If the value is smaller, search in the left subtree and increment the depth
            elif value < self.value:
                # If there's no left child, return -1 (value not found)
                if self.left is None:
                    return -1  # Value not found
                # Otherwise, recursively search in the left subtree, increasing the depth by 1
                return self.left.get_depth(value, current_depth + 1)
            # If the value is greater, search in the right subtree and increment the depth
            else:
                # If there's no right child, return -1 (value not found)
                if self.right is None:
                    return -1  # Value not found
                # Otherwise, recursively search in the right subtree, increasing the depth by 1
                return self.right.get_depth(value, current_depth + 1)

        # New Method: Calculate the Height of the current node
        # Height is defined as the number of edges on the longest path from this node to a leaf.
        # Time Complexity: O(n) where n is the number of nodes (since every node is visited)
        def get_height(self):
            # If the node has no children, it is a leaf and has a height of 0.
            # For leaves, the height is -1 when we reach a None (non-existent) node.
            if self is None:
                return -1  # Base case for null node
            # Recursively calculate the height of the left and right subtrees
            left_height = self.left.get_height() if self.left else -1
            right_height = self.right.get_height() if self.right else -1
            # The height of the current node is the maximum height of its children + 1 (for this node)
            return max(left_height, right_height) + 1

        # Method to find the minimum value node in the tree (used in deletion)
        # Time Complexity: O(log n) on average, O(n) in worst case
        def find_min(self):
            current = self
            # Traverse to the leftmost node
            while current.left is not None:
                current = current.left
            return current

        # New Method: Delete a node from the Binary Search Tree
        # Handles three cases: leaf node, node with one child, node with two children.
        # Time Complexity: O(log n) on average, O(n) in the worst case (unbalanced tree)
        def delete(self, value):
            # If the value to be deleted is smaller than the root, look in the left subtree
            if value < self.value:
                if self.left:
                    self.left = self.left.delete(value)
            # If the value to be deleted is greater than the root, look in the right subtree
            elif value > self.value:
                if self.right:
                    self.right = self.right.delete(value)
            else:
                # Node to be deleted found
                # Case 1: Node has no children (leaf node)
                if self.left is None and self.right is None:
                    return None  # Return None to delete the node

                # Case 2: Node has only one child (either left or right)
                if self.left is None:  # If no left child, return right child
                    return self.right
                elif self.right is None:  # If no right child, return left child
                    return self.left

                # Case 3: Node has two children
                # Find the in-order successor (smallest value in the right subtree)
                min_right_subtree = self.right.find_min()
                # Replace the current node's value with the in-order successor's value
                self.value = min_right_subtree.value
                # Delete the in-order successor from the right subtree
                self.right = self.right.delete(min_right_subtree.value)

            return self  # Return the (possibly updated) root node

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
