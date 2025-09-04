from collections import deque
from typing import Optional

# Định nghĩa node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # giá trị của node
        self.left = left      # con trái
        self.right = right    # con phải

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # Cây rỗng thì mặc định là BST hợp lệ

        # Khởi tạo hàng đợi với 1 phần tử ban đầu: (root, -∞, +∞)
        # Nghĩa là: kiểm tra node gốc trong khoảng (-∞, +∞)
        q = deque([(root, float("-inf"), float("inf"))])

        while q:
            # Lấy ra công việc cần kiểm tra
            node, left, right = q.popleft()

            # Nếu giá trị node không nằm trong khoảng hợp lệ -> sai
            if not (left < node.val < right):
                return False

            # Nếu có con trái, thêm công việc kiểm tra con trái
            # Khoảng hợp lệ: (left, node.val)
            if node.left:
                q.append((node.left, left, node.val))

            # Nếu có con phải, thêm công việc kiểm tra con phải
            # Khoảng hợp lệ: (node.val, right)
            if node.right:
                q.append((node.right, node.val, right))

        # Nếu duyệt hết mà không sai -> đúng
        return True


# ------------------------
# Tạo cây ví dụ để test
# ------------------------

# Cây hợp lệ (BST đúng)
#       10
#      /  \
#     5    15
#         /  \
#        11   20
valid_root = TreeNode(10)
valid_root.left = TreeNode(5)
valid_root.right = TreeNode(15, TreeNode(11), TreeNode(20))

# Cây không hợp lệ (BST sai)
#       10
#      /  \
#     5    15
#         /
#        6   <-- sai vì 6 < 10 nhưng lại ở bên phải 10
invalid_root = TreeNode(10)
invalid_root.left = TreeNode(5)
invalid_root.right = TreeNode(15, TreeNode(6), None)

# ------------------------
# Chạy thử
# ------------------------
sol = Solution()

print("Cây hợp lệ:", sol.isValidBST(valid_root))     # True
print("Cây không hợp lệ:", sol.isValidBST(invalid_root))  # False
