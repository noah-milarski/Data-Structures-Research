class HashMapChaining:
    def __init__(self):
        self.MAX = 10  # Set the size of the hash table
        # Initialize each index of the hash table as an empty list (to store chains)
        self.arr = [[] for _ in range(self.MAX)]

        # Function to compute the hash value of a key

    def get_hash(self, key):
        hash = 0  # Initialize hash value
        # Sum the ASCII values of each character in the key
        for char in key:
            hash += ord(char)
            # Return the hash value mod the size of the hash table (self.MAX)
        return hash % self.MAX

        # Function to retrieve a value by key (Time Complexity: O(n) in worst case, O(1) in best case)

    def __getitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # Traverse the list (chain) at the hash index 'h'
        for element in self.arr[h]:
            if element[0] == key:  # If the key matches, return its corresponding value
                return element[1]
        return None  # If key is not found in the chain, return None

    # Function to insert or update a key-value pair (Time Complexity: O(n) in worst case, O(1) in best case)
    def __setitem__(self, key, val):
        h = self.get_hash(key)  # Get the hash index for the key
        # Traverse the chain at index 'h' to check if the key already exists
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:  # If key exists, update the value
                self.arr[h][idx] = (key, val)
                return
        # If key does not exist, append the new key-value pair to the chain at index 'h'
        self.arr[h].append((key, val))
        print(self.arr)  # Optional: Print the hash table for debugging

    # Function to delete a key-value pair by key (Time Complexity: O(n) in worst case, O(1) in best case)
    def __delitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # Traverse the chain at index 'h' to find the key-value pair
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:  # If key is found, delete the key-value pair from the list
                del self.arr[h][idx]
                return
        print(self.arr)  # Optional: Print the hash table for debugging