'''
Time Complexity of Merge Sort:

    Best Case:
        Even if the input array is already sorted, Merge Sort still splits and merges the array.
        Thus, the best-case time complexity is O(n log n).

        Best-case time complexity: O(n log n).

    Average Case:
        In the average case, the array is in a random order. The divide-and-conquer approach ensures
        that the performance remains the same.

        Average-case time complexity: O(n log n).

    Worst Case:
        The worst case occurs when the array is sorted in reverse order or randomly. However, the time complexity
        remains consistent due to the recursive nature of the algorithm.

        Worst-case time complexity: O(n log n).

    Space Complexity of Merge Sort:
        Merge Sort is not an in-place sorting algorithm. It requires extra space proportional to the input size
        for temporary subarrays during the merge step.

        Worst-case space complexity: O(n).
'''

class MergeSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of elements to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def merge(self, left, right):
        """
        Helper function to merge two sorted subarrays into a single sorted array.

        :param left: The left subarray
        :param right: The right subarray
        :return: Merged sorted array
        """
        merged = []
        i = j = 0

        # Merge the two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        # If any elements remain in the left subarray, append them
        merged.extend(left[i:])

        # If any elements remain in the right subarray, append them
        merged.extend(right[j:])

        return merged

    def sort(self, arr=None):
        """
        Method to perform the Merge Sort on the list stored in the instance.
        Recursively splits the array and merges sorted subarrays.

        :param arr: Optional subarray to be sorted. Defaults to the entire array.
        :return: Sorted array
        """
        if arr is None:
            arr = self.arr  # Use the main array if no subarray is passed

        # Base case: If the array has only one element, return it (it's already sorted)
        if len(arr) <= 1:
            return arr

        # Find the middle point and split the array into two halves
        mid = len(arr) // 2
        left = self.sort(arr[:mid])  # Recursively sort the left half
        right = self.sort(arr[mid:])  # Recursively sort the right half

        # Merge the sorted halves
        return self.merge(left, right)

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.sort()
