# Node class represents a single element in a doubly linked list.
class Node:
    def __init__(self, data=None, next=None, previous=None):
        self.data = data  # 'data' stores the value of the node
        self.next = next  # 'next' is a reference to the next node in the list
        self.previous = previous  # 'previous' is a reference to the previous node in the list

# DoublyLinkedList class manages the doubly linked list and supports various operations.
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 'head' points to the first node in the list. Initially, the list is empty.
        self.tail = None  # 'tail' points to the last node in the list for efficient end operations.

    # Prints the linked list in forward order
    # Time Complexity: O(n)
    def print_forward(self):
        if self.head is None:  # If the list is empty
            print("Linked list is empty")
            return

        itr = self.head  # Start from the head
        llstr = ''  # To build the string representation
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    # Prints the linked list in backward order
    # Time Complexity: O(n)
    def print_backward(self):
        if self.tail is None:  # If the list is empty
            print("Linked list is empty")
            return

        itr = self.tail  # Start from the tail for reverse traversal
        llstr = ''  # To build the string representation
        while itr:
            llstr += str(itr.data) + ' <-- '
            itr = itr.previous
        print("Linked list in reverse: ", llstr)

    # Returns the number of nodes in the list
    # Time Complexity: O(n)
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    # Inserts a new node at the beginning of the list
    # Time Complexity: O(1)
    def insert_at_beginning(self, data):
        node = Node(data, self.head, None)  # Create a new node with 'previous' as None
        if self.head is None:
            self.head = self.tail = node  # If list is empty, head and tail are the same
        else:
            self.head.previous = node  # Update the previous pointer of the current head
            self.head = node  # Update head to the new node

    # Inserts a new node at the end of the list
    # Time Complexity: O(1)
    def insert_at_end(self, data):
        node = Node(data, None, self.tail)  # Create a new node with 'next' as None and 'previous' as the current tail
        if self.tail is None:
            self.head = self.tail = node  # If the list is empty, both head and tail point to the new node
        else:
            self.tail.next = node  # Update the next pointer of the current tail
            self.tail = node  # Update tail to the new node

    # Removes the node at the beginning of the list
    # Time Complexity: O(1)
    def remove_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")  # Raise exception if the list is empty

        if self.head == self.tail:  # If there's only one node
            self.head = self.tail = None  # Set both head and tail to None
        else:
            self.head = self.head.next  # Move the head to the second node
            self.head.previous = None  # Update the previous pointer of the new head

    # Removes the node at the end of the list
    # Time Complexity: O(1)
    def remove_at_end(self):
        if self.tail is None:
            raise Exception("List is empty")  # Raise exception if the list is empty

        if self.head == self.tail:  # If there's only one node
            self.head = self.tail = None  # Set both head and tail to None
        else:
            self.tail = self.tail.previous  # Move the tail pointer back to the previous node
            self.tail.next = None  # Set the next pointer of the new tail to None

    # Helper method to get the last node
    # Time Complexity: O(1)
    def get_last_node(self):
        return self.tail  # Return the tail, which is the last node in the list

    # Inserts a new node at a specific index
    # Time Complexity: O(n)
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        if index == self.get_length():
            self.insert_at_end(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)  # Create a new node with 'next' and 'previous' references
                if node.next:
                    node.next.previous = node  # Update the next node's previous pointer
                itr.next = node  # Insert the new node after the current node
                break
            itr = itr.next
            count += 1

    # Removes the node at a specific index
    # Time Complexity: O(n)
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.remove_at_beginning()  # Call the remove_at_beginning method
            return

        if index == self.get_length() - 1:
            self.remove_at_end()  # Call the remove_at_end method
            return

        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.previous.next = itr.next  # Bypass the node to be removed
                if itr.next:  # If it's not the last node, update the next node's previous pointer
                    itr.next.previous = itr.previous
                break
            itr = itr.next
            count += 1

    # Converts the linked list to a Python list (array)
    # Time Complexity: O(n)
    def convert_to_array(self):
        array = []
        itr = self.head
        while itr:
            array.append(itr.data)  # Append each node's data to the array
            itr = itr.next
        return array  # Return the final array representation of the linked list

    # Inserts multiple values from a list into the doubly linked list (each element at the end)
    # Time Complexity: O(kn) - Where k is the length of the data_list and n is the length of the linked list.
    def insert_values(self, data_list):
        self.head = self.tail = None  # Reset the linked list
        for data in data_list:
            self.insert_at_end(data)  # Insert each element at the end of the list
