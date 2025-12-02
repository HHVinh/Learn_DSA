from collections import deque
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """ Hàm đếm số thành phần liên thông (connected components) trong đồ thị.
        Một thành phần liên thông là tập các node có thể đi đến nhau qua các cạnh """

        adj = [[] for _ in range(n)] # Tạo danh sách kề (adjacency list) cho n node
        visit = [False] * n  # visit[i] = True nghĩa là đã thăm node i

        for u, v in edges: # Gắn cạnh vào danh sách kề
            adj[u].append(v)
            adj[v].append(u)

        def bfs(node): # Hàm BFS để duyệt tất cả node trong một thành phần liên thông
            q = deque([node])
            visit[node] = True  # Đánh dấu node đầu tiên đã thăm

            while q:
                cur = q.popleft()  # lấy node ra khỏi queue
                for nei in adj[cur]:  # duyệt tất cả hàng xóm
                    if not visit[nei]:  # nếu chưa thăm
                        visit[nei] = True
                        q.append(nei)

        res = 0  # đếm số thành phần liên thông

        for node in range(n): # Duyệt tất cả node
            if not visit[node]: # Nếu node chưa được thăm → đây là một thành phần liên thông mới
                bfs(node)
                res += 1

        return res


# ---------------------------------------------------
# Test trong VS Code
# ---------------------------------------------------
if __name__ == "__main__":
    sol = Solution()

    # Ví dụ 1: đồ thị có 2 thành phần: {0,1,2} và {3,4}
    n1 = 5
    edges1 = [[0,1], [1,2], [3,4]]
    print("Test 1:", sol.countComponents(n1, edges1))  # Kết quả: 2

    # Ví dụ 2: đồ thị connected hết → chỉ 1 thành phần
    n2 = 5
    edges2 = [[0,1], [1,2], [2,3], [3,4]]
    print("Test 2:", sol.countComponents(n2, edges2))  # Kết quả: 1

    # Ví dụ 3: không có cạnh → mỗi node là 1 thành phần
    n3 = 4
    edges3 = []
    print("Test 3:", sol.countComponents(n3, edges3))  # Kết quả: 4
