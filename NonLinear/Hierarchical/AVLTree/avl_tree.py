# AVL Tree is a balanced Binary Search Tree

# AVL Tree Node class
class Node:
    def __init__(self, key):
        # Initialize a node with key, height, and left/right child as None
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # New node is initially added at leaf (height=1)

# AVL Tree class
class AVLTree:

    # Helper function to get the height of the node
    # Time complexity: O(1)
    # Reason: Accessing the height is a direct property lookup and takes constant time.
    def get_height(self, node):
        if not node:
            return 0  # If node is None, height is 0
        return node.height  # Otherwise return node's height

    # Helper function to get the balance factor of the node
    # Time complexity: O(1)
    # Reason: This function just computes the difference in heights of left and right children, which are both accessed in constant time.
    def get_balance(self, node):
        if not node:
            return 0  # Balance factor of None node is 0
        # Balance factor is height of left subtree - height of right subtree
        return self.get_height(node.left) - self.get_height(node.right)

    # Function to perform right rotation
    # Time complexity: O(1)
    # Reason: Rotations in AVL trees involve a constant number of pointer updates and height recalculations, all done in constant time.
    def right_rotate(self, y):
        x = y.left  # x becomes the new root of the subtree
        T2 = x.right  # T2 is the subtree between x and y

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights after rotation
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        # Return the new root
        return x

    # Function to perform left rotation
    # Time complexity: O(1)
    # Reason: Like the right rotation, a left rotation involves constant-time pointer updates and height recalculations.
    def left_rotate(self, x):
        y = x.right  # y becomes the new root of the subtree
        T2 = y.left  # T2 is the subtree between x and y

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights after rotation
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        # Return the new root
        return y

    # Function to insert a node in the AVL tree
    # Time complexity: O(log n)
    # Reason: Insertion in a binary search tree takes O(log n) time in a balanced tree because we only visit one path from root to leaf.
    # After insertion, we perform at most O(1) rotations, each of which takes O(1) time. Hence, overall time is O(log n).
    def insert(self, root, key):
        # Perform standard BST insert
        if not root:
            return Node(key)  # If root is None, create a new node with the key

        if key < root.key:
            root.left = self.insert(root.left, key)  # Insert in left subtree
        elif key > root.key:
            root.right = self.insert(root.right, key)  # Insert in right subtree
        else:
            return root  # Duplicate keys not allowed, return the root unchanged

        # Update height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor to check if node is unbalanced
        balance = self.get_balance(root)

        # Left Left Case (LL Rotation)
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case (RR Rotation)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case (LR Rotation)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case (RL Rotation)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        # Return the (unchanged) root pointer
        return root

    # Function to get the node with minimum key value found in the tree
    # Time complexity: O(log n)
    # Reason: This function traverses down the leftmost path of the tree, which in a balanced tree takes O(log n) time.
    def get_min_value_node(self, node):
        if node is None or node.left is None:
            return node  # Node with no left child is the smallest
        return self.get_min_value_node(node.left)  # Recursively find the minimum value node

    # Function to delete a node from the AVL tree
    # Time complexity: O(log n)
    # Reason: Deletion involves a search for the node, which takes O(log n) in a balanced tree.
    # After the deletion, at most O(1) rotations are needed at each level up the tree, so the total complexity is O(log n).
    def delete(self, root, key):
        # Perform standard BST delete
        if not root:
            return root  # If root is None, return None

        if key < root.key:
            root.left = self.delete(root.left, key)  # Recur in left subtree
        elif key > root.key:
            root.right = self.delete(root.right, key)  # Recur in right subtree
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: get the inorder successor (smallest in the right subtree)
            temp = self.get_min_value_node(root.right)
            root.key = temp.key  # Copy inorder successor's value to this node
            root.right = self.delete(root.right, temp.key)  # Delete the inorder successor

        if root is None:
            return root  # If the tree had only one node, return None

        # Update height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor of the node to check if it is unbalanced
        balance = self.get_balance(root)

        # Left Left Case (LL Rotation)
        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left Right Case (LR Rotation)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Right Case (RR Rotation)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)

        # Right Left Case (RL Rotation)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Function to perform an in-order traversal of the tree (sorted order)
    # Time complexity: O(n)
    # Reason: In-order traversal visits every node in the tree exactly once, so its time complexity is proportional to the number of nodes, i.e., O(n).
    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)  # Traverse left subtree
            res.append(root.key)  # Visit the node
            res = res + self.inorder_traversal(root.right)  # Traverse right subtree
        return res

        # Function for pre-order traversal
        # Pre-order: root -> left -> right
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.key)  # Visit root first
            res = res + self.preorder_traversal(root.left)  # Then traverse left subtree
            res = res + self.preorder_traversal(root.right)  # Then traverse right subtree
        return res

    # Function for post-order traversal
    # Post-order: left -> right -> root
    def postorder_traversal(self, root):
        res = []
        if root:
            res = self.postorder_traversal(root.left)  # Traverse left subtree first
            res = res + self.postorder_traversal(root.right)  # Then traverse right subtree
            res.append(root.key)  # Visit root last
        return res