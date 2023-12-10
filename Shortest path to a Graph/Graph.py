from Queue import Queue
 
class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.neighbors = self.getAdjacnecyLists(edges)
 
    # Return a list of adjacency lists for edges
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
           
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v)) # Insert an edge (u, v)
 
        return neighbors
   
 
    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]
 
  
 
    # Print the edges
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print("Vertex " + str(self.getVertex(u)) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " +
                      str(self.neighbors[u][j].v), end = ") ")
            print()
 
 
    # Starting bfs search from vertex v
    # To be discussed in Section 22.7
    def bfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1
 
        queue = Queue() # the Queue class is defined in Chapter 17
        isVisited = len(self.vertices) * [False]
        queue.enqueue(v) # Enqueue v
        isVisited[v] = True # Mark it visited
 
        while not queue.isEmpty():
            u = queue.dequeue() # Dequeue to u
            searchOrders.append(u) # u searched
            for e in self.neighbors[u]:
                if not isVisited[e.v]:
                    queue.enqueue(e.v) # Enqueue w
                    parent[e.v] = u # The parent of w is u
                    isVisited[e.v] = True # Mark it visited
 
        return Tree(v, parent, searchOrders, self.vertices)
 
# Tree  class will be discussed in Section 22.5
class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root # The root of the tree
        # Store the parent of each vertex in a list
        self.parent = parent
        # Store the search order in a list
        self.searchOrders = searchOrders
        self.vertices = vertices # vertices of the graph
 
 
   
    # Return the path of vertices from a vertex index to the root
    def getPath(self, index):
        path = []
 
        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]
        return path
 
 
# The Edge class for defining an edge from u to v       
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v