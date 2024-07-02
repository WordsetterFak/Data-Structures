from __future__ import annotations
# Me pinaka geitniashs / adjacency matrix


class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.index = -1


class Graph:

    def __init__(self, directed: bool = False) -> None:
        self.nodes: list[Node] = []
        self.adjacencyMatrix = []  # 1 if there is an edge from node i to node j (directed), else 0
        self.directed = directed

    def addNode(self, node: Node):

        if node.index != -1:
            # Not allowed to add same node instance more than once
            return

        node.index = len(self.nodes)
        self.nodes.append(node)

        for i in self.adjacencyMatrix:
            i.append(0)  # add new columnn every existing row representing edge from node i to new node
        
        self.adjacencyMatrix.append([0] * len(self.nodes))  # add new row representing edgees from new node to other nodes
    
    def removeNode(self, node: Node):

        if node.index == -1:
            return  # node doesn't exist in graph
        
        self.nodes.pop(node.index)

        for i in self.adjacencyMatrix:
            i.pop(node.index)  # remove respective column from every row
        
        self.adjacencyMatrix.pop(node.index)  # remove respective node row entirely

        for i in range(node.index, len(self.nodes)):
            self.nodes[i].index -= 1  # adjust indexes
        
        node.index = -1
    
    def addEdge(self, node1: Node, node2: Node):

        if node1.index == -1 or node2.index == -1:
            return  # at least one node doesn't exist in the graph

        self.adjacencyMatrix[node1.index][node2.index] = 1  # add edge (node1, node2)
        
        if not self.directed:  # add opposite direction edge if graph lacks direction
            self.adjacencyMatrix[node2.index][node1.index] = 1  # add edge (node2, node1)

    def removeEdge(self, node1: Node, node2: Node):

        if node1.index == -1 or node2.index == -1:
            return  # at least one node doesn't exist in the graph

        self.adjacencyMatrix[node1.index][node2.index] = 0  # remove edge (node1, node2) if it exists
        
        if not self.directed:  # remove opposite direction edge if graph lacks direction
            self.adjacencyMatrix[node2.index][node1.index] = 0

    def areNeighboring(self, node1: Node, node2: Node) -> bool:
        """
        True if there exists an edge from node1 to node2 or from node2 to node1
        """

        if node1.index == -1 or node2.index == -1:
            return False # at least one node doesn't exist in the graph

        # check if one is reachable from the other
        return self.adjacencyMatrix[node1.index][node2.index] == 1 or self.adjacencyMatrix[node2.index][node1.index] == 1

    def degreeOfNode(self, node: Node) -> int:
        """
        Number of outgoing edges
        """

        if node.index == -1:
            return 0
        
        s = 0

        # sum of the node's row, since s = number of 1s = number of outgoing edges
        for i in range(len(self.nodes)):
            s += self.adjacencyMatrix[node.index][i]
        
        return s



if __name__ == "__main__":

    x = Graph(directed=False)
    n1 = Node(3)
    n2 = Node(5)
    n3 = Node(3)
    n4 = Node(0)
    n5 = Node(-1)

    x.addNode(n1)
    x.addNode(n2)
    x.addNode(n3)
    x.addNode(n4)
    print(n2.index)

    x.removeNode(n3)

    x.addEdge(n1, n2)
    x.addEdge(n2,n3)
    x.addEdge(n2,n4)
    x.addNode(n5)
    x.addEdge(n2, n5)
    print(x.degreeOfNode(n2))
    print(x.adjacencyMatrix)
