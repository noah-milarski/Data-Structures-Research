class BasicHashMap:
    def __init__(self):
        self.MAX = 10  # Set the size of the hash table
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

    # Function to insert or update a key-value pair (O(1))
    def __setitem__(self, key, val):
        h = self.get_hash(key)  # Get the hash index for the key
        # Insert or update the key-value pair at the computed hash index
        self.arr[h] = (key, val)
        print(self.arr)  # Optional: Print the current state of the hash table

    # Function to retrieve a value by key (O(1))
    def __getitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # If no element exists at the hash index, return None (key not found)
        if self.arr[h] is None:
            return None
        # If the key matches, return the associated value
        if self.arr[h][0] == key:
            return self.arr[h][1]
        return None  # In case of collision, but this version doesn't handle it

    # Function to delete a key-value pair (O(1))
    def __delitem__(self, key):
        h = self.get_hash(key)  # Get the hash index for the key
        # If the key exists, set the slot to None (delete key-value pair)
        if self.arr[h] is not None and self.arr[h][0] == key:
            self.arr[h] = None
        print(self.arr)  # Optional: Print the current state of the hash table
