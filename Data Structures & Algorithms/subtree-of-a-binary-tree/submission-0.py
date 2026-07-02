from typing import Optional

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Helper function to check if two trees are identical
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            # Call the inner function directly without using 'self'
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
        # If the main tree is empty, it cannot contain a subRoot (unless subRoot is also empty)
        if not root:
            return False
            
        # Check if identical here, OR recursively check left/right subtrees
        if isSameTree(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
