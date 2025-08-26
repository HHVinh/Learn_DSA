from typing import Optional
from collections import deque

# Định nghĩa node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = deque()  # dùng queue để duyệt theo level (BFS)
        if root:
            q.append(root)  # thêm node gốc vào hàng đợi nếu không rỗng

        level = 0  # biến đếm số tầng (độ sâu)
        while q:  # còn node để duyệt
            for i in range(len(q)):  # duyệt hết các node trong 1 level
                node = q.popleft()  # lấy node ra
                if node.left:       # nếu có con trái thì thêm vào queue
                    q.append(node.left)
                if node.right:      # nếu có con phải thì thêm vào queue
                    q.append(node.right)
            level += 1  # sau khi duyệt xong 1 tầng thì tăng level lên
        return level  # trả về độ sâu tối đa


# ==============================
# HÀM HỖ TRỢ
# ==============================

def build_tree(values):  # xây dựng cây từ list level-order
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


# ==============================
# CHẠY THỬ
# ==============================
if __name__ == "__main__":
    # Ví dụ nhập: 3 9 20 None None 15 7
    # Cây:
    #       3
    #      / \
    #     9  20
    #       /  \
    #      15   7
    arr = input("Nhập các giá trị node theo level-order, cách nhau bởi dấu cách (dùng None cho chỗ trống): ").split()
    values = [int(x) if x != "None" else None for x in arr]

    root = build_tree(values)
    sol = Solution()
    depth = sol.maxDepth(root)
    print("Độ sâu tối đa của cây:", depth)
