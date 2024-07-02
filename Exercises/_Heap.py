import math

class Heap:
    # maxHeap
    # values were improperly not encapsulated within a node, so that a value and a priority can be held, due to time
    # limitations it was left this way, more on exercise 25 in the latex document

    def __init__(self, maxLevel) -> None:
        self.maxSize = 2 ** maxLevel
        self.array = [-math.inf] * (self.maxSize - 1)  # size of 2^n - 1
        self.last = 1  # points to last inserted element, using 1...2^n enumeration
    
    def getValueAt(self, pos):
        # adjust between 1...2^n enumeration, to 0...2^n - 1 enumeration (actual enumeration in the array)
        return self.array[pos - 1]

    def setValueAt(self, pos, value):
        self.array[pos - 1] = value

    def parent(self, pos):
        # get the parent of the element at position pos, in 1...2^n enumeration
        return math.floor(pos / 2)

    def rightChild(self, pos):
        # get the right child of the element at pos, in 1...2^n enumeration
        return 2 * pos + 1
    
    def leftChild(self, pos):
        # get the left child of the element at pos, in 1...2^n enumeration
        return 2 * pos

    @property
    def isEmpty(self):
        return self.array[0] == -math.inf
    
    @property
    def lastPos(self):
        # last available position in 1...2^n enumeration
        return len(self.array)

    def exchange(self, pos1, pos2):
        # exchange values between pos1, pos2 nodes
        temp = self.getValueAt(pos2)
        self.setValueAt(pos2, self.getValueAt(pos1))
        self.setValueAt(pos1, temp)

    def insert(self, value):

        if self.isEmpty:
            self.array[0] = value
            return

        if self.last == self.lastPos:  # Heap is full
            return

        self.last += 1
        self.setValueAt(self.last, value)
        self.heapifyUp(self.last)
    
    def heapifyUp(self, pos):
        
        if pos == 1:
            return
        
        parent = self.parent(pos)

        if self.getValueAt(parent) < self.getValueAt(pos):  # exchange elements, and continue recursion, to fix maxHeap property
            self.exchange(pos, parent)
            self.heapifyUp(parent)

    def popRoot(self):

        if self.isEmpty:
            return None
        
        v = self.getValueAt(1)

        if self.last == 1:  # heap contains only root
            self.setValueAt(1, -math.inf)
            return v

        self.setValueAt(1, self.getValueAt(self.last))
        self.setValueAt(self.last, -math.inf)
        self.last -= 1
        self.heapifyDown(1)
        return v

    def heapifyDown(self, pos):
        
        leftChildPos = self.leftChild(pos)
        rightChildPos = self.rightChild(pos)

        maxChildPos = rightChildPos if self.getValueAt(rightChildPos) > self.getValueAt(leftChildPos) else leftChildPos  
        # find child with biggest value to exchange, so heap property is fixed
        # prefer leftward movement so the tree remains left side dominant

        if self.getValueAt(maxChildPos) <= self.getValueAt(pos):  # heap property was fixed so recursion may stop 
            return

        self.exchange(maxChildPos, pos)
        self.heapifyDown(maxChildPos)  # move on the next level



if __name__ == "__main__":

    heap = Heap(3)
    for i in range(8):
        heap.insert(i)

    print(heap.array)
    print(heap.last)
    print("----")
    for i in range(8):
        print(heap.popRoot())
        print(heap.array)
        print(heap.last)
    
    for i in range(8):
        heap.insert(i)

    print("----")
    print(heap.array)