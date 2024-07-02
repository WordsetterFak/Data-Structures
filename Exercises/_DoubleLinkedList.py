from __future__ import annotations

class DoubleLinkedListNode:
    
    def __init__(self, value, next: DoubleLinkedListNode = None, previous: DoubleLinkedListNode = None) -> None:
        self.value = value
        self._next = next
        self._previous = previous
    
    def connectInFront(self, other: DoubleLinkedListNode):
        """
        Adds other node as next to this node, and this node as previous to the other node
        """
        self._next = other
        if other is not None:
            other._previous = self


class DoubleLinkedList:

    def __init__(self, head: DoubleLinkedListNode = None) -> None:
        self._head = head

    def addAtHead(self, node: DoubleLinkedListNode):
        node._next = self._head

        if self._head is not None:
            self._head._previous = node

        self._head = node

    def addAtIndex(self, new_node: DoubleLinkedListNode, index: int) -> bool:

        if index == 0:
            return self.addAtHead(new_node)
        
        node = self._head

        if node is None:
            return False

        while node._next is not None and index - 1 > 0:  # taksideuoume mexri to index h to telos
            index -= 1
            node = node._next

        if index > 1:  # reached the tail before the index, thus it is out of range
            return False
        
        new_node._previous = node  # ftiaxnoume deiktes gia na mpei o kombos mas
        new_node._next = node._next

        if node._next is not None:
            node._next._previous = new_node

        node._next = new_node

        return True

    def addNodesAtTail(self, nodes: list[DoubleLinkedListNode]):

        if len(nodes) == 0:
            return

        tail = self.getTail()

        prev_node = tail

        if prev_node is None:  # empty list case
            prev_node = nodes[0]
            self._head = prev_node
            nodes = nodes[1:]

        for node in nodes:
            prev_node._next = node
            node._previous = prev_node
            prev_node = node

    def getTail(self) -> DoubleLinkedListNode:
        node = self._head
        
        if node is None:
            return None

        while node._next is not None:  # taksideuoume mexri to na broume kombo xwris diadoxo
            node = node._next
        
        return node

    def removeAtHead(self) -> DoubleLinkedListNode:
        head = self._head
        self._head = self._head._next
        self._head._previous = None
        return head

    def removeAtIndex(self, index: int) -> DoubleLinkedList:

        if index == 0:
            return self.removeAtHead()
        
        node = self._head

        while index > 1 and node._next is not None:  # proxwrame mexri ton prohgoymeno kombo apo auton pou diagrafoume h thn oura
            node = node._next
            index -= 1
        
        if node._next is None:  # index out of range, ftasame sthn oura prin to index ara den yparxei
            return None

        nodeToDelete = node._next  # allazoume deiktes
        node._next = nodeToDelete._next

        if node._next is not None:
            node._next._previous = node

        return nodeToDelete

    @property
    def Length(self):
        node = self._head
        counter = 0

        while node is not None:
            node = node._next
            counter += 1
        
        return counter
    

    def __str__(self) -> str:
        """
        Gia ta prints
        """
        node = self._head
        string = ""

        while node is not None:
            string += str(node.value) + "<->"
            node = node._next
        
        return string[:-3]


if __name__ == "__main__":
    l = DoubleLinkedList()
    ks = DoubleLinkedListNode(3)
    l.addAtHead(ks)
    print(str(l))
    ads = DoubleLinkedListNode(1)
    dsa = DoubleLinkedListNode(0)
    l.addNodesAtTail([ads, dsa])
    print(str(l))
    print(l.Length)
    ks1 = DoubleLinkedListNode(-3)
    ads1 = DoubleLinkedListNode(-1)
    dsa1 = DoubleLinkedListNode(10)
    l.addNodesAtTail([ks1, ads1, dsa1])
    print(l.getTail().value)
    print(str(l))
    l.addAtIndex(DoubleLinkedListNode(-100), 2)
    print(str(l))
    l.addAtIndex(DoubleLinkedListNode(21), 21)
    print(str(l))
    l.addAtIndex(DoubleLinkedListNode(32), l.Length)
    print(str(l))
    l.addAtIndex(DoubleLinkedListNode(-25), 0)
    print(str(l))
    l.removeAtIndex(8)
    print(str(l))

    n = l.getTail()
    while n is not None:
        print(n.value)
        n = n._previous
    