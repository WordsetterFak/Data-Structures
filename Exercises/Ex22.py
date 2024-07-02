from _BinaryTree import BinaryTree, TreeNode

def leastSubtree(T: BinaryTree, node1: TreeNode, node2: TreeNode) -> BinaryTree:
    node2InNextSubtree = True

    while node2InNextSubtree:
        next = None
        node2InNextSubtree = False

        if node1 is T.root or node2 is T.root:  # An pesoume panw se enan anagkastika den mporoume na paroume kapoio ypodentro
            return T

        if node1.value >= T.root.value and node2.value >= T.root.value:  # koitame an einai kai oi dyo sto deksi ypodentro tou trexwn root
            next = T.root.right
            node2InNextSubtree = True
        
        elif node1.value < T.root.value and node2.value < T.root.value:  # koitame an einai kai oi dyo sto aristero ypodentro tou trexwn root
            next = T.root.left
            node2InNextSubtree = True

        if node2InNextSubtree:  # an True, einai sto idio ara pame se poio mikro ypodentro, poy gnwrizoume oti periexei tous kombous
            T = BinaryTree(next)

    return T
    

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

    print(leastSubtree(T, n8, n9).root.value)
    print(leastSubtree(T, n5, n2).root.value)
    print(leastSubtree(T, n2, n3).root.value)
