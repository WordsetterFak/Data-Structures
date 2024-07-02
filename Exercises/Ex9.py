from _LinkedList import LinkedList, LinkedListNode

def combineLinkedLists(l1: LinkedList, l2: LinkedList):
    l1Tail = l1._head

    if l1._head is None:
        return l2  # l1 is empty, thus their union is l2

    while l1Tail._next is not None:  # travel to l1s tail 
        l1Tail = l1Tail._next

    l1Tail._next = l2._head  # link l1's tail to l2's head achieving our goal of joining both lists 

    return l1


if __name__ == "__main__":

    l = LinkedList()
    ks = LinkedListNode(3)
    ads = LinkedListNode(1)
    dsa = LinkedListNode(0)
    l.addNodesAtTail([ks, ads, dsa])
    print(str(l))

    k = LinkedList()
    j1 = LinkedListNode(-3)
    j2 = LinkedListNode(-1)
    j3 = LinkedListNode(0)
    k.addNodesAtTail([j1, j2, j3])
    print(str(k))

    print(str(combineLinkedLists(l, k)))