from _LinkedList import LinkedList, LinkedListNode
from _DoubleLinkedList import DoubleLinkedList, DoubleLinkedListNode
from math import floor


def stringToLinkedList(string: str) -> LinkedList:
    linkedList = LinkedList()

    linkedList.addNodesAtTail([LinkedListNode(char) for char in string])  # same as ex6

    return linkedList


def stringToDoubleLinkedList(string: str) -> DoubleLinkedList:
    doubleLinkedList = DoubleLinkedList()

    doubleLinkedList.addNodesAtTail([DoubleLinkedListNode(char) for char in string])
    
    return doubleLinkedList


def invertStringAsLinkedList(string: str):
    linkedList = stringToLinkedList(string)

    node1 = linkedList._head

    for i in range(floor(len(string) / 2)):
        
        node2 = node1
        for _ in range(len(string) - 2 * i - 1):
            node2 = node2._next

        # same as ex6.py but now instead of checking if values match, we exchange them

        swap = node1.value
        node1.value = node2.value
        node2.value = swap
        
        node1 = node1._next

    return linkedList

def invertStringAsDoubleLinkedList(string: str) -> bool:
    doubleLinkedList = stringToDoubleLinkedList(string)

    node1 = doubleLinkedList._head
    node2 = doubleLinkedList.getTail()

    for _ in range(floor(len(string) / 2)):

        # same as ex6.py but now instead of checking if values match, we exchange them

        swap = node1.value
        node1.value = node2.value
        node2.value = swap

        node1 = node1._next  # forward step
        node2 = node2._previous  # backward step
    
    return doubleLinkedList


if __name__ == "__main__":

    s1 = "ABA"
    s2 = "AB"
    s3 = "J"
    s4 = "123456789"
    s5 = "NULOPOLUN"
    s6 = "1234567890"
    s7 = "LOOL"

    sAll = [s1, s2, s3, s4, s5, s6, s7]

    for s in sAll:
        print(f"{s}: {str(invertStringAsLinkedList(s))}, {str(invertStringAsDoubleLinkedList(s))}")