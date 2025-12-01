from collections import deque
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """ Hàm kiểm tra xem đồ thị có phải là cây hay không.
        Một đồ thị là cây khi: Không có chu kỳ và Tất cả các node đều được nối với nhau (connected) """

        if len(edges) > n - 1: # Nếu số cạnh > n - 1 thì chắc chắn không thể là cây (vì sẽ tạo chu kỳ)
            return False

        adj = [[] for _ in range(n)] # Tạo danh sách kề (adjacency list) rỗng cho n đỉnh
        for u, v in edges:# Gắn các cạnh vào danh sách kề
            adj[u].append(v)
            adj[v].append(u)

        visit = set() # visit = set() để lưu những node đã duyệt

        # Bắt đầu BFS từ node 0 (giả sử node 0 tồn tại)
        q = deque([(0, -1)])  # (node hiện tại, node cha)
        visit.add(0)

        while q: # BFS duyệt toàn bộ đồ thị
            node, parent = q.popleft()
            for nei in adj[node]:
                if nei == parent: # Nếu hàng xóm trùng với cha → bỏ qua (tránh đi lùi)
                    continue

                if nei in visit: # Nếu đã visit rồi → có chu kỳ → KHÔNG phải cây
                    return False

                visit.add(nei) # Thêm vào visited
                q.append((nei, node))

        return len(visit) == n # Cuối cùng, tất cả node phải được duyệt


# ---------------------------------------------------------
# Phần test trong VS Code
# ---------------------------------------------------------

if __name__ == "__main__":
    sol = Solution()

    # Ví dụ 1: là cây
    n = 5
    edges = [[0,1], [0,2], [0,3], [1,4]]
    print("Test 1:", sol.validTree(n, edges))  # True

    # Ví dụ 2: có chu kỳ
    n2 = 5
    edges2 = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    print("Test 2:", sol.validTree(n2, edges2))  # False

    # Ví dụ 3: thiếu cạnh → không connected
    n3 = 4
    edges3 = [[0,1], [2,3]]
    print("Test 3:", sol.validTree(n3, edges3))  # False
