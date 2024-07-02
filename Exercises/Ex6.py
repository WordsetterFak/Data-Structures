from _LinkedList import LinkedList, LinkedListNode
from _DoubleLinkedList import DoubleLinkedList, DoubleLinkedListNode
from math import floor


def stringToLinkedList(string: str) -> LinkedList:
    linkedList = LinkedList()

    linkedList.addNodesAtTail([LinkedListNode(char) for char in string])  # use this method and list comprehension to
    # create linked list with elements the characters of the string

    return linkedList


def stringToDoubleLinkedList(string: str) -> DoubleLinkedList:
    doubleLinkedList = DoubleLinkedList()

    doubleLinkedList.addNodesAtTail([DoubleLinkedListNode(char) for char in string])
    
    return doubleLinkedList


def isPalindromeLinkedList(string: str):
    linkedList = stringToLinkedList(string)

    node1 = linkedList._head

    for i in range(floor(len(string) / 2)):  # run for every element till the middle (inclusive if len(string) = 2k else exclusive)
        # we don't need to check again the other half obviously
        
        node2 = node1
        for _ in range(len(string) - 2 * i - 1):  # travel till the symmetric element at position |s| - i - 1 from position i
            node2 = node2._next

        if node2.value != node1.value:  # check if values match
            return False  # word is not a palindrome!
        
        node1 = node1._next  # move on to the next

    return True

def isPalindromeDoubleLinkedList(string: str) -> bool:
    doubleLinkedList = stringToDoubleLinkedList(string)

    node1 = doubleLinkedList._head
    node2 = doubleLinkedList.getTail()

    for _ in range(floor(len(string) / 2)):  # same as before

        if node1.value != node2.value:
            return False

        node1 = node1._next  # step forward to i+1 element
        node2 = node2._previous  # step backward to i-1 element
        # thus we already found the next 2 symmetric nodes, in i and |s| - i - 1 positions
    
    return True


if __name__ == "__main__":

    s1 = "ABA"
    s2 = "AB"
    s3 = "J"
    s4 = "123456789"
    s5 = "NULOPOLUN"
    s6 = "1234567890"
    s7 = "LOOL"
    s8 = "Roma-Olina-Milo-Amor"

    sAll = [s1, s2, s3, s4, s5, s6, s7, s8]

    for s in sAll:
        print(f"{s}: {isPalindromeLinkedList(s)}, {isPalindromeDoubleLinkedList(s)}")