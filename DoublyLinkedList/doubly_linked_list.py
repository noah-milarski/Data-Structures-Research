# Node class represents a single element in a doubly linked list.
class Node:
    def __int__(self, data, next, previous):
        self.data = data  # 'data' stores the value of the node
        self.next = next  # 'next' is a reference to the next node in the list
        self.previous = previous  # 'previous' is a reference to the previous node in the list

# DoublyLinkedList class manages the doubly linked list and supports various operations.
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 'head' points to the first node in the list. Initially, the list is empty, so it's None.

    # Prints the linked list in forward order
    # Time Complexity: O(n) - We need to traverse all nodes in the list to print each element.
    def print_forward(self):
        if self.head is None:  # If the list is empty, print a message and return
            print("Linked list is empty")
            return

        itr = self.head  # Start from the head of the list
        llstr = ''  # Initialize an empty string to store the linked list elements
        while itr:  # Traverse through the list
            llstr += str(itr.data) + ' --> '  # Append each node's data to the string
            itr = itr.next  # Move to the next node
        print(llstr)  # Print the final string representation of the list

    # Prints the linked list in backward order
    # Time Complexity: O(n) - We need to traverse all nodes to reach the last node, then traverse back.
    def print_backward(self):
        if self.head is None:  # If the list is empty, print a message and return
            print("Linked list is empty")
            return

        last_node = self.get_last_node()  # Get the last node in the list
        itr = last_node  # Start from the last node
        llstr = ''  # Initialize an empty string to store the linked list elements
        while itr:  # Traverse the list in reverse
            llstr += itr.data + '-->'  # Append each node's data to the string
            itr = itr.prev  # Move to the previous node
        print("Link list in reverse: ", llstr)  # Print the final string representation of the list

    # Helper method to get the last node in the list
    # Time Complexity: O(n) - We need to traverse the entire list to find the last node.
    def get_last_node(self):
        itr = self.head  # Start from the head of the list
        while itr.next:  # Traverse the list until the last node
            itr = itr.next  # Move to the next node
        return itr  # Return the last node

    # Returns the number of nodes in the doubly linked list
    # Time Complexity: O(n) - We need to traverse the entire list to count the nodes.
    def get_length(self):
        count = 0  # Initialize a counter
        itr = self.head  # Start from the head of the list
        while itr:  # Loop through the list
            count += 1  # Increment the count for each node
            itr = itr.next  # Move to the next node
        return count  # Return the total number of nodes

    # Inserts a new node at the beginning of the doubly linked list
    # Time Complexity: O(1) - Inserting at the beginning only involves updating the head pointer.
    def insert_at_beginning(self, data):
        if self.head is None:  # If the list is empty, create the first node
            node = Node(data, self.head, None)  # Create a new node with 'data', 'next' as None, and 'previous' as None
            self.head = node  # Set the new node as the head
        else:
            node = Node(data, self.head, None)  # Create a new node with 'data' and the current head as 'next'
            self.head.previous = node  # Set the current head's 'previous' to the new node
            self.head = node  # Set the new node as the head

    # Inserts a new node at the end of the doubly linked list
    # Time Complexity: O(n) - We need to traverse the entire list to find the last node before insertion.
    def insert_at_end(self, data):
        if self.head is None:  # If the list is empty, set the new node as the head
            self.head = Node(data, None, None)  # Create a new node with 'data', 'next' as None, and 'previous' as None
            return  # Exit the function since we've inserted the node

        itr = self.head  # Start from the head of the list
        while itr.next:  # Traverse the list until the last node
            itr = itr.next  # Move to the next node

        itr.next = Node(data, None, itr)  # Create a new node at the end and set 'previous' to the last node

    # Inserts a new node at a specific index (0-based index)
    # Time Complexity: O(n) - In the worst case, we need to traverse the entire list to reach the index.
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():  # Check if the index is valid
            raise Exception("Invalid Index")  # Raise an exception if the index is out of bounds

        if index == 0:  # If the index is 0, insert at the beginning
            self.insert_at_beginning(data)  # Use the existing insert_at_beginning method
            return  # Exit after inserting the node

        count = 0  # Initialize a counter
        itr = self.head  # Start from the head of the list
        while itr:  # Loop through the list
            if count == index - 1:  # Stop at the node just before the desired index
                node = Node(data, itr.next, itr)  # Create a new node with 'data', 'next', and 'previous'
                if node.next:  # If the new node has a next node
                    node.next.previous = node  # Update the 'previous' reference of the next node
                itr.next = node  # Link the current node to the new node
                break  # Exit the loop after inserting the node

            itr = itr.next  # Move to the next node
            count += 1  # Increment the counter

    # Removes the node at a specific index (0-based index)
    # Time Complexity: O(n) - We may need to traverse the entire list to reach the node to be removed.
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():  # Check if the index is valid
            raise Exception("Invalid Index")  # Raise an exception if the index is out of bounds

        if index == 0:  # If the index is 0, remove the head node
            self.head = self.head.next  # Make the second node the new head
            self.head.prev = None  # Set the 'previous' reference of the new head to None
            return  # Exit after removing the node

        count = 0  # Initialize a counter
        itr = self.head  # Start from the head of the list
        while itr:  # Loop through the list
            if count == index:  # Stop at the node to be removed
                itr.prev.next = itr.next  # Bypass the node by linking the previous node to the next node
                if itr.next:  # If there's a next node
                    itr.next.prev = itr.prev  # Update the 'previous' reference of the next node
                break  # Exit the loop after removing the node

            itr = itr.next  # Move to the next node
            count += 1  # Increment the counter

    # Inserts multiple values from a list into the doubly linked list (each element at the end)
    # Time Complexity: O(kn) - Where k is the length of the data_list and n is the length of the linked list.
    # Each insertion requires traversing the list (O(n)), and it's repeated k times.
    def insert_values(self, data_list):
        self.head = None  # Reset the linked list (make it empty)
        for data in data_list:  # Iterate through each element in the data_list
            self.insert_at_end(data)  # Insert each element at the end of the linked list
