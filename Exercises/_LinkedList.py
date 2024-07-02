from __future__ import annotations

class LinkedListNode:
    
    def __init__(self, value, next: LinkedListNode = None) -> None:
        self.value = value
        self._next = next

class LinkedList:

    def __init__(self, head: LinkedListNode = None) -> None:
        self._head = head

    def addAtHead(self, node: LinkedListNode):
        node._next = self._head
        self._head = node
        return True

    def addAtIndex(self, new_node: LinkedListNode, index: int) -> bool:

        if index == 0:
            return self.addAtHead(new_node)
        
        node = self._head

        if node is None:
            return False

        while node._next is not None and index - 1 > 0:  # travel till the previous element of given index or tail
            index -= 1
            node = node._next

        if index > 1:  # reached the tail before the index, thus it is out of range
            return False
        
        new_node._next = node._next
        node._next = new_node
        return True
    
    def addNodesAtTail(self, nodes: list[LinkedListNode]):

        if len(nodes) == 0:
            return

        tail = self.getTail()

        prev_node = tail

        if prev_node is None:  # empty list
            prev_node = nodes[0]
            self._head = prev_node
            nodes = nodes[1:]

        for node in nodes:
            prev_node._next = node
            prev_node = node

    def getTail(self) -> LinkedListNode:
        node = self._head
        
        if node is None:
            return None

        while node._next is not None:  # travel till a node with no successor, the tail
            node = node._next
        
        return node

    def removeAtHead(self) -> LinkedListNode:
        head = self._head
        self._head = self._head._next
        return head

    def removeAtIndex(self, index: int) -> LinkedListNode:

        if index == 0:
            return self.removeAtHead()
        
        node = self._head

        while index > 1 and node._next is not None:  # travel till the previous element of given index or tail
            node = node._next
            index -= 1
        
        if node._next is None:  # index out of range
            return None

        nodeToDelete = node._next
        node._next = nodeToDelete._next
        return nodeToDelete

    def removeIf(self, predicate):

        node = self._head

        if node is None:
            return
        
        if predicate(node.value):  # check if head is to be removed
            self.removeAtHead()
            self.removeIf(predicate)  # recursion to ensure head is not to be removed predicate(head.value) = False!
            return
        
        previousNode = self._head  # previous valid node (it's valid due to above recursion)
        node = previousNode._next

        if node is None:  # list only contains head
            return

        while node._next is not None:  # while we are not on the tail
            
            if predicate(node.value):  # link previous valid node to next node, so this one is lost
                previousNode._next = node._next
            else:
                previousNode = node  # this node is valid, thus we can safely keep it

            node = node._next  # move on to the next node
        
        if predicate(node.value):  # check if tail should be kept
            previousNode._next = None

    @property
    def Length(self):
        node = self._head
        counter = 0

        while node is not None:
            node = node._next
            counter += 1
        
        return counter

    def __str__(self) -> str:
        node = self._head
        string = ""

        while node is not None:
            string += str(node.value) + "->"
            node = node._next
        
        return string[:-2]

if __name__ == "__main__":
    l = LinkedList()
    ks = LinkedListNode(3)
    l.addAtHead(ks)
    print(str(l))
    ads = LinkedListNode(1)
    dsa = LinkedListNode(0)
    l.addNodesAtTail([ads, dsa])
    print(str(l))
    print(l.Length)
    ks1 = LinkedListNode(-3)
    ads1 = LinkedListNode(-1)
    dsa1 = LinkedListNode(10)
    l.addNodesAtTail([ks1, ads1, dsa1])
    print(l.getTail().value)
    print(str(l))
    l.addAtIndex(LinkedListNode(-100), 2)
    print(str(l))
    l.addAtIndex(LinkedListNode(21), 21)
    print(str(l))
    l.addAtIndex(LinkedListNode(32), l.Length)
    print(str(l))
    l.addAtIndex(LinkedListNode(-25), 0)
    print(str(l))
    l.removeAtHead()
    l.removeAtIndex(7)
    l.addNodesAtTail([LinkedListNode(4)])
    l.addAtHead(LinkedListNode(1))
    l.addAtHead(LinkedListNode(6))
    l.addAtHead(LinkedListNode(0))
    l.addNodesAtTail([LinkedListNode(1), LinkedListNode(2)])
    print(str(l))
    l.removeIf(lambda x: x % 2 == 0)
    print(str(l))
