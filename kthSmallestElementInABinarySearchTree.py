from typing import Optional

# Định nghĩa node của cây nhị phân tìm kiếm (BST)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # giá trị node
        self.left = left      # con trái
        self.right = right    # con phải

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []           # stack để lưu các node tổ tiên (ancestor)
        curr = root          # bắt đầu từ gốc

        # duyệt in-order (trái -> node -> phải)
        while stack or curr:
            # đi hết nhánh trái, đồng thời push các node dọc đường
            while curr:
                stack.append(curr)
                curr = curr.left

            # pop node ra để thăm
            curr = stack.pop()
            k -= 1  # đã thăm được 1 node
            if k == 0:
                return curr.val  # nếu đủ k thì trả về luôn

            # sau khi thăm, đi sang phải
            curr = curr.right

        return -1  # nếu k lớn hơn số node trong cây

# -------------------------------
# Tạo cây BST mẫu
#        5
#       / \
#      3   7
#     / \    \
#    2   4    8

root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(7, None, TreeNode(8))

# Nhập k từ bàn phím
k = int(input("Nhập k (vị trí nhỏ nhất cần tìm): "))

sol = Solution()
result = sol.kthSmallest(root, k)
print(f"Phần tử nhỏ thứ {k} trong BST là: {result}")
