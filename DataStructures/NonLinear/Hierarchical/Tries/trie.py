class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to hold children nodes (characters)
        self.is_end_of_word = False  # True if the node represents the end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node of the Trie

    # Time Complexity: O(m), where m is the length of the word
    # Why: Inserting a word involves traversing its characters (m), and possibly creating new nodes along the way.
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # Create a new node if the character doesn't exist
            node = node.children[char]  # Move to the next node
        node.is_end_of_word = True  # Mark the end of the word

    # Time Complexity: O(m), where m is the length of the word
    # Why: Searching a word involves traversing its characters (m).
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False  # If the character isn't in the Trie, return False
            node = node.children[char]
        return node.is_end_of_word  # Return True if it's the end of a valid word

    # Time Complexity: O(m), where m is the length of the prefix
    # Why: Checking if a prefix exists involves traversing the characters of the prefix.
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False  # If the character isn't in the Trie, return False
            node = node.children[char]
        return True  # Return True if the prefix exists in the Trie

    # Time Complexity: O(m), where m is the length of the word
    # Why: Deleting a word involves traversing its characters and unmarking the end of word.
    def delete(self, word):
        def _delete(node, word, depth):
            if depth == len(word):
                if not node.is_end_of_word:
                    return False  # Word doesn't exist
                node.is_end_of_word = False  # Unmark the end of the word
                return len(node.children) == 0  # If the node has no children, it can be deleted
            char = word[depth]
            if char not in node.children:
                return False  # Word doesn't exist
            should_delete = _delete(node.children[char], word, depth + 1)
            if should_delete:
                del node.children[char]  # Delete the node if it can be removed
                return len(node.children) == 0  # Return True if the parent node can also be deleted
            return False

        _delete(self.root, word, 0)

    # Helper function to display all words in the Trie
    def display(self):
        def _collect_words(node, prefix, words):
            if node.is_end_of_word:
                words.append(prefix)  # Add the word to the list if it's a valid word
            for char, child_node in node.children.items():
                _collect_words(child_node, prefix + char, words)

        words = []
        _collect_words(self.root, '', words)  # Start collecting from the root node
        return words