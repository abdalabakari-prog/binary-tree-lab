from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    
    left_height = max_depth(root.left)
    right_height = max_depth(root.right)
    
    return max(left_height, right_height) + 1

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # BST Property: If both nodes are smaller, LCA is in the left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor(root.left, p, q)
    
    # BST Property: If both nodes are larger, LCA is in the right subtree
    if p.val > root.val and q.val > root.val:
        return lowest_common_ancestor(root.right, p, q)
    
    # If they split (one left, one right) or one matches root, this is the LCA
    return root