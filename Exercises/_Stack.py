from _LinkedList import LinkedList, LinkedListNode

class Stack:

    def __init__(self) -> None:
        self._list = LinkedList()
        self.length = 0

    def push(self, value):
        self.length += 1
        self._list.addAtHead(LinkedListNode(value))
    
    def pop(self):
        self.length -= 1
        return self._list.removeAtHead().value

if __name__ == "__main__":

    s = Stack()
    s.push(2)
    s.push(4)
    print(s.pop())
    print(s.pop())