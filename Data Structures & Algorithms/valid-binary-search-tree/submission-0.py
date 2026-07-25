# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node,maxval,minval):
            if node is None:
                return True
            if node.val>=maxval or node.val<=minval:
                return False
            return(valid(node.right,maxval,node.val) and valid(node.left,node.val,minval))
        return valid(root,float('inf'),float('-inf'))
        