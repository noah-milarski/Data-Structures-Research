'''
Time Complexity of Quick Sort:

    Best Case:
        The best-case scenario occurs when the pivot divides the array into two equal halves at each step,
        leading to balanced recursion and optimal time complexity of O(n log n).

        Best-case time complexity: O(n log n).

    Average Case:
        For random input, Quick Sort typically performs well, producing balanced partitions most of the time,
        resulting in O(n log n) complexity on average.

        Average-case time complexity: O(n log n).

    Worst Case:
        The worst case occurs when the pivot always results in unbalanced partitions, such as when the array is
        sorted or nearly sorted, leading to O(n²) complexity.

        Worst-case time complexity: O(n²).

    Space Complexity of Quick Sort:
        Quick Sort is an in-place algorithm, but the recursion depth depends on the partitioning.
        In the worst case, the recursion depth can be O(n), but the average depth is O(log n).

        Worst-case space complexity: O(n) due to recursive calls.
        Average-case space complexity: O(log n).
'''

class QuickSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of elements to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def partition(self, low, high):
        """
        Helper function to partition the array based on a pivot element.
        Elements smaller than the pivot are placed to the left, and elements greater than the pivot are placed to the right.

        :param low: The starting index of the subarray
        :param high: The ending index of the subarray
        :return: The index of the pivot after partitioning
        """
        pivot = self.arr[high]  # Choose the last element as the pivot
        i = low - 1  # Index of the smaller element

        # Traverse through all elements and partition based on the pivot
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1  # Increment index of smaller element
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]  # Swap

        # Swap the pivot element with the element at i+1 (correct position for the pivot)
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]

        return i + 1  # Return the pivot index

    def sort(self, low=None, high=None):
        """
        Method to perform the Quick Sort on the list stored in the instance.
        Recursively sorts the subarrays by partitioning around a pivot.

        :param low: The starting index of the subarray to sort
        :param high: The ending index of the subarray to sort
        """
        if low is None or high is None:
            low, high = 0, len(self.arr) - 1  # Sort the entire array if no bounds are given

        if low < high:
            # Partition the array and get the pivot index
            pi = self.partition(low, high)

            # Recursively sort elements before and after partition
            self.sort(low, pi - 1)  # Sort the left subarray
            self.sort(pi + 1, high)  # Sort the right subarray

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr
