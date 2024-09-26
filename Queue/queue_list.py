class QueueList:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the end of the queue.
        Time Complexity: O(1) - appending to the end of a list is a constant time operation.
        """
        self.queue.append(item)  # Add item to the end of the list
        print(f"Enqueued {item} to queue")

    def dequeue(self):
        """Removes and returns the front item from the queue.
        Time Complexity: O(n) - removing the first item requires shifting all subsequent elements.
        """
        if not self.is_empty():  # Check if the queue is not empty
            dequeued_item = self.queue.pop(0)  # Remove and return the first element
            print(f"Dequeued {dequeued_item} from queue")
            return dequeued_item
        else:
            print("Queue is empty, cannot dequeue an element")
            return None

    def front(self):
        """Returns the front item from the queue without removing it.
        Time Complexity: O(1) - accessing the first element in a list is a constant time operation.
        """
        if not self.is_empty():  # Check if the queue is not empty
            front_item = self.queue[0]  # Get the first element in the list
            print(f"Front element is: {front_item}")
            return front_item
        else:
            print("Queue is empty, no element to show at the front")
            return None

    def is_empty(self):
        """Checks if the queue is empty.
        Time Complexity: O(1) - checking the length of a list is a constant time operation.
        """
        empty = len(self.queue) == 0  # Check if list length is zero
        print(f"Is queue empty? {empty}")
        return empty

    def size(self):
        """Returns the number of elements in the queue.
        Time Complexity: O(1) - getting the length of the list is a constant time operation.
        """
        size = len(self.queue)  # Get the number of elements in the queue
        print(f"Queue size is: {size}")
        return size

    def display(self):
        """Displays all the elements in the queue.
        Time Complexity: O(n) - iterating over the list to print each element.
        """
        print("Queue elements (front to back):")
        for item in self.queue:  # Display elements from front to back
            print(item)