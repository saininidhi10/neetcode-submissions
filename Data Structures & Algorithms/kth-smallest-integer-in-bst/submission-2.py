# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # res = root.val
        # cnt = 0

        # def inorder(root):
        #     nonlocal res, cnt
        #     if not root:
        #         return
            
        #     inorder(root.left)
        #     cnt += 1  
        #     if cnt == k:
        #         res = root.val
        #         return
        #     inorder(root.right)

        # inorder(root)
        # return res

        # Morris traversal, O(S.C) = O(1)
        curr = root
        
        while curr:
            if not curr.left:
                k -= 1
                if k == 0:
                    return curr.val
                curr = curr.right
            else:
                pred = curr.left
                while pred.right and pred.right != curr:
                    pred = pred.right
                
                if pred.right is None:
                    pred.right = curr
                    curr = curr.left
                else:
                    pred.right = None
                    k -= 1
                    if k == 0:
                        return curr.val
                    curr = curr.right
        return -1