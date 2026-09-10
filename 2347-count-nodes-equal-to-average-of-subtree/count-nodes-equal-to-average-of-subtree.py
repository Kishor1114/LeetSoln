# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        pass

class Solution(object):
    def averageOfSubtree(self, root):
        def iter_dfs(root):
            result = 0
            stk = [(1, (root, [0]*2))]
            while stk:
                step, args = stk.pop()
                if step == 1:
                    node, ret = args
                    if not node:
                        continue
                    ret1, ret2 = [0]*2, [0]*2
                    stk.append((2, (node, ret1, ret2, ret)))
                    stk.append((1, (node.right, ret2)))
                    stk.append((1, (node.left, ret1)))
                elif step == 2:
                    node, ret1, ret2, ret = args
                    ret[0] = ret1[0]+ret2[0]+node.val
                    ret[1] = ret1[1]+ret2[1]+1
                    result += int(ret[0]//ret[1] == node.val)
            return result
        
        return iter_dfs(root)
        """
        :type root: TreeNode
        :rtype: int
        """
        