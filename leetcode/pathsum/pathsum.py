# https://leetcode.com/problems/path-sum/
class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        else:
            # Only leaf could return true
            if targetSum == root.val and root.left is None and root.right is None:
                return True
            else:
                return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
