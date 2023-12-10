#  In order for this program run and find the .txt file
#  the file has to be save in the following pathway:
#  /Users/"username"/"file.txt",
#  whereas username = username for the sesion on the computer
#  file.txt the .txt file the it has to be input


from Graph import Graph
from Queue import Queue
import os.path
import sys


filename = input("Enter a file: ").strip()
print("Absolute path:", os.path.abspath(filename))
if not os.path.isfile(filename):
    print(filename, "does not exist")
    sys.exit()

# Take input for two vertices (integer indexes)
start_vertex = int(input("Enter the starting vertex: "))
end_vertex = int(input("Enter the ending vertex: "))

inputFile = open(filename, "r")
lines = inputFile.readlines()
inputFile.close()

# Read the number of vertices and print it
num_vertices = int(lines[0])
print("Number of vertices:", num_vertices)

vertices = []
edges = []

for line in lines[1:]:
    tokens = [int(x) for x in line.split()]

    starting_vertex = tokens[0]
    vertices.append(starting_vertex)
    for adjacent_vertex in tokens[1:]:
        edges.append([starting_vertex, adjacent_vertex])

# Call Graph Constructor with vertices and edges
graph = Graph(vertices, edges)

# Print the edges in the graph as a list
print("Edges in the graph:")
graph.printEdges()

# Call the method (bfs) to set a path (if connected) between input vertices
tree = graph.bfs(start_vertex)

if tree.getPath(end_vertex):
    print(f"There is a path between {start_vertex} and {end_vertex}:")
    path = tree.getPath(end_vertex)
    print(" -> ".join(map(str, path)))
    print(f"Shortest hops between {start_vertex} and {end_vertex}: {len(path) - 1}")
else:
    print(f"There is no path between {start_vertex} and {end_vertex}.")
