class StackList:
    def __init__(self):
        # Initialize an empty list to represent the stack
        self.stack = []

    def push(self, item):
        """Adds an item to the top of the stack.
        Time Complexity: O(1) - appending to the end of a list is a constant time operation.
        """
        self.stack.append(item)  # Append item to the end of the list (top of the stack)
        print(f"Pushed {item} onto stack")

    def pop(self):
        """Removes and returns the top item from the stack.
        Time Complexity: O(1) - removing the last element from the list is a constant time operation.
        """
        if not self.is_empty():  # Check if the stack is not empty
            popped_item = self.stack.pop()  # Remove and return the top element
            print(f"Popped {popped_item} from stack")
            return popped_item
        else:
            print("Stack is empty, cannot pop an element")
            return None

    def peek(self):
        """Returns the top item from the stack without removing it.
        Time Complexity: O(1) - accessing the last element is a constant time operation.
        """
        if not self.is_empty():  # Check if the stack is not empty
            top_item = self.stack[-1]  # Get the last element
            print(f"Top element is: {top_item}")
            return top_item
        else:
            print("Stack is empty, no element to peek")
            return None

    def is_empty(self):
        """Checks if the stack is empty.
        Time Complexity: O(1) - checking the length of a list is a constant time operation.
        """
        empty = len(self.stack) == 0  # Check if list length is zero
        print(f"Is stack empty? {empty}")
        return empty

    def size(self):
        """Returns the number of elements in the stack.
        Time Complexity: O(1) - getting the length of the list is a constant time operation.
        """
        size = len(self.stack)  # Get the number of elements in the stack
        print(f"Stack size is: {size}")
        return size

    def display(self):
        """Displays all the elements in the stack.
        Time Complexity: O(n) - iterating over the list to print each element.
        """
        print("Stack elements (top to bottom):")
        for item in reversed(self.stack):  # Display elements from top to bottom
            print(item)