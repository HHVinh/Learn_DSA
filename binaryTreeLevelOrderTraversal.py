from collections import deque
from typing import Optional, List

# Định nghĩa node của cây nhị phân
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Hàm duyệt level-order (BFS) để in từng tầng của cây
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)

        while q:
            lenQ = len(q)   # số node trong 1 tầng
            level = []      # lưu các node trong tầng hiện tại

            for i in range(lenQ):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)   # thêm con trái vào queue
                    q.append(node.right)  # thêm con phải vào queue
            if level:       # chỉ lưu tầng có giá trị
                res.append(level)
        return res


# Hàm xây dựng cây nhị phân từ list đầu vào (level-order)
def build_tree(values: List[Optional[str]]) -> Optional[TreeNode]:
    if not values or values[0] == "null":
        return None
    
    root = TreeNode(int(values[0]))
    q = deque([root])
    i = 1

    while q and i < len(values):
        node = q.popleft()
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            q.append(node.right)
        i += 1
    return root


if __name__ == "__main__":
    # Nhập cây từ bàn phím, ví dụ: 3 9 20 null null 15 7
    arr = input("Nhập cây dạng level-order (dùng 'null' cho node rỗng): ").split()
    root = build_tree(arr)

    sol = Solution()
    print("Kết quả Level Order Traversal:")
    print(sol.levelOrder(root))
