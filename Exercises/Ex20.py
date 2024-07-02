from _BinaryTree import BinaryTree, TreeNode


def leafCount(T: BinaryTree):
    
    if T.root is None:  # empty tree has no leaves
        return 0

    if T.root.isLeaf():  # we reached base case of a tree of 1 node, which is a leaf
        return 1

    return leafCount(BinaryTree(T.root.right)) + leafCount(BinaryTree(T.root.left))  # sum leaf count of left and right subtrees
    # current root is not a leaf since it passed the above if statement


def height(T: BinaryTree):

    if T.root is None:
        return 0

    if T.root.isLeaf():
        return 1

    return max([height(BinaryTree(T.root.right)), height(BinaryTree(T.root.left))]) + 1
    #  height of current root node, is the maximum of its left and right subtrees plus 1,
    # these subtrees exist since we passed the above if statement


def innerNodes(T: BinaryTree):

    if T.root is None or T.root.isLeaf():  # current root is not an inner node
        return 0

    return innerNodes(BinaryTree(T.root.right)) + innerNodes(BinaryTree(T.root.left)) + 1
    # sum the inner nodes of left,right subtrees and add 1, since current root is an inner node (it passed above if check)


if __name__ == "__main__":

    n1 = TreeNode(1)
    T = BinaryTree(n1)

    n2 = TreeNode(0)
    n3 = TreeNode(2)
    n4 = TreeNode(4)
    n5 = TreeNode(-1)

    n6 = TreeNode(-3)
    n7 = TreeNode(-8)

    n1.left = n2
    n1.right = n3
    n2.left = n4
    n4.right = n5
    n3.left = n6
    n3.right = n7

    print(leafCount(T))
    print(height(T))
    print(innerNodes(T))