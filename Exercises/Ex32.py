from _DoubleLinkedList import DoubleLinkedList, DoubleLinkedListNode
from Ex31 import *


def hasCycleFrom(start: Node, graph: Graph):

    visited = [False] * len(graph.nodes)
    visited[start.index] = True
    s = Stack()
    s.push(start)

    while s.length > 0:
        v: Node = s.pop()  # pop first element of the stack

        head = v.outgoingNeighbors._head
        while head is not None:
            
            if visited[head.value.index]:  # back edge found!
                return True

            if not visited[head.value.index]:
                visited[head.value.index] = True
                s.push(head.value)  # place the node on the stack

            head = head._next

    return False

def hasCycle(graph: Graph):

    for node in graph.nodes:  # try to find a cycle from every node
        
        if hasCycleFrom(node, graph):
            return True
    
    return False


if __name__ == "__main__":
    
    g = Graph(directed=True)

    u1 = Node(1)
    u2 = Node(2)
    u3 = Node(3)
    u4 = Node(4)
    u5 = Node(5)
    u6 = Node(6)
    u7 = Node(7)
    u8 = Node(8)
    u9 = Node(9)

    g.addNode(u1)
    g.addNode(u2)
    g.addNode(u3)
    g.addNode(u4)
    g.addNode(u5)
    g.addNode(u6)
    g.addNode(u7)
    g.addNode(u8)
    g.addNode(u9)

    g.addEdge(u1, u3)
    g.addEdge(u1, u5)
    g.addEdge(u1, u2)
    g.addEdge(u1, u4)
    g.addEdge(u2, u4)
    g.addEdge(u2, u1)
    g.addEdge(u2, u3)
    g.addEdge(u3, u2)
    g.addEdge(u3, u1)
    g.addEdge(u3, u4)
    g.addEdge(u4, u1)
    g.addEdge(u4, u2)
    g.addEdge(u4, u3)
    g.addEdge(u5, u6)
    g.addEdge(u5, u7)
    g.addEdge(u6, u5)
    g.addEdge(u6, u7)
    g.addEdge(u7, u5)
    g.addEdge(u7, u6)

    g.addEdge(u8, u3)
    g.addEdge(u8, u4)
    g.addEdge(u8, u9)

    print(hasCycleFrom(u1, g))
    print(hasCycle(g))

    g2 = Graph(directed=True)

    v1 = Node(1)
    v2 = Node(1)
    v3 = Node(1)
    v4 = Node(1)

    g2.addNode(v1)
    g2.addNode(v2)
    g2.addNode(v3)
    g2.addNode(v4)

    g2.addEdge(v1, v2)
    g2.addEdge(v2, v4)
    g2.addEdge(v3, v1)

    print(hasCycleFrom(v1, g2))
    print(hasCycle(g2))
