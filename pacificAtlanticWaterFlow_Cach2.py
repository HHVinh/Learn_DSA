from typing import List   # ✅ Import để Python nhận biết List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])  # ✅ Lưu số hàng và số cột của lưới độ cao
        pac, atl = set(), set()  # ✅ Hai tập hợp lưu các ô có thể chảy tới Thái Bình Dương (pac) và Đại Tây Dương (atl)

        # ✅ Hàm đệ quy DFS để tìm các ô có thể chảy tới đại dương
        def dfs(r, c, visit, prevHeight):
            # Nếu ô (r, c) đã được thăm, hoặc ra khỏi giới hạn bản đồ,
            # hoặc chiều cao hiện tại thấp hơn chiều cao trước → không thể chảy ngược nước lên cao hơn
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                heights[r][c] < prevHeight
            ):
                return
            
            visit.add((r, c))  # ✅ Đánh dấu ô (r, c) đã được thăm
            # ✅ Gọi đệ quy theo 4 hướng: xuống, lên, phải, trái
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        # ✅ Duyệt hàng đầu tiên (Pacific) và hàng cuối cùng (Atlantic)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])               # Nước từ biển Thái Bình Dương (hàng đầu)
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Nước từ biển Đại Tây Dương (hàng cuối)

        # ✅ Duyệt cột đầu tiên (Pacific) và cột cuối cùng (Atlantic)
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])               # Biên trái → Thái Bình Dương
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Biên phải → Đại Tây Dương

        res = []  # ✅ Kết quả chứa các ô có thể chảy đến cả 2 đại dương
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:     # ✅ Nếu ô này có trong cả 2 tập hợp
                    res.append([r, c])
        return res  # ✅ Trả về danh sách tọa độ các ô hợp lệ

# ===============================
# ✅ Ví dụ chạy thử:
heights = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]
]

s = Solution()
print(s.pacificAtlantic(heights))  # 👉 Kết quả mong đợi: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
