from math import floor
from _Stack import Stack


def binarySearchStack(array, key) -> int:
    s = Stack()

    if len(array) == 0:
        return None

    s.push(0)
    s.push(len(array) - 1)

    while True:
        high = s.pop()  # get high index bound
        low = s.pop()  # get low index bound

        middle = floor((high + low) / 2)  # get middle of array

        if high < low:  # we have exhausted all posibilities, the key doesn't exist
            return None
        
        if array[middle] == key:
            return middle

        if array[middle] > key:  # right side of current array (ascending) (from low-high), cannot contain our key, so we ignore it
            s.push(low)  # place low and new high in this exact order
            s.push(middle - 1)
        else:  # left side of current array (ascending) (from low-high), cannot contain our key, so we ignore it
            s.push(middle + 1)  # place new low and high in this order
            s.push(high)
        
if __name__ == "__main__":

    print(binarySearchStack([0, 2, 4, 6, 8, 10, 12, 14], 4))
    print(binarySearchStack([0, 2, 4, 6, 8, 10, 12, 14], 10))
    print(binarySearchStack([0, 2, 4, 6, 8, 10, 12, 14], 0))
    print(binarySearchStack([0, 2, 4, 6, 8, 10, 12, 14], 14))
    print(binarySearchStack([0, 2, 4, 6, 8, 10, 12, 14], 3))
    print(binarySearchStack([3], 3))
    print(binarySearchStack([3, 4], 3))
    print(binarySearchStack([3, 4], 4))
    print(binarySearchStack([2, 3, 4], 4))
    print(binarySearchStack([2, 3, 4], 10))
