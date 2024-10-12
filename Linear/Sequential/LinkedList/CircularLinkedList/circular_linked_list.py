# Node class represents a single element in a circular linked list.
class Node:
    def __init__(self, data=None):
        self.data = data  # 'data' stores the value of the node
        self.next = None  # 'next' is a reference to the next node in the list

# CircularLinkedList class manages the circular linked list and supports various operations.
class CircularLinkedList:
    def __init__(self):
        self.head = None  # 'head' points to the first node in the list
        self.tail = None  # 'tail' points to the last node in the list

    # Time Complexity: O(n)
    # Prints the circular linked list
    def print_list(self):
        if self.head is None:  # If the list is empty
            print("Circular linked list is empty")
            return

        itr = self.head  # Start from the head
        llstr = ''  # To build the string representation
        while True:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
            if itr == self.head:  # Stop when we loop back to the head
                break
        print(llstr)

    # Time Complexity: O(n)
    # Returns the number of nodes in the list
    def get_length(self):
        if self.head is None:
            return 0  # If the list is empty

        count = 1  # Start with 1 to count the head
        itr = self.head.next  # Start from the node after head
        while itr != self.head:
            count += 1
            itr = itr.next
        return count

    # Time Complexity: O(1)
    # Inserts a new node at the beginning of the list
    def insert_at_beginning(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node  # If the list is empty, set head to new node
            self.tail = node  # Set tail to new node
            node.next = node  # Point the new node to itself
        else:
            node.next = self.head  # Link new node to the current head
            self.tail.next = node  # Update the current tail to point to the new node
            self.head = node  # Update head to the new node

    # Time Complexity: O(1)
    # Inserts a new node at the end of the list
    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node  # If the list is empty, set head to new node
            self.tail = node  # Set tail to new node
            node.next = node  # Point the new node to itself
        else:
            self.tail.next = node  # Link current tail to the new node
            node.next = self.head  # Link new node to the head
            self.tail = node  # Update the tail to the new node

    # Time Complexity: O(1)
    # Removes the node at the beginning of the list
    def remove_at_beginning(self):
        if self.head is None:
            raise Exception("List is empty")  # Raise exception if the list is empty

        if self.head == self.tail:  # If there's only one node
            self.head = None  # Set head to None
            self.tail = None  # Set tail to None
        else:
            self.tail.next = self.head.next  # Update tail to skip the head
            self.head = self.head.next  # Update head to the next node

    # Time Complexity: O(n)
    # Removes the node at the end of the list
    def remove_at_end(self):
        if self.head is None:
            raise Exception("List is empty")  # Raise exception if the list is empty

        if self.head == self.tail:  # If there's only one node
            self.head = None  # Set head to None
            self.tail = None  # Set tail to None
        else:
            itr = self.head
            while itr.next != self.tail:  # Find the second to last node
                itr = itr.next
            itr.next = self.head  # Update the second to last node to point to head
            self.tail = itr  # Update the tail to the second to last node

    # Time Complexity: O(n)
    # Converts the circular linked list to a Python list (array)
    def convert_to_array(self):
        array = []
        if self.head is None:
            return array  # Return empty array if the list is empty

        itr = self.head
        while True:
            array.append(itr.data)  # Append each node's data to the array
            itr = itr.next
            if itr == self.head:  # Stop when we loop back to the head
                break
        return array  # Return the final array representation of the circular linked list

    # Time Complexity: O(kn)
    # Inserts multiple values from a list into the circular linked list (each element at the end)
    def insert_values(self, data_list):
        self.head = None  # Reset the linked list (make it empty)
        self.tail = None  # Reset the tail
        for data in data_list:  # Iterate through each element in the data_list
            self.insert_at_end(data)  # Insert each element at the end of the circular linked list
