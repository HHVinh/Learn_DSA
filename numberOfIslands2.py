from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 4 hướng di chuyển: xuống, lên, phải, trái
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])  # số hàng và số cột
        islands = 0  # đếm số đảo

        # Hàm DFS để "đánh dấu" toàn bộ vùng đất nối liền
        def dfs(r, c):
            # Nếu ra ngoài biên hoặc gặp nước thì dừng
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return

            # Đánh dấu ô hiện tại đã thăm (chuyển đất "1" thành nước "0")
            grid[r][c] = "0"

            # Gọi DFS cho 4 ô kề bên (trên, dưới, trái, phải)
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Duyệt toàn bộ lưới
        for r in range(ROWS):
            for c in range(COLS):
                # Nếu gặp đất "1" thì tìm thấy một đảo mới
                if grid[r][c] == "1":
                    dfs(r, c)      # "chìm" toàn bộ đảo này
                    islands += 1   # tăng số lượng đảo

        return islands


# ------------------------------
# Ví dụ chạy thử
if __name__ == "__main__":
    solution = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("Số đảo là:", solution.numIslands(grid))  # Kết quả mong đợi: 3
