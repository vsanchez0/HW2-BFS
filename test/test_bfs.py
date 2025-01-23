# write tests for bfs
import pytest
from search import graph
import networkx as nx

def get_expected_bfs(filename, start):
    graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    traversal = list(nx.bfs_tree(graph, source=start))
    return traversal

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = Graph("data/tiny_network.adjlist")
    expected = get_expected_bfs("data/tiny_network.adjlist", 'Luke Gilbert')
    traversal = g.bfs("Luke Gilbert")
    assert traversal == expected, f"Expected {expected}, but got {traversal}"

    missing = g.bfs('Snoopy')

def get_expected_shortestpath(filename, start, end):
    graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")
    path = list(nx.shortest_path(graph, source=start, target=end))
    return path

def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = Graph("data/citation_network.adjlist")
    expected = get_expected_shortestpath("data/citation_network.adjlist", 'Marina Sirota', 'Tony Capra')
    path = g.bfs("Marina Sirota", 'Tony Capra')
    assert path == expected, f"Expected {expected}, but got {path}"

    empty_path = g.bfs('Tony Capra', '34916529')
    assert empty_path == None, f"Expected None, but got {empty_path}"
    

test_bfs_traversal()
test_bfs()