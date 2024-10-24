'''
Time Complexity of Bucket Sort:

    Best Case:
        The best-case scenario occurs when all elements are uniformly distributed across the buckets,
        allowing for linear time complexity.

        Best-case time complexity: O(n).

    Average Case:
        The average-case time complexity is also O(n) when the elements are uniformly distributed,
        allowing for efficient sorting within each bucket.

        Average-case time complexity: O(n).

    Worst Case:
        The worst-case scenario occurs when all elements fall into a single bucket,
        leading to time complexity similar to the sorting algorithm used within that bucket (e.g., O(n²) for insertion sort).

        Worst-case time complexity: O(n²).

    Space Complexity of Bucket Sort:
        Bucket Sort requires extra space for the buckets created for sorting.

        Auxiliary space complexity: O(n + k), where `n` is the number of elements and `k` is the number of buckets.
'''

class BucketSort:
    def __init__(self, arr, num_buckets=10):
        """
        Constructor to initialize the list that needs to be sorted and the number of buckets.

        :param arr: list of elements to be sorted (assumed to be numerical)
        :param num_buckets: number of buckets to use for sorting
        """
        self.arr = arr  # Store the list in the class instance
        self.num_buckets = num_buckets  # Set the number of buckets

    def sort(self):
        """
        Method to perform Bucket Sort on the list stored in the instance.
        """
        if not self.arr:  # If the input array is empty, return immediately
            return

        # Create empty buckets
        buckets = [[] for _ in range(self.num_buckets)]

        # Find the maximum and minimum values to determine the range
        min_value = min(self.arr)
        max_value = max(self.arr)

        # Calculate the range for each bucket
        range_of_buckets = (max_value - min_value) / self.num_buckets

        # Distribute elements into buckets
        for num in self.arr:
            index = int((num - min_value) // range_of_buckets)  # Determine bucket index
            if index == self.num_buckets:  # Handle the edge case where num is the max value
                index -= 1
            buckets[index].append(num)

        # Sort each bucket and concatenate the results
        sorted_array = []
        for bucket in buckets:
            sorted_array.extend(sorted(bucket))  # You can replace sorted() with any sorting algorithm

        # Update the original array with the sorted elements
        self.arr[:] = sorted_array

    def get_sorted_array(self):
        """
        Method to return the sorted array.

        :return: Sorted list
        """
        return self.arr
