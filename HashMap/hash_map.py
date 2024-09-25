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


class HashMapLinearProbing:
    def __init__(self):
        self.MAX = 10  # Set the size of the hash table (low to demonstrate linear probing)
        # Initialize the array with None values (each index will hold a key-value pair)
        self.arr = [None for _ in range(self.MAX)]

    # Function to compute the hash value of a key
    def get_hash(self, key):
        hash = 0  # Initialize the hash value
        # Loop through each character in the key and compute ASCII sum
        for char in key:
            hash += ord(char)
            # Return the hash value mod the size of the hash table
        return hash % self.MAX

        # Function to retrieve a value by key (Time Complexity: O(n) in worst case, O(1) in best case)

    def __getitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # If no element exists at the hash index, return None (key not found)
        if self.arr[h] is None:
            return
        # Get the range of probe indices for linear probing
        prob_range = self.get_prob_range(h)
        # Traverse the probing range to find the key
        for prob_index in prob_range:
            element = self.arr[prob_index]
            if element is None:  # If an empty slot is found, return None (key not found)
                return
            if element[0] == key:  # If the key matches, return the associated value
                return element[1]

    # Function to insert or update a key-value pair (Time Complexity: O(n) in worst case, O(1) in best case)
    def __setitem__(self, key, val):
        h = self.get_hash(key)  # Get the hash index for the key
        # If no collision, insert key-value pair at hash index
        if self.arr[h] is None:
            self.arr[h] = (key, val)
        else:
            # If a collision occurs, find the next available slot using linear probing
            new_h = self.find_slot(key, h)
            # Insert the key-value pair at the new hash index
            self.arr[new_h] = (key, val)
        print(self.arr)  # Optional: Print the current state of the hash table

    # Function to get the probing range for linear probing
    def get_prob_range(self, index):
        # Return a range of indices starting from 'index' to the end, then wrap around to the start
        return [*range(index, len(self.arr))] + [*range(0, index)]

    # Function to find the next available slot using linear probing (Time Complexity: O(n))
    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)  # Get the probing range starting from the hash index
        # Traverse the probing range to find an empty slot or an existing key
        for prob_index in prob_range:
            # If an empty slot is found, return that index
            if self.arr[prob_index] is None:
                return prob_index
            # If the key already exists, return its index (to update the value)
            if self.arr[prob_index][0] == key:
                return prob_index
        # If no empty slot is found, raise an exception (hash table is full)
        raise Exception("Hashmap full")

    # Function to delete a key-value pair (Time Complexity: O(n) in worst case, O(1) in best case)
    def __delitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        prob_range = self.get_prob_range(h)  # Get the probing range starting from the hash index
        # Traverse the probing range to find the key and delete it
        for prob_index in prob_range:
            # If an empty slot is found, stop searching (key not found)
            if self.arr[prob_index] is None:
                return  # Key not found, return without error (could throw exception if desired)
            # If the key matches, set the slot to None (delete key-value pair)
            if self.arr[prob_index][0] == key:
                self.arr[prob_index] = None
        print(self.arr)  # Optional: Print the current state of the hash table
