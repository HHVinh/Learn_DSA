from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preIdx: chỉ số đang xét trong preorder
        # inIdx: chỉ số đang xét trong inorder
        preIdx = inIdx = 0

        # Hàm đệ quy để xây dựng cây
        def dfs(limit):
            nonlocal preIdx, inIdx  # Cho phép thay đổi preIdx, inIdx bên ngoài

            # Nếu đã duyệt hết preorder thì dừng
            if preIdx >= len(preorder):
                return None

            # Nếu giá trị tại inorder[inIdx] == limit nghĩa là đã đi hết 1 nhánh
            if inorder[inIdx] == limit:
                inIdx += 1  # Di chuyển sang phần tử kế tiếp trong inorder
                return None

            # Tạo node gốc mới từ preorder
            root = TreeNode(preorder[preIdx])
            preIdx += 1

            # Xây dựng cây con bên trái với giới hạn là giá trị root
            root.left = dfs(root.val)

            # Xây dựng cây con bên phải với giới hạn là limit
            root.right = dfs(limit)

            return root

        # Gọi hàm đệ quy với giới hạn ban đầu là vô cực (không giới hạn)
        return dfs(float('inf'))


# Hàm duyệt inorder để kiểm tra kết quả
def print_inorder(root: Optional[TreeNode]):
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)


if __name__ == "__main__":
    # Ví dụ: cây gốc từ preorder và inorder
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    print("Duyệt inorder của cây đã xây dựng:")
    print_inorder(root)  # Kết quả phải khớp với mảng inorder ban đầu
