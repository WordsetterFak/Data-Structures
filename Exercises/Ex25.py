from _Heap import Heap
from typing import Any
import random
import math

class PriorityQueue:
    """
    Dioti to Heap den exei ikanothta na labei zeugaria value, priority pairs "kleboume" me ena dict O(1) xronou me hashing,
    apla prepei ta priorities na einai ksexorista! Logw periorismenou xronou den ftiaxthke
    """

    def __init__(self, maxHeapHeight: int = 10) -> None:
        self._heap = Heap(maxHeapHeight)
        self.priorityToValue: dict[float, Any] = {}  # to save dev time

    def enqueue(self, value, priority: float):
        self._heap.insert(priority)
        self.priorityToValue[priority] = value

    def dequeue(self):
        prio = self._heap.popRoot()
        return self.priorityToValue.pop(prio)


if __name__ == "__main__":

    queue = PriorityQueue()
    queue.enqueue("Jake", 0)
    queue.enqueue("Mike", 10.2)
    queue.enqueue("Josh", -3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
