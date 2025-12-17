from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Tạo danh sách kề (adjacency list)
        # adj[i] sẽ chứa các đỉnh kề với đỉnh i
        adj = [[] for _ in range(n)]

        # Mảng đánh dấu đã thăm hay chưa
        visit = [False] * n

        # Duyệt qua danh sách cạnh để xây dựng đồ thị vô hướng
        for u, v in edges:
            adj[u].append(v)   # u kề với v
            adj[v].append(u)   # v kề với u

        # Hàm DFS để thăm toàn bộ các đỉnh trong cùng 1 thành phần liên thông
        def dfs(node):
            # Duyệt qua các hàng xóm của node
            for nei in adj[node]:
                if not visit[nei]:        # nếu hàng xóm chưa được thăm
                    visit[nei] = True    # đánh dấu đã thăm
                    dfs(nei)             # tiếp tục DFS từ hàng xóm đó

        res = 0  # biến đếm số thành phần liên thông

        # Duyệt qua tất cả các đỉnh trong đồ thị
        for node in range(n):
            if not visit[node]:           # nếu đỉnh này chưa được thăm
                visit[node] = True        # bắt đầu thăm một thành phần mới
                dfs(node)                 # DFS để thăm hết thành phần đó
                res += 1                  # tăng số thành phần liên thông

        return res


# =========================
# PHẦN CHẠY THỬ TRONG VS CODE
# =========================
if __name__ == "__main__":
    sol = Solution()

    # Ví dụ test
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]

    result = sol.countComponents(n, edges)
    print("Số thành phần liên thông là:", result)
