# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def preorder(root, arr):
            if not root:
                return
            if root != None:
                arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)
            
        def change(root, arr, i):
            if i < len(arr):
                root.left = None
                root.val = arr[i]
            
                if root.right:
                    change(root.right, arr, i+1)
                    
                elif i<len(arr)-1:
                    root.right = TreeNode()
                    change(root.right, arr, i+1)

        arr = []
        i = 0
        preorder(root, arr)
        change(root, arr, i)
                