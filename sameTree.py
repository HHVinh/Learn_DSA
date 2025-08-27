from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])  # hàng đợi duyệt cây p
        q2 = deque([q])  # hàng đợi duyệt cây q

        while q1 and q2:  # duyệt song song cả 2 cây
            for _ in range(len(q1)):  # duyệt hết số node hiện tại trong queue
                nodeP = q1.popleft()  # lấy node bên cây p
                nodeQ = q2.popleft()  # lấy node bên cây q

                if nodeP is None and nodeQ is None:  # nếu cả hai cùng None thì bỏ qua
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:  # khác nhau ở đây -> false
                    return False

                q1.append(nodeP.left)   # thêm con trái của nodeP vào queue
                q1.append(nodeP.right)  # thêm con phải của nodeP vào queue
                q2.append(nodeQ.left)   # thêm con trái của nodeQ vào queue
                q2.append(nodeQ.right)  # thêm con phải của nodeQ vào queue

        return True  # nếu duyệt hết mà không khác -> giống nhau

# =========================
# HÀM HỖ TRỢ: Tạo cây từ list level-order
# =========================
def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:  # tạo node trái nếu có
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:  # tạo node phải nếu có
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

# =========================
# CHẠY THỬ TRONG VS CODE
# =========================
if __name__ == "__main__":
    # Ví dụ nhập: 1 2 3  (tương ứng cây: 1 với con trái 2, con phải 3)
    arr1 = input("Nhập cây 1 (level-order, cách nhau bởi dấu cách, dùng None cho chỗ trống): ").split()
    arr2 = input("Nhập cây 2 (level-order, cách nhau bởi dấu cách, dùng None cho chỗ trống): ").split()

    values1 = [int(x) if x != "None" else None for x in arr1]
    values2 = [int(x) if x != "None" else None for x in arr2]

    root1 = build_tree(values1)
    root2 = build_tree(values2)

    sol = Solution()
    result = sol.isSameTree(root1, root2)
    print("Hai cây có giống nhau không?", result)
