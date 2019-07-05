class Graph:
    """
    graph implementation using adjacency list
    format:
        {
            "vertex": [list of adjacent vertices]
        }
    """
    def __init__(self):
        self.adjacency_list = {}
    
    def add_vertex(self, vertex):
        if vertex in self.adjacency_list.keys():
            return None
        self.adjacency_list[vertex] = []

    def add_edge_undirected(self, vertex_a, vertex_b):
        """
        create an undirected edge/path between vertices a and b
        """
        if vertex_a not in self.adjacency_list.keys() or not vertex_b in self.adjacency_list.keys():
            # both vertices must exist to create an edge to join them
            return None
        # only add an edge if there's no edge joining them.
        if vertex_a not in self.adjacency_list[vertex_b]:
            self.adjacency_list[vertex_b].append(vertex_a)
        if vertex_b not in self.adjacency_list[vertex_a]:
            self.adjacency_list[vertex_a].append(vertex_b)
    
    def add_edge_directed(self, vertex_a, vertex_b):
        """
        create an edge from vertex a to b ONLY
        """
        if vertex_a not in self.adjacency_list.keys() or vertex_b not in self.adjacency_list.keys():
            # both vertices must exist to create an edge to join them
            return None
        # print("vertex b: ", vertex_b, vertex_a)
        if vertex_b not in self.adjacency_list[vertex_a]:
            self.adjacency_list[vertex_a].append(vertex_b)

    def bfs_traversal(self, start_node):
        """
        uses queue(FIFO) data structure
        """
        if start_node not in self.adjacency_list.keys():
            return None
        visited = {}
        queue = []
        # push start node to queue
        queue.append(start_node)
        while(queue):
            # remove from queue i.e. first vertex on queue
            vertex = queue.pop(0)
            # check if vertex is already visited
            if vertex not in visited.keys():
                visited[vertex] = True
                print(vertex)
            for edge in self.adjacency_list[vertex]:
                if edge not in visited.keys():
                    queue.append(edge)


"""
# uncomment to run

graph = Graph()
graph.add_vertex("Nairobi")
graph.add_vertex("Mombasa")
print(graph.adjacency_list)
graph.add_edge_undirected("Nairobi", "Mombasa")
print(graph.adjacency_list)
graph.add_vertex("Kisumu")
graph.add_edge_undirected("Nairobi", "Kisumu")
graph.add_edge_directed("Kisumu", "Mombasa")
print(graph.adjacency_list)

# bfs traversal
graph.bfs_traversal("Nairobi")
"""
