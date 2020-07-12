# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> [float]:
        if not root:
            return 0
        stack = [root]
        output = []
        while stack:
            stack, output = self.pop(stack, output)
        return output

    def pop(self, array, output):
        children = []
        parent = []
        while array:
            node = array.pop()
            parent.append(node.val)
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        output.append(sum(parent) / len(parent))

        return children, output

# solution from leetcode
class SolutionFast1:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return root
        que = [root]
        ans = []
        while que:
            ans.append(sum([i.val for i in que])/len(que))
            semi = []
            while que:
                temp = que.pop()
                if temp.left:
                    semi.append(temp.left)
                if temp.right:
                    semi.append(temp.right)
            que = semi
        return ans
