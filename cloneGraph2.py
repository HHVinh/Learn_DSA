from typing import Optional, List, Dict   # import để dùng kiểu dữ liệu (không bắt buộc nhưng nên có)


# Định nghĩa Node của đồ thị
class Node:
    def __init__(self, val: int = 0, neighbors: List['Node'] = None):
        self.val = val                                  # giá trị của node
        self.neighbors = neighbors if neighbors else [] # danh sách các node kề


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        oldToNew: Dict[Node, Node] = {}   # map: node cũ -> node mới (tránh clone lặp)

        def dfs(node: Node) -> Node:
            # Nếu node này đã được clone rồi thì trả về bản clone
            if node in oldToNew:           # kiểm tra node đã xử lý chưa
                return oldToNew[node]      # trả về node đã clone

            copy = Node(node.val)          # tạo node mới với cùng giá trị
            oldToNew[node] = copy          # lưu mapping node cũ -> node mới

            for nei in node.neighbors:     # duyệt các node hàng xóm
                copy.neighbors.append(
                    dfs(nei)               # clone node hàng xóm và thêm vào danh sách kề
                )

            return copy                    # trả về node đã clone

        if not node:                       # nếu đồ thị rỗng
            return None

        return dfs(node)                   # bắt đầu clone từ node gốc


if __name__ == "__main__":
    # Tạo đồ thị mẫu: 1 -- 2
    #                   |    |
    #                   4 -- 3

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    sol = Solution()
    clone = sol.cloneGraph(n1)

    print(clone.val)                        # 1
    print([n.val for n in clone.neighbors]) # [2, 4]
