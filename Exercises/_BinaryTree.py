from __future__ import annotations

class TreeNode:
    
    def __init__(self, value = 0, right: TreeNode = None, left: TreeNode = None) -> None:
        self.right = right
        self.left = left
        self.value = value
    
    def isLeaf(self) -> bool:
        return self.right is None and self.left is None


class BinaryTree:

    def __init__(self, root: TreeNode = None) -> None:
        self.root = root
    
