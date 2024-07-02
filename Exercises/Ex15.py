from _Stack import Stack

def recursiveLucasAlg(n: int):

    if n == 0:
        return 2
    
    if n == 1:
        return 1
    
    return recursiveLucasAlg(n - 1) + recursiveLucasAlg(n - 2)

def stackLucasAlg(n):
    
    stack = Stack()
    stack.push(2)

    if n > 0:  # if n = 0, for loop won't execute and we want 2 popped not 1, since L(0) = 2
        stack.push(1)

    for _ in range(n - 1):
        cur = stack.pop()  # retrieve L(i-1), first in stack
        old = stack.pop()  # retrieve L(i-2), second in stack
        new = cur + old  # calculate L(i) = L(i-1) + L(i-2)
        stack.push(old)  # place L(i-2)
        stack.push(cur)  # place L(i-1)
        stack.push(new)  # place L(i)
        # now L(i) is in first place and L(i-1) is in second, we are now ready for next step
    
    return stack.pop()  # return value on top, L(n)


if __name__ == "__main__":

    print(stackLucasAlg(4))