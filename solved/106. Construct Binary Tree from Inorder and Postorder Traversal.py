# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if inorder and postorder:
            node_val = postorder.pop()
            node = TreeNode(node_val)
            val_index = inorder.index(node_val)
            left_sub = inorder[: val_index]
            right_sub = inorder[val_index + 1 :]
            node.right = self.buildTree(right_sub, postorder)
            node.left = self.buildTree(left_sub, postorder)
            return node
        else:
            return None

# Solution from leetcode (recursive, dictionary)
class SolutionF1:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        inorder_map = {}
        for i, v in enumerate(inorder):
            inorder_map[v] = i
        k = -1

        def dfs(low, high):
            nonlocal k
            if low > high: return None
            root = TreeNode(postorder[k])
            k -= 1
            index = inorder_map[root.val]
            root.right = dfs(index + 1, high)
            root.left = dfs(low, index - 1)

            return root

        return dfs(0, len(inorder) - 1)

class SolutionF2:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        dict1={v:k for k,v  in enumerate(inorder)}
        i,n=0,len(postorder)
        postorder.reverse()
        def tra(l,r):
            nonlocal i
            if i==n or l>r:return None
            a=dict1[postorder[i]]
            if a<l and a>r:return None
            root=TreeNode(postorder[i])
            i+=1
            root.right=tra(a+1,r)
            root.left=tra(l,a-1)
            return root
        return tra(0,n-1)



if __name__ == '__main__':
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    sol = Solution().buildTree(inorder, postorder)
    print(sol)