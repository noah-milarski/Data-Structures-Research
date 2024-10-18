# Array class to demonstrate array operations and their complexities
class Array:
    def __init__(self):
        self.array = []  # Initialize an empty array (Python list)

    # Time Complexity: O(1) - Accessing an element by its index
    def access_element(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")  # Raise error if index is invalid
        return self.array[index]  # Return the element at the specified index

    # Time Complexity: O(n) - In the worst case, we traverse the entire array
    def search_element(self, value):
        for index, element in enumerate(self.array):
            if element == value:  # If element is found
                return index  # Return the index of the found element
        return -1  # If element is not found, return -1

    # Time Complexity: O(1) - Adding an element at the end of the array
    def insert_at_end(self, value):
        self.array.append(value)  # Append the value to the end of the array

    # Time Complexity: O(n) - Insertion in the middle requires shifting elements
    def insert_at_index(self, index, value):
        if index < 0 or index > len(self.array):
            raise IndexError("Index out of bounds")  # Raise error if index is invalid
        self.array.insert(index, value)  # Insert element at the specified index

    # Time Complexity: O(n) - Removing a specific element requires shifting elements
    def remove_element(self, value):
        if value in self.array:  # Check if value is in array
            self.array.remove(value)  # Remove the element by value

    # Time Complexity: O(1) - Removing an element by index
    def remove_at_index(self, index):
        if index < 0 or index >= len(self.array):
            raise IndexError("Index out of bounds")  # Raise error if index is invalid
        del self.array[index]  # Remove the element at the specified index

    # Time Complexity: O(n) - Traversing through each element to print it
    def print_array(self):
        for element in self.array:  # Iterate through each element
            print(element, end=" ")  # Print the element with a space
        print()  # Print a new line for better readability

    # Time Complexity: O(1) - Getting the length of the array
    def get_length(self):
        return len(self.array)  # Return the length of the array
