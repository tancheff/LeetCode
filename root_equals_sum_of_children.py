# Build the following binary tree
#       20
#      /  \
#     5    15
#    / \     \
#   2   6     20
#
# include a method to check if the children equal the value of the parent.

from typing import Optional

class TreeNode(object):
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(20)
root.left = TreeNode(5)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)
root.right = TreeNode(15)
root.right.right = TreeNode(20)


class Solution:
    def check_tree(self, root: Optional[TreeNode]) -> bool:
        return root.value == root.left.value + root.right.value


solution = Solution()

print(solution.check_tree(root))