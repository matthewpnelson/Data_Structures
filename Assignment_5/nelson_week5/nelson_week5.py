## Data Structures and Algorithms, Week 5 assignment
## Matt Nelson, Jan 5, 2017

import string
from queue import Queue

def read_adj(input_file):
    with open(input_file, 'rt') as f_in:
        matrix = []
        for line in f_in.readlines():
            #print(line.strip("  "))
            line_dig = []
            for i in line:
                if i == "0" or i == "1":
                    line_dig.append(int(i))
            matrix.append(line_dig)
    return matrix


class GraphNode:
    """A node for an undirected linked graph, adapted from lecture notes / Goodrich textbook."""

    def __init__(self, name, value=None):
        self.value = value
        self.name = name
        self.connections = []
        self.connection_names = []

    def add_connections(self,other):
        if other not in self.connections:
            self.connections.append(other)
            self.connection_names.append(other.name)
        if self not in other.connections:
            other.connections.append(self)
            other.connection_names.append(self.name)

    def get_connections(self):
        return self.connections

    def get_connection_names(self):
        print("Current Node Name:", self.name)
        return self.connection_names

def graph(matrix):
    """Populate a graph from an adjacency matrix.

    Create nodes and add connections and connection names based
    on an adjacency matrix input (an array list)
    """

    # Create nodes
    node_list = []
    i=1
    while i <= len(matrix[0]):
        name = "Node" + str(i)
        node_list.append(GraphNode(name))
        i += 1

    # Add connections and connection names based on an adjacency matrix input (an array list)
    current_row_node_index = 0
    for row in matrix:
        current_column_node_index = 0
        for column in row:
            if column == 1:
                node_list[current_column_node_index].add_connections(node_list[current_row_node_index])
            current_column_node_index += 1
        current_row_node_index += 1

    return node_list

def breadth_first_traverse(node_object):
    """Traverse a tree, breadth first. Adapted from lecture notes.
    Complete checks to ensure nodes are not counted more than once.
    """

    Q = Queue()
    Q.put(node_object)
    already_pulled = []

    # Array with indexes indicating the objects with index number of steps to the node_object
    # ie. index [1] is one node away from node_object
    path_count = [[node_object]]

    while not Q.empty():
        v = Q.get()

        # Ignore node if already_pulled from queue
        if v in already_pulled:
            continue

        # Proceed to build queue with connections at node v
        already_pulled.append(v)
        path_count_connection_index = 0
        for connections in v.get_connections():

            # Verify the node has not already been removed from the stack or passed through
            if connections not in already_pulled:
                Q.put(connections)

                # Calculate the correct index to place the connections into
                for sublist in path_count:
                    #print(sublist)
                    if v in sublist:
                        path_count_connection_index = path_count.index(sublist) + 1

                # Add connections to the correct path_count via calculated index
                try:
                    i = 0
                    while i < len(path_count):
                        if connections in path_count[i]:
                            break
                        i += 1
                    else:
                        path_count[path_count_connection_index].append(connections)
                    continue

                except:
                    path_count.append([])
                    path_count[path_count_connection_index].append(connections)

    return path_count


def equidistant(n1,n2, node_list):
    """Calculate a list of nodes which are equidistant between two passed in nodes.
    Nodes should be entered as numbers."""
    n1_index = int(n1)
    n2_index = int(n2)

    n1_distances = breadth_first_traverse(node_list[n1_index])
    n2_distances = breadth_first_traverse(node_list[n2_index])

    equidistant_nodes = []
    i = 0
    while i < len(n1_distances):
        for each in n1_distances[i]:
            try:
                if each in n2_distances[i]:
                    equidistant_nodes.append(each)
            except:
                break
        i += 1

    return equidistant_nodes

# MAIN PART OF SCRIPT

# Read in adjacency matrix
matrix = read_adj("adj.txt")

# Create a Graph from the Matrix
node_list = graph(matrix)

# Import input.txt file containing nodes,
# Calculate the equidistant nodes to those two nodes,
# Write # of equidistant nodes to output.txt
with open("input.txt", 'rt') as f_in:
    out = ""
    for r in f_in.readlines():
        r = r.strip("\n")
        out += str(len(equidistant(int(r[0]),int(r[2]),node_list))) + "\n"

with open("output.txt", 'wt') as f_out:
    f_out.write(out)
