import math


class Queue:
    """
    More detail in latex document exercises 16 
    """

    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize  # maxsize of the queue
        self.array = [math.nan] * maxsize
        self.qfront = 0  # points to front of queue (extraction point)
        self.qrear = 0  # points to rear of queue (insertion point)
        self.length = 0
    
    def rightMove(self, pos: int) -> int:
        pos += 1
        if pos == self.maxsize:
            pos = 0
        # calculate pos + 1 mod maxsize, to allow for cyclicity of list
        return pos

    def enqueue(self, val):
        nextQrear = self.rightMove(self.qrear)

        if nextQrear == self.qfront:  # qrear can't move right
            
            if self.array[self.qrear] is math.nan:  # check if it can insert element at its current position
                self.array[self.qrear] = val
                self.length += 1
            # if not is full so we just return
            return
        
        self.array[self.qrear] = val
        self.length += 1  # update queue length
        self.qrear = nextQrear  # move right
    
    def dequeue(self):
        v = self.array[self.qfront]
        self.array[self.qfront] = math.nan
        
        if self.qrear == self.qfront:  # qfront can't move right, queue is empty or has 1 element
            if v is not math.nan:  # check if qfront position has a value if so dequeue it
                self.length -= 1

            return v
        
        self.qfront = self.rightMove(self.qfront)  # move right qfront
        self.length -= 1
        return v

    def __str__(self) -> str:
        return str(self.array)

if __name__ == "__main__":

    queue = Queue(8)
    for i in range(10):
        queue.enqueue(i)
    
    print(queue)
    for i in range(10):
        print(queue.dequeue())
    
    for i in range(10):
        queue.enqueue(i)
    
    print(queue)
    for i in range(10):
        print(queue.dequeue())
