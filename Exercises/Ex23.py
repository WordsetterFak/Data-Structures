from _BinaryTree import BinaryTree, TreeNode

def findLastLeftTurn(T: BinaryTree, node: TreeNode, lastLeftTurn: TreeNode = None) -> TreeNode:
    """
    Follow the path to given node and take note of the lastLeftTurnMade
    """
    if node is T.root:
        return lastLeftTurn

    if node.value >= T.root.value:
        return findLastLeftTurn(BinaryTree(T.root.right), node, lastLeftTurn)

    return findLastLeftTurn(BinaryTree(T.root.left), node, T.root)


def findExactGreater(T: BinaryTree, node: TreeNode) -> TreeNode:
    right = node.right

    if right is not None:
        return findLeftMostChild(right)
    
    return findLastLeftTurn(T, node)


def findLeftMostChild(node: TreeNode) -> TreeNode:
    
    while node.left is not None:  # follow left children route till it stops
        node = node.left

    return node

if __name__ == "__main__":

    n1 = TreeNode(8)
    n2 = TreeNode(3)
    n3 = TreeNode(10)
    n4 = TreeNode(1)
    n5 = TreeNode(6)
    n6 = TreeNode(14)
    n7 = TreeNode(13)
    n8 = TreeNode(4)
    n9 = TreeNode(7)

    T = BinaryTree()
    T.root = n1
    n1.left = n2
    n1.right = n3
    n3.right = n6
    n6.left = n7
    n2.left = n4
    n2.right = n5
    n5.left = n8
    n5.right = n9
    # To opoio einai binary search tree, to brhka sthn eikona ths wikipedia gia eukolia
    print(findExactGreater(T,n8).value)
    print(findExactGreater(T,n6))
    print(findExactGreater(T,n1).value)
    print(findExactGreater(T,n7).value)
    print(findExactGreater(T,n8).value)
    print(findExactGreater(T,n9).value)

