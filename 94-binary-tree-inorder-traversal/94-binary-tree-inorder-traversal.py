# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 迭代
        # 中序遍历 先遍历左子树->根节点->右子树
        # 如果是递归做法则递归遍历左子树，访问根节点，递归遍历右子树
        # 非递归过程即:先访问..最左子树..结点，再访问其父节点，再访问其兄弟
        # while循环条件 中序遍历需先判断当前结点是否存在，若存在则将该节点放入栈中，再将当前结点设置为结点的左孩子，
        # 若不存在则取栈顶元素为cur，当且仅当栈空cur也为空，循环结束。
        stack = []
        res = []
        cur = root
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res