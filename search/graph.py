import networkx as nx
import queue

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        if nx.is_empty(self.graph):
            raise ValueError(f'Graph is empty')
        if start not in self.graph:
            raise ValueError(f"Start node {start} is not in the graph.")
        if end is not None and end not in self.graph:
            raise ValueError(f"End node {end} is not in the graph.")

        Q = queue.Queue()
        visited = []
        parent = {}

        Q.put(start)
        visited.append(start)
        parent[start] = None

        while not Q.empty():
            v = Q.get()

            if v == end:
                path = []
                while v is not None:
                    path.append(v)
                    v = parent[v]
                return path[::-1]

            for neighbor in self.graph.neighbors(v):
                if neighbor not in visited:
                    visited.append(neighbor)
                    parent[neighbor] = v
                    Q.put(neighbor)

        if end is None:
            return list(visited)
        return None