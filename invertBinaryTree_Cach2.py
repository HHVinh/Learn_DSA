from typing import Optional

# Định nghĩa node trong cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # Giá trị của node hiện tại
        self.left = left        # Con trái
        self.right = right      # Con phải


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Nếu cây rỗng thì trả về None
        if not root:
            return None

        # Hàm duyệt cây theo chiều sâu (DFS)
        def dfs(cur):
            if cur:
                # Đổi chỗ nhánh trái và nhánh phải
                cur.left, cur.right = cur.right, cur.left

                # Gọi đệ quy cho 2 nhánh con
                dfs(cur.left)
                dfs(cur.right)

        # Gọi hàm đệ quy bắt đầu từ node gốc
        dfs(root)

        # Trả về cây sau khi đảo
        return root


# ----------------------------------------
# Hàm phụ để in cây nhị phân theo thứ tự duyệt trước (preorder)
# ----------------------------------------
def printTree(root):
    if not root:
        return
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


# ----------------------------------------
# Tạo cây ví dụ để kiểm tra
# Cây ban đầu:
#         4
#        / \
#       2   7
#      / \ / \
#     1  3 6  9
# ----------------------------------------
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# In cây ban đầu
print("Cây ban đầu (preorder):")
printTree(root)
print("\n")

# Gọi hàm đảo cây
solution = Solution()
inverted_root = solution.invertTree(root)

# In cây sau khi đảo
print("Cây sau khi đảo (preorder):")
printTree(inverted_root)
print()
