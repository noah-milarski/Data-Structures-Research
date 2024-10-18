# Node class represents a single element in a linked list.
class Node:
    def __init__(self, data, next):
        self.data = data  # 'data' stores the value of the node
        self.next = next  # 'next' is a reference to the next node in the list

# LinkedList class manages the linked list and supports various operations.
class LinkedList:
    def __init__(self):
        self.head = None  # 'head' points to the first node in the list. Initially, the list is empty, so it's None.
        self.tail = None  # 'tail' points to the last node in the list. Initially, the list is empty, so it's None.

        # Prints the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    # Returns the number of nodes in the linked list
    def get_length(self):
        count = 0  # Initialize a counter.
        itr = self.head  # Start from the head of the list.
        while itr:  # Loop until 'itr' becomes None (end of the list).
            count += 1  # Increment the count for each node.
            itr = itr.next  # Move to the next node.
        return count  # Return the total number of nodes.

    # Inserts a new node at the beginning of the linked list
    # Time Complexity: O(1) - Insertion at the beginning is constant time since we only update the head pointer.
    def insert_at_beginning(self, data):
        node = Node(data, self.head)  # Create a new node with 'data', and its 'next' points to the current head.
        self.head = node  # Update the head to point to the new node, making it the first node in the list.

        # If the list was empty, then head and tail are the same node.
        if self.tail is None:
            self.tail = self.head

    # Inserts a new node at the end of the linked list
    # Time Complexity: O(1) - we reference the last node
    def insert_at_end(self, data):
        if self.head is None:  # If the list is empty, set the new node as the head.
            self.head = Node(data, None)  # The new node has 'data' and 'next' is None since it's the only node.
            self.tail = self.head  # Set tail to the head since there's only one node.
            return

            # Using the tail to insert at the end in O(1) time.
        self.tail.next = Node(data, None)  # Insert the new node after the current tail.
        self.tail = self.tail.next  # Update the tail to point to the new last node.

    # Inserts multiple values from a list into the linked list (each element at the end)
    # Time Complexity: O(kn) - Where k is the length of the data_list and n is the length of the linked list. Inserting each element is O(n), and it's repeated k times.
    def insert_values(self, data_list):
        self.head = None  # Reset the linked list (make it empty).
        self.tail = None  # Reset the tail as well.
        for data in data_list:  # Iterate through each element in the data_list.
            self.insert_at_end(data)  # Insert each element at the end of the linked list.

    # Removes the node at a specific index (0-based index)
    # Time Complexity: O(n) - In the worst case, we may need to traverse the entire list to remove the node at index n-1.
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():  # Check if the index is valid.
            raise Exception("Invalid Index")  # Raise an exception if the index is out of bounds.

        if index == 0:  # If the index is 0, remove the head node.
            self.head = self.head.next  # Make the second node (head.next) the new head.
            return  # Exit after removing the node.

        count = 0  # Initialize a counter.
        itr = self.head  # Start from the head of the list.
        while itr:  # Loop through the list.
            if count == index - 1:  # Stop at the node just before the node to be removed.
                itr.next = itr.next.next  # Remove the target node by bypassing it.
                break  # Exit the loop after removing the node.
            itr = itr.next  # Move to the next node.
            count += 1  # Increment the counter.

    # Inserts a new node at a specific index (0-based index)
    # Time Complexity: O(n) - In the worst case, we need to traverse the entire list to reach index n.
    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():  # Check if the index is valid.
            raise Exception("Invalid Index")  # Raise an exception if the index is out of bounds.

        if index == 0:  # If the index is 0, insert at the beginning.
            self.insert_at_beginning(data)  # Use the existing insert_at_beginning method.
            return  # Exit after inserting the node.

        count = 0  # Initialize a counter.
        itr = self.head  # Start from the head of the list.
        while itr:  # Loop through the list.
            if count == index - 1:  # Stop at the node just before the desired index.
                node = Node(data, itr.next)  # Create a new node with 'data'.
                itr.next = node  # Link the previous node (at index-1) to the new node.
                break  # Exit the loop after inserting the node.
            itr = itr.next  # Move to the next node.
            count += 1  # Increment the counter.

    # Method to insert a new node with 'data_to_insert' after the first occurrence of 'data_after'
    # Time Complexity: O(n) - We may need to traverse the entire list to find 'data_after'.
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:  # If the list is empty, no insertion can happen
            return

        if self.head.data == data_after:  # If the head node contains 'data_after'
            # Insert the new node right after the head node
            self.head.next = Node(data_to_insert, self.head.next)
            return  # Exit after inserting the node

        itr = self.head  # Start traversing the list from the head
        while itr:  # Continue traversing until the end of the list
            if itr.data == data_after:  # When the node with 'data_after' is found
                # Insert the new node after this node
                itr.next = Node(data_to_insert, itr.next)
                break  # Exit after insertion
            itr = itr.next  # Move to the next node

    # Method to remove the first occurrence of a node with the value 'data'
    # Time Complexity: O(n) - In the worst case, we need to traverse the entire list to find the node with 'data'.
    def remove_value(self, data):
        if self.head is None:  # If the list is empty, there's nothing to remove
            return

        if data == self.head.data:  # If the head node contains the value 'data'
            self.head = self.head.next  # Remove the head by making the second node the new head
            return  # Exit after removal

        itr = self.head  # Start traversing the list from the head
        while itr.next:  # Continue until the second-to-last node (because we check 'itr.next')
            if itr.next.data == data:  # If the next node contains 'data'
                itr.next = itr.next.next  # Bypass the node with 'data'
                break  # Exit after the node is removed
            itr = itr.next  # Move to the next node

    # Converts the linked list to a Python list (array) and prints it
    # Time Complexity: O(n) - We traverse the entire linked list to collect the values.
    def linked_list_to_array(self):
        itr = self.head  # Start from the head of the list.
        lista = []  # Initialize an empty list to store the node values.
        while itr:  # Loop through the linked list until itr becomes None (end of the list).
            lista.append(itr.data)  # Append the data of the current node to the list.
            itr = itr.next  # Move to the next node.
        print(lista)  # Print the list that contains the linked list values.

