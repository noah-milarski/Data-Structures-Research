class UndirectedGraph:
    def __init__(self):
        # Initializes a new undirected graph with an empty dictionary to hold the adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Time Complexity: O(1) for adding an edge in both directions
        # Adds an undirected edge between nodes u and v

        if u not in self.graph:
            self.graph[u] = []  # Initialize adjacency list for u if it doesn't exist
        if v not in self.graph:
            self.graph[v] = []  # Initialize adjacency list for v if it doesn't exist

        self.graph[u].append(v)  # Add v to u's adjacency list
        self.graph[v].append(u)  # Add u to v's adjacency list (undirected, so both ways)

    def remove_edge(self, u, v):
        # Time Complexity: O(E) where E is the number of edges
        # Removes an undirected edge between nodes u and v (removes both directions)

        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)  # Remove v from u's adjacency list
            if u in self.graph[v]:
                self.graph[v].remove(u)  # Remove u from v's adjacency list

    def has_edge(self, u, v):
        # Time Complexity: O(V) where V is the number of vertices in the worst case
        # Checks if there is an undirected edge between u and v
        return u in self.graph and v in self.graph[u] and v in self.graph and u in self.graph[v]

    def get_neighbors(self, u):
        # Time Complexity: O(1) for returning the list of neighbors
        # Returns the neighbors of node u (the nodes that are connected to u)
        return self.graph.get(u, [])

    def bfs(self, start):
        # Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
        # Performs a breadth-first search starting from node 'start'

        visited = set()  # Set to track visited nodes
        queue = [start]  # Initialize queue with the start node

        while queue:  # While there are nodes to explore
            node = queue.pop(0)  # Dequeue a node from the front of the queue
            if node not in visited:  # If it hasn't been visited yet
                visited.add(node)  # Mark it as visited
                print(node, end=' ')  # Process the node (print it)

                # Add all unvisited neighbors to the queue
                for neighbor in self.graph.get(node, []):
                    if neighbor not in visited:
                        queue.append(neighbor)  # Enqueue the neighbor

    def dfs(self, start):
        # Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
        # Performs a depth-first search starting from node 'start'

        visited = set()  # Set to track visited nodes
        self._dfs_recursive(start, visited)  # Start the recursive DFS

    def _dfs_recursive(self, node, visited):
        # Helper method for DFS that performs the recursive call
        if node not in visited:  # If the node hasn't been visited
            visited.add(node)  # Mark it as visited
            print(node, end=' ')  # Process the node (print it)

            # Recursively visit all unvisited neighbors
            for neighbor in self.graph.get(node, []):
                self._dfs_recursive(neighbor, visited)  # Visit the neighbor

    def display(self):
        # Time Complexity: O(V + E) to display all nodes and edges
        # Displays the entire undirected graph's adjacency list representation

        for node in self.graph:
            print(f"{node}: {self.graph[node]}")  # Print each node and its neighbors
