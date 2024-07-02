from Ex31 import *


def dfs(start: Node, visited, postVisit):
    explore(start, visited, postVisit)

def explore(node: Node, visited, postVisit):
    visited[node.index] = True

    head = node.outgoingNeighbors._head
    while head is not None:
        
        if not visited[head.value.index]:
            explore(head.value, visited, postVisit)

        head = head._next
    
    postVisit(node)

def Kosaraju(graph: Graph):
    stack = Stack()
    visited = [False] * len(graph.nodes)

    def postvisit(x: Node):
        stack.push(x)

    i = 0
    while stack.length < len(graph.nodes):
        start = graph.nodes[i]
        if visited[i]:
            i += 1
            continue
        dfs(start, visited, postvisit)
        i += 1

    graph.reverseEdges()

    added = [False] * len(graph.nodes)
    remaining = [len(graph.nodes)]
    components = []

    while stack.length != 0:
        component = []
        def post(x: Node):
            if added[x.index]:
                return

            added[x.index] = True
            remaining[0] -= 1
            component.append(x)
        
        dfs(stack.pop(), [False] * len(graph.nodes), post)
        components.append(component)

        if remaining[0] == 0:
            break

    return components
    

if __name__ == "__main__":
    
    g = Graph(directed=True)  # to grafhma ths askhshs 31

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

    stack = Stack()

    components = Kosaraju(g)    

    for i, comp in enumerate(components):
        if len(comp) == 0:
            continue

        print(f"Component {i}: ")
        for v in comp:
            print(f"{v.value}, ")