# Heap Class that can work as both MaxHeap and MinHeap depending on the 'is_max' flag
class Heap:
    def __init__(self, is_max=True):
        self.heap = []  # The internal list representation of the heap
        self.is_max = is_max  # Flag to determine if it's a max heap or min heap

    # Helper function to compare values depending on heap type
    def _compare(self, parent, child):
        # If max heap, parent should be greater than or equal to child
        # If min heap, parent should be less than or equal to child
        return parent >= child if self.is_max else parent <= child

    # Time Complexity: O(log n)
    # Why: Inserting into a heap involves placing the new element at the end and then "bubbling up" the element
    # to restore heap order, which takes log(n) time in the worst case (height of the tree).
    def insert(self, value):
        self.heap.append(value)  # Add the new value at the end
        self._bubble_up(len(self.heap) - 1)  # Restore the heap property by bubbling up

    # Helper function to maintain heap property after insertion (bubbling up)
    def _bubble_up(self, index):
        parent = (index - 1) // 2  # Parent index of the current node
        while index > 0 and not self._compare(self.heap[parent], self.heap[index]):
            # Swap with the parent if the heap property is violated
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent  # Move up to the parent's index
            parent = (index - 1) // 2

    # Time Complexity: O(log n)
    # Why: Removing the root involves replacing it with the last element and then "bubbling down" to restore the heap.
    def remove(self):
        if len(self.heap) == 0:
            return None  # Return None if heap is empty
        if len(self.heap) == 1:
            return self.heap.pop()  # If only one element, just pop and return it
        root = self.heap[0]  # Save the root element to return it later
        self.heap[0] = self.heap.pop()  # Replace root with the last element
        self._bubble_down(0)  # Restore the heap property by bubbling down
        return root  # Return the removed root element

    # Helper function to maintain heap property after removal (bubbling down)
    def _bubble_down(self, index):
        length = len(self.heap)
        left_child = 2 * index + 1  # Left child index
        right_child = 2 * index + 2  # Right child index

        while left_child < length:
            # Determine the index of the child to swap with
            swap_index = left_child
            if right_child < length and not self._compare(self.heap[left_child], self.heap[right_child]):
                swap_index = right_child
            if self._compare(self.heap[index], self.heap[swap_index]):
                break
            self.heap[index], self.heap[swap_index] = self.heap[swap_index], self.heap[index]
            index = swap_index  # Move down to the child's index
            left_child = 2 * index + 1
            right_child = 2 * index + 2

    # Time Complexity: O(n log n)
    # Why: Heapsort involves inserting all elements into a heap (O(n log n)) and then extracting them back (O(n log n)).
    def heapsort(self):
        sorted_list = []
        original_heap = self.heap[:]  # Copy the original heap
        while self.heap:
            sorted_list.append(self.remove())  # Repeatedly remove the root element and store it in sorted_list
        self.heap = original_heap  # Restore the original heap
        return sorted_list if not self.is_max else sorted_list[::-1]  # Reverse if max heap for ascending order

    # Time Complexity: O(n)
    # Why: Heapify processes all elements and organizes them into a valid heap in linear time.
    def heapify(self, array):
        self.heap = array[:]  # Copy the array into the heap
        for i in reversed(range(len(self.heap) // 2)):
            self._bubble_down(i)  # Rebuild the heap by bubbling down non-leaf nodes

    # Time Complexity: O(1)
    # Why: Accessing the first element of the heap takes constant time.
    def find_largest(self):
        return self.heap[0] if self.is_max and self.heap else None

    # Time Complexity: O(1)
    # Why: Accessing the first element of the heap takes constant time.
    def find_smallest(self):
        return self.heap[0] if not self.is_max and self.heap else None

    # Time Complexity: O(log n)
    # Why: Enqueue is essentially inserting an element, which is a log(n) operation in a heap.
    def enqueue(self, value):
        self.insert(value)  # Insert the element into the heap (priority queue)

    # Time Complexity: O(log n)
    # Why: Dequeue is equivalent to removing the root of the heap, which takes log(n) time.
    def dequeue(self):
        return self.remove()  # Remove the element with the highest priority
