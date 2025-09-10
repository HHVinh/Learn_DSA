# Định nghĩa lớp Node cho đồ thị
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val                               # Giá trị của node
        self.neighbors = neighbors if neighbors else []  # Danh sách các node kề

from typing import Optional
from collections import deque   # dùng deque để duyệt BFS

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:   # Nếu đồ thị rỗng thì trả về None
            return None

        # Bảng ánh xạ từ node cũ -> node mới (dùng để tránh tạo trùng node)
        oldToNew = {}
        # Tạo node mới từ node đầu tiên
        oldToNew[node] = Node(node.val)

        # Dùng BFS để duyệt qua các node
        q = deque([node])

        while q:
            cur = q.popleft()   # Lấy 1 node ra khỏi queue
            for nei in cur.neighbors:   # Duyệt qua tất cả neighbor của node hiện tại
                if nei not in oldToNew:   # Nếu neighbor này chưa được clone
                    oldToNew[nei] = Node(nei.val)  # Tạo node mới
                    q.append(nei)  # Thêm neighbor gốc vào queue để xử lý tiếp
                # Thêm neighbor đã clone vào danh sách kề của node mới
                oldToNew[cur].neighbors.append(oldToNew[nei])

        # Trả về node đã clone tương ứng với node đầu tiên
        return oldToNew[node]


# ================== TEST CODE ==================
if __name__ == "__main__":
    # Tạo một đồ thị mẫu: 1 -- 2
    #                      |    |
    #                      4 -- 3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    # Clone đồ thị
    sol = Solution()
    cloned = sol.cloneGraph(n1)

    # In ra kết quả kiểm tra
    print("Node gốc:", n1.val, "có neighbors:", [nei.val for nei in n1.neighbors])
    print("Node clone:", cloned.val, "có neighbors:", [nei.val for nei in cloned.neighbors])
