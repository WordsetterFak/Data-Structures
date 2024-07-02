from _GraphAdjLi import Graph, Node
from _Stack import Stack
from _Queue import Queue

# classic dfs, bfs implementations

def dfs(start: Node, graph: Graph, onVisit):
    visited = [False] * len(graph.nodes)
    visited[start.index] = True
    s = Stack()
    s.push(start)

    while s.length > 0:
        v: Node = s.pop()  # pop first element of the stack
        onVisit(v)

        head = v.outgoingNeighbors._head
        while head is not None:
            
            if not visited[head.value.index]:
                visited[head.value.index] = True
                s.push(head.value)  # place the node on the stack

            head = head._next


def bfs(start: Node, graph: Graph, onVisit):
    visited = [False] * len(graph.nodes)
    visited[start.index] = True
    s = Queue(len(graph.nodes))
    s.enqueue(start)

    while s.length > 0:
        v: Node = s.dequeue()  # take first element in line
        onVisit(v)

        head = v.outgoingNeighbors._head
        while head is not None:
            
            if not visited[head.value.index]:
                visited[head.value.index] = True
                s.enqueue(head.value)  # place the node on the queue

            head = head._next


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

    def p(n):
        print(n.value)

    dfs(u1, g, p)
    
    print("----")
    dfs(u8, g, p)
    print("----")
    bfs(u1, g, p)
    print("----")
    bfs(u8, g, p)