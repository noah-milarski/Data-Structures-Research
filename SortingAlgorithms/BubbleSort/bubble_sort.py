'''
Time Complexity of Bubble Sort:

    Best Case:
        The best-case scenario occurs when the input array is already sorted.
        In this case, the algorithm only needs one pass to verify that the list is sorted, so no swaps are made,
        and the inner loop runs once for each element.

        Best-case time complexity: O(n), where n is the number of elements.

    Average Case:
        On average, each element will need to be swapped about halfway through the array, requiring multiple passes.

        Average-case time complexity: O(n^2).

    Worst Case:
        The worst case occurs when the input array is in reverse order. In this case, every element needs to be swapped on every pass,
        requiring n passes with n comparisons on each pass.

        Worst-case time complexity: O(n^2).

    Space Complexity of Bubble Sort:
        Bubble Sort is an in-place sorting algorithm, meaning it does not require extra space proportional to the input size.
        It only uses a constant amount of additional memory (for variables like swapped).

        Worst-case space complexity: O(1) (constant space).
'''

class BubbleSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of elements to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def sort(self):
        """
        Method to perform the Bubble Sort on the list stored in the instance.
        """
        n = len(self.arr)  # Get the number of elements in the list

        # Outer loop: Traverse through all elements
        for i in range(n):
            swapped = False  # Initialize flag to detect any swap in this pass

            # Inner loop: Compare adjacent elements
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    # Swap if the current element is greater than the next one
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    swapped = True  # Mark swapped as True since a swap occurred

            # If no elements were swapped in the inner loop, the array is sorted
            if not swapped:
                break  # Break out of the loop early if the list is sorted

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr