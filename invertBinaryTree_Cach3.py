from typing import Optional
from collections import deque  # cần import để dùng hàng đợi deque

# Định nghĩa node trong cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # giá trị của node
        self.left = left        # con trái
        self.right = right      # con phải

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Nếu cây rỗng thì không cần làm gì, trả về None
        if not root:
            return None
        
        # Tạo hàng đợi (queue) để duyệt BFS
        q = deque([root])  # ban đầu chỉ có node gốc
        
        # Lặp cho đến khi hàng đợi rỗng
        while q:
            # Lấy node ở đầu hàng đợi ra xử lý
            node = q.popleft()

            if node:
                # Đổi chỗ 2 nhánh trái và phải
                node.left, node.right = node.right, node.left
            
                # Thêm các node con vào hàng đợi để xử lý tiếp
                q.append(node.left)
                q.append(node.right)

        # Sau khi đảo xong toàn bộ cây, trả về node gốc (root)
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
