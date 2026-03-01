# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Trường hợp cơ bản: Nếu cây trống, trả về danh sách rỗng
        if not root:
            return []
        
        res = []    # Danh sách chứa kết quả cuối cùng
        stack = []  # Ngăn xếp để lưu lại các node "đang chờ" xử lý gốc và bên phải
        cur = root  # Con trỏ 'cur' dùng để duyệt qua các node

        # Vòng lặp chính: Chạy khi vẫn còn node để thăm hoặc còn node trong stack
        while cur or stack:
            
            # 1. Cố gắng đi sâu nhất có thể về phía bên TRÁI
            while cur:
                stack.append(cur) # Cất node hiện tại vào stack để quay lại sau
                cur = cur.left    # Di chuyển sang con bên trái
            
            # Khi không thể sang trái được nữa (cur là None):
            
            # 2. Lấy node vừa cất gần nhất ra khỏi stack (đây chính là GỐC của cây con hiện tại)
            cur = stack.pop()
            res.append(cur.val)   # Thêm giá trị của GỐC vào kết quả
            
            # 3. Bây giờ chuyển hướng sang bên PHẢI của node vừa lấy ra
            # Nếu bên phải có node, vòng lặp 'while cur' ở trên sẽ lại lặp lại cho nhánh phải đó
            cur = cur.right
            
        return res

if __name__ == "__main__":
    # Tạo cây nhị phân từ ví dụ
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.inorderTraversal(root)
    print(result)  # Output: [1, 3, 2]  