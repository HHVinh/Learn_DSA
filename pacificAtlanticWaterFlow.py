from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0]) # Số hàng và số cột
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # Các hướng di chuyển: xuống, lên, phải, trái
        # Hai ma trận đánh dấu: True nếu ô đó có thể đi đến Thái Bình Dương hoặc Đại Tây Dương
        pac = [[False] * COLS for _ in range(ROWS)]  # Pacific
        atl = [[False] * COLS for _ in range(ROWS)]  # Atlantic

        def bfs(source, ocean): # Hàm BFS xuất phát từ bờ biển, tìm các ô có thể chảy nước đến
            q = deque(source)  # tạo queue từ các ô bờ
            while q:
                r, c = q.popleft()
                ocean[r][c] = True  # đánh dấu ô này có thể đi đến biển
                for dr, dc in directions: # duyệt 4 hướng
                    nr, nc = r + dr, c + dc
                    # kiểm tra trong biên và chưa được thăm
                    # đồng thời chiều cao phải >= ô hiện tại (nước chảy ngược về phía cao hơn hoặc bằng)
                    if (0 <= nr < ROWS and 0 <= nc < COLS and not ocean[nr][nc] and
                        heights[nr][nc] >= heights[r][c]):

                        q.append((nr, nc))

        pacific = [] # Tập hợp các ô sát biển Pacific (hàng 0 và cột 0)
        atlantic = [] # Tập hợp các ô sát biển Atlantic (hàng cuối và cột cuối)
        for c in range(COLS):
            pacific.append((0, c))           # hàng đầu
            atlantic.append((ROWS - 1, c))   # hàng cuối

        for r in range(ROWS):
            pacific.append((r, 0))           # cột đầu
            atlantic.append((r, COLS - 1))   # cột cuối

        bfs(pacific, pac) # BFS từ biên Pacific
        bfs(atlantic, atl) # BFS từ biên Atlantic

        res = [] # Lấy kết quả: những ô đến được cả 2 đại dương
        for r in range(ROWS):
            for c in range(COLS):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])
        return res


# ================== TEST ==================
if __name__ == "__main__":
    solution = Solution()
    heights = [
        [1, 2, 2, 3, 5],
        [3, 2, 3, 4, 4],
        [2, 4, 5, 3, 1],
        [6, 7, 1, 4, 5],
        [5, 1, 1, 2, 4]
    ]
    print("Các ô có thể chảy tới cả 2 đại dương là:")
    print(solution.pacificAtlantic(heights))
