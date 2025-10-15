from typing import Optional

# Định nghĩa cấu trúc node cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Hàm DFS kiểm tra tính hợp lệ của cây
        def dfs(node, left, right):
            # Nếu node rỗng => hợp lệ
            if not node:
                return True
            
            # Nếu giá trị node vi phạm điều kiện BST => sai
            if not (left < node.val < right):
                return False
            
            # Duyệt đệ quy cây con trái và phải
            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
        
        # Gọi DFS từ gốc, với khoảng giá trị vô cùng
        return dfs(root, float('-inf'), float('inf'))

# -------------------------------
# 🌳 Tạo ví dụ test:
# Cây hợp lệ:
#       5
#      / \
#     3   7
#    / \   \
#   2  4   8

root1 = TreeNode(5)
root1.left = TreeNode(3, TreeNode(2), TreeNode(4))
root1.right = TreeNode(7, None, TreeNode(8))

# Cây không hợp lệ (node 6 nằm bên phải 5 nhưng nhỏ hơn 7):
#       5
#      / \
#     3   7
#        /
#       6
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(7, TreeNode(6))

# -------------------------------
# 🧪 Kiểm tra:
sol = Solution()
print("Cây 1 hợp lệ BST?", sol.isValidBST(root1))  # ✅ True
print("Cây 2 hợp lệ BST?", sol.isValidBST(root2))  # ❌ False
