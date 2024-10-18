class DirectedGraph:
    def __init__(self):
        # Initializes a new directed graph with an empty dictionary to hold the adjacency list
        self.graph = {}

    def add_edge(self, u, v):
        # Time Complexity: O(1) for adding an edge
        # Adds a directed edge from node u to node v

        if u not in self.graph:
            self.graph[u] = []  # If u is not in the graph, initialize its adjacency list
        if v not in self.graph:
            self.graph[v] = []  # If v is not in the graph, initialize its adjacency list

        self.graph[u].append(v)  # Add v to u's adjacency list (directed)

    def remove_edge(self, u, v):
        # Time Complexity: O(E) where E is the number of edges
        # Removes the directed edge from node u to node v

        if u in self.graph and v in self.graph:
            self.graph[u].remove(v)  # Remove v from u's adjacency list

    def has_edge(self, u, v):
        # Time Complexity: O(V) where V is the number of vertices in the worst case
        # Checks if there is a directed edge from node u to node v
        return u in self.graph and v in self.graph[u]

    def get_neighbors(self, u):
        # Time Complexity: O(1) for returning the list of neighbors
        # Returns the neighbors of node u (the nodes that u points to)
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
        # Displays the entire directed graph's adjacency list representation

        for node in self.graph:
            print(f"{node}: {self.graph[node]}")  # Print each node and its neighbors
