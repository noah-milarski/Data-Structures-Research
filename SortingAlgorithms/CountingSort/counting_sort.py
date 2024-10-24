'''
Time Complexity of Counting Sort:

    Best Case:
        The best-case scenario occurs when all elements in the input are the same.
        The time complexity remains O(n + k) due to counting and output array creation.

        Best-case time complexity: O(n + k).

    Average Case:
        The average case also has a time complexity of O(n + k), as the algorithm still needs to count all occurrences
        and generate the output regardless of the distribution of input values.

        Average-case time complexity: O(n + k).

    Worst Case:
        The worst-case scenario occurs when the range of input values (`k`) is significantly larger than the number of elements (`n`),
        but the time complexity still remains O(n + k).

        Worst-case time complexity: O(n + k).

    Space Complexity of Counting Sort:
        Counting Sort requires extra space for the counting array and output array,
        which results in an auxiliary space complexity of O(k), where `k` is the range of the input values.

        Auxiliary space complexity: O(k).
'''

class CountingSort:
    def __init__(self, arr):
        """
        Constructor to initialize the list that needs to be sorted.

        :param arr: list of non-negative integers to be sorted
        """
        self.arr = arr  # Store the list in the class instance

    def sort(self):
        """
        Method to perform Counting Sort on the list stored in the instance.
        """
        if not self.arr:  # If the input array is empty, return immediately
            return

        max_val = max(self.arr)  # Find the maximum value in the array
        count = [0] * (max_val + 1)  # Create a count array with a size of max_val + 1

        # Count each element's occurrences
        for num in self.arr:
            count[num] += 1

        # Update the count array to reflect positions
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Create an output array to store the sorted elements
        output = [0] * len(self.arr)

        # Build the output array using the count array
        for num in reversed(self.arr):  # Traverse the input array in reverse for stability
            output[count[num] - 1] = num
            count[num] -= 1  # Decrease count for the current number

        # Copy the sorted elements back to the original array
        self.arr[:] = output

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr
