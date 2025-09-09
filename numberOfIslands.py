from typing import List
from collections import deque  # để dùng queue

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # 4 hướng di chuyển: xuống, lên, phải, trái
        ROWS, COLS = len(grid), len(grid[0])  # số hàng và số cột của lưới
        islands = 0  # biến đếm số đảo

        def bfs(r, c):  # duyệt BFS bắt đầu từ ô (r,c)
            q = deque()  # tạo queue rỗng
            grid[r][c] = "0"  # đánh dấu ô này đã thăm (biến đất thành nước)
            q.append((r, c))  # đưa ô ban đầu vào queue

            while q:  # lặp khi queue còn phần tử
                row, col = q.popleft()  # lấy phần tử đầu ra khỏi queue
                for dr, dc in directions:  # duyệt 4 hướng
                    nr, nc = dr + row, dc + col  # tọa độ mới
                    if (nr < 0 or nc < 0 or nr >= ROWS or  # kiểm tra ngoài biên
                        nc >= COLS or grid[nr][nc] == "0"):  # hoặc là nước rồi
                        continue  # bỏ qua
                    q.append((nr, nc))  # thêm ô đất mới vào queue
                    grid[nr][nc] = "0"  # đánh dấu đã thăm (chìm đất)

        for r in range(ROWS):  # duyệt toàn bộ lưới
            for c in range(COLS):
                if grid[r][c] == "1":  # gặp một ô đất chưa thăm
                    bfs(r, c)  # gọi BFS để làm chìm cả đảo
                    islands += 1  # đếm thêm 1 đảo

        return islands  # trả kết quả cuối cùng


# Ví dụ chạy thử
if __name__ == "__main__":
    grid = [
        ["1","1","0","0"],
        ["1","0","0","1"],
        ["0","0","1","1"],
        ["0","0","0","0"]
    ]
    sol = Solution()
    print(sol.numIslands(grid))  # Kết quả mong đợi: 2
