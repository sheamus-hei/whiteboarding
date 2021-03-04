# this is using adjacency list instead of matrix
# borrowed code from here https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
# (but obviously adapted for adjaceny list)
class Graph:
  def __init__(self):
    self.vertices = []

  def print_graph(self):
    for v in self.vertices:
      print("Vertex", v.data)
      print("Edges:")
      for edge in v.edges:
        print(edge[0].data, f"costing ${edge[1]}") 
  
  def print_dfs(self):
    if len(self.vertices):
      s = set()
      in_order(self.vertices[0], s)

class Vertex:
  def __init__(self, data, edges):
    self.data = data
    self.edges = edges or []

def in_order(vertex, s):
  if vertex.data not in s:
    print(vertex.data)
    s.add(vertex.data)
    for edge in vertex.edges:
      in_order(edge[0], s)

# find next vertex with minimum distance
def min_distance(vertex, s):
  min_cost = sys.maxsize
  next_edge = None
  for edge in vertex.edges:
    if edge[0].data not in s and edge[1] < min_cost:
      min_cost = edge[1]
      next_edge = edge
  return next_edge
  
# Dijkstra method
# find min distance to all nodes in graph
def dijkstra(start, graph):
  paths = []
  current_cost = 0
  s = set()
  for vertex in graph.vertices:
    # find min path to each node until we reach the other node
    edge = min_distance(vertex, s)
    s.add(edge[0])
    current_cost += edge[1]
    # ???
  return paths


# The following code makes this graph: (sorry about inferior ascii art)
#            A
#       5 /^ |   \v 1
#       D    |1    B
#      4^\   v   v/ 3
#            C

g = Graph()
a = Vertex("A", None)
b = Vertex("B", None)
c = Vertex("C", None)
d = Vertex("D", None)

a.edges.append([b, 1])
a.edges.append([c, 1])
b.edges.append([c, 3])
c.edges.append([d, 4])
d.edges.append([a, 5])

g.vertices = [a, b, c, d]
g.print_graph()
g.print_dfs()