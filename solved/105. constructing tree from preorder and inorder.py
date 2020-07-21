# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if preorder and inorder:
            node_val = preorder.pop(0)
            node = TreeNode(node_val)
            val_index = inorder.index(node_val)
            left_sub = inorder[: val_index]
            right_sub = inorder[val_index + 1 :]
            node.left = self.buildTree(preorder, left_sub)
            node.right = self.buildTree(preorder, right_sub)
            return node
        else:
            return None

# Solution from leetcode (recursive)
class SolutionFast1:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        loc={v:i for i,v in enumerate(inorder)}
        def construct(pre,l,r):
            if r<=l :
                return
            root=TreeNode(pre.pop(0))
            i=loc[root.val]
            root.left=construct(pre,l,i)
            root.right=construct(pre,i+1,r)
            return root
        return construct(preorder,0,len(inorder))

# Solution from leetcode


if __name__ == '__main__':
    preorder = [3,1,2,4]
    inorder = [1,2,3,4]
    sol = Solution().buildTree(preorder, inorder)
