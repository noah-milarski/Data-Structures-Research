'''
Time Complexity of Insertion Sort:

    Best Case:
        The best-case scenario occurs when the input array is already sorted.
        In this case, the algorithm only needs to pass through the array without any shifting or swapping.

        Best-case time complexity: O(n), where n is the number of elements.

    Average Case:
        On average, each element needs to be compared and shifted back until it reaches its correct position,
        resulting in quadratic time complexity.

        Average-case time complexity: O(n^2).

    Worst Case:
        The worst case occurs when the input array is sorted in reverse order. Every element needs to be compared
        and shifted back to the beginning of the list, requiring maximum comparisons and shifts.

        Worst-case time complexity: O(n^2).

    Space Complexity of Insertion Sort:
        Like Bubble Sort, Insertion Sort is an in-place sorting algorithm, meaning it requires only a constant amount
        of extra space regardless of the input size.

        Worst-case space complexity: O(1) (constant space).
'''

class InsertionSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of elements to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def sort(self):
        """
        Method to perform the Insertion Sort on the list stored in the instance.
        """
        n = len(self.arr)  # Get the number of elements in the list

        # Traverse from the second element to the last
        for i in range(1, n):
            key = self.arr[i]  # Element to be inserted in the sorted sublist
            j = i - 1

            # Shift elements of the sorted sublist that are greater than the key to one position ahead
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]  # Move element to the right
                j -= 1

            # Insert the key into its correct position
            self.arr[j + 1] = key

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr
