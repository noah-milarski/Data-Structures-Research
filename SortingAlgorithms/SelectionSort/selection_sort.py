'''
Time Complexity of Selection Sort

    Best Case:
        The best-case scenario for selection sort occurs when the input array is already sorted.
        However, even in this case, the algorithm will still have to go through the entire array to verify that it is sorted, making the comparisons.
        Best-case time complexity: O(n²), where n is the number of elements.

    Average Case:
        On average, for every element, the selection sort will have to make comparisons with all remaining unsorted elements to find the minimum.
        This leads to roughly n/2 comparisons for each of the n elements.
        Average-case time complexity: O(n²).

    Worst Case:
        The worst-case scenario also results in the same number of comparisons as the average case.
        This is because selection sort always performs n-1 comparisons for the first element, n-2 for the second, and so on, down to 1 for the last element.
        Worst-case time complexity: O(n²).

Space Complexity of Selection Sort

    Selection Sort is an in-place sorting algorithm, meaning it does not require extra space proportional to the input size.
    It only uses a constant amount of additional memory for variables used during the sorting process (like min_index).
    Space complexity: O(1) (constant space).
'''

class SelectionSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of elements to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def sort(self):
        """
        Method to perform the Selection Sort on the list stored in the instance.
        """
        n = len(self.arr)  # Get the number of elements in the list

        # Outer loop: Traverse through all elements
        for i in range(n):
            # Assume the minimum is the first element of the unsorted part
            min_index = i

            # Inner loop: Find the index of the minimum element in the unsorted part
            for j in range(i + 1, n):
                if self.arr[j] < self.arr[min_index]:
                    min_index = j

            # Swap the found minimum element with the first element of the unsorted part
            if min_index != i:
                self.arr[i], self.arr[min_index] = self.arr[min_index], self.arr[i]

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr