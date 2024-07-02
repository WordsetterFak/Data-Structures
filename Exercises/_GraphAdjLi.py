from __future__ import annotations
from _LinkedList import LinkedList, LinkedListNode

# Neighboring list, lista geitniashs


class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.index = -1
        self.outgoingNeighbors = LinkedList()  # lista geitniashs, adjecency list


class Graph:

    def __init__(self, directed=False) -> None:
        self.directed=directed
        self.nodes: list[Node] = []

    def addNode(self, node: Node):
        if node.index != -1:
            return  # not allowed to add same node instance more than once

        node.index = len(self.nodes)
        self.nodes.append(node)
    
    def removeNode(self, nodeToRemove: Node):
        
        self.nodes.pop(nodeToRemove.index)

        for node in self.nodes:

            if node is nodeToRemove:
                continue
            
            if node.index > nodeToRemove.index:  # adjust index
                node.index -= 1

            node.outgoingNeighbors.removeIf(lambda x: x is nodeToRemove)

        nodeToRemove.index = -1  # remove index

    def addEdge(self, node1: Node, node2: Node):
        node1.outgoingNeighbors.addNodesAtTail([LinkedListNode(node2)])  # add (node1, node2) directed edge

        if not self.directed:  # add opposite direction edge, to account for lack of direction in this graph
            node2.outgoingNeighbors.addNodesAtTail([LinkedListNode(node1)])  # add (node2, node1) directed edge
    
    def removeEdge(self, node1: Node, node2: Node):

        node1.outgoingNeighbors.removeIf(lambda x: x is node2)  # remove edge (node1, node2) if it exists
        
        if not self.directed:  # remove opposite direction edge, to account for lack of direciton in this graph
            node2.outgoingNeighbors.removeIf(lambda x: x is node1)

    def degree(self, node1: Node):
        return node1.outgoingNeighbors.Length  # degree = number of edges

    def isOutgoingNeigbhbor(self, node1: Node, node2: Node):
        head = node1.outgoingNeighbors._head
        # search for node2 in adjecency list
        while head is not None:

            if head.value is node2:
                return True

            head = head._next
        
        return False

    def reverseEdges(self):
        if not self.directed:
            return
        
        newAdjencyLists = [None] * len(self.nodes)

        for i, node in enumerate(self.nodes):
            newAdjencyList = LinkedList()
            newNeighbors = []
            for node2 in self.nodes:
                if node is node2:
                    continue
                
                if self.isOutgoingNeigbhbor(node2, node):
                    newNeighbors.append(LinkedListNode(node2))
            
            newAdjencyList.addNodesAtTail(newNeighbors)
            newAdjencyLists[i] = newAdjencyList
        
        for i, node in enumerate(self.nodes):
            node.outgoingNeighbors = newAdjencyLists[i]


    def __str__(self) -> str:
        """
        gia ta prints
        """
        s = ""

        for i, node in enumerate(self.nodes):
            s += f"{i}: ({node.value}): "
            
            k = ""
            neighbor = node.outgoingNeighbors._head
            while neighbor is not None:
                k += f"{neighbor.value.value}->"
                neighbor = neighbor._next

            s += f"{k} \n"
        return s

if __name__ == "__main__":
    g = Graph(directed=True)
    n0 = Node(0)
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    g.addNode(n0)
    g.addNode(n1)
    g.addNode(n2)
    g.addNode(n3)
    g.addNode(n4)
    g.addNode(n5)

    g.addEdge(n0, n3)
    g.addEdge(n1, n5)
    g.addEdge(n2, n3)
    g.addEdge(n3, n5)
    print(g)

    g.removeEdge(n3, n0)


    print(g)

    g.addEdge(n1, n2)
    g.addEdge(n3, n4)
    g.addEdge(n2, n5)

    print(g)

    g.removeNode(n5)

    print(g)

    g.reverseEdges()

    print(g)