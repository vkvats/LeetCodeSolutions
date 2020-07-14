# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [root]
        combinations = []
        while stack:
            stack, combinations = self.visit(stack, combinations)
        # return combinations
        sum_ = 0
        for binary in combinations:
            sum_ += int(binary, 2)
        return sum_

    def visit(self, array, combi):
        tmp_combi = []
        tmp_array = []
        while array:
            node = array.pop()
            if combi:
                # this part is making more then required combinations.
                # apparently twice the combination needed
                for val in combi:
                    new_val = val + str(node.val)
                    tmp_combi.append(new_val)
            if not combi:
                tmp_combi.append(str(node.val))

            if node.right:
                tmp_array.append(node.right)
            if node.left:
                tmp_array.append(node.left)

        return tmp_array, tmp_combi

# Solution from discussion
class SolutionDiscussion:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.total = 0
        node = root
        stack = []
        stack.append((node, node.val))
        while stack:
            node, temp = stack.pop()
            if not node.left and not node.right:
                # this is only adding the last digit of the binary, This doesn't require
                # converting the binary into decimal as last digit has same value as binary value.
                self.total += temp

            if node.right:
                # converting binary into decimal with temp*2
                # every time the node is not leaf node, then temp value is multiplied with
                # 2, so with each level, multiplication with 2 takes place.
                stack.append((node.right, temp*2+node.right.val))
            if node.left:
                stack.append((node.left, temp*2+node.left.val))
        return self.total

# from leetcode
class SolutionFast1:
    def sumRootToLeaf(self, root, val=0):
        if not root:
            return 0
        # this is also converting binary into decimal at each level.
        val = val * 2 + root.val
        if root.left == root.right:
            return val
        return self.sumRootToLeaf(root.left, val) + self.sumRootToLeaf(root.right, val)


class SolutionFast2:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths=[]
        def dfs(root,path):
            if root:
                path=path+str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                dfs(root.left,path)
                dfs(root.right,path)
        dfs(root,"")
        def decimal(num_str):
            num_str=num_str[::-1]
            sum1=0
            for x in range(0,len(num_str)):
                sum1=sum1+(2**x)*int(num_str[x])
            return sum1
        out=0
        for p in paths:
            deci=decimal(p)
            out=out+deci
        return out