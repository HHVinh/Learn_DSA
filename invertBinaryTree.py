from typing import Optional
from collections import deque

# Định nghĩa node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        stack = [root]
        while stack:
            node = stack.pop()
            # Đổi chỗ trái <-> phải
            node.left, node.right = node.right, node.left
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root


# ==============================
# HÀM HỖ TRỢ
# ==============================

# Tạo cây nhị phân từ list (level-order), dùng None cho chỗ trống
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

# In cây nhị phân dạng level-order
def print_tree(root):
    if not root:
        print("[]")
        return
    q = deque([root])
    res = []
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # Xoá None dư thừa ở cuối
    while res and res[-1] is None:
        res.pop()
    print(res)


# ==============================
# CHẠY THỬ
# ==============================
if __name__ == "__main__":
    # Nhập cây: ví dụ [4,2,7,1,3,6,9]
    # Cây gốc:
    #       4
    #      / \
    #     2   7
    #    / \ / \
    #   1  3 6  9
    arr = list(map(int, input("Nhập các giá trị node cách nhau bởi dấu cách (ví dụ: 4 2 7 1 3 6 9): ").split()))
    root = build_tree(arr)

    print("Cây ban đầu (level-order):")
    print_tree(root)

    sol = Solution()
    root = sol.invertTree(root)

    print("Cây sau khi đảo ngược (level-order):")
    print_tree(root)
