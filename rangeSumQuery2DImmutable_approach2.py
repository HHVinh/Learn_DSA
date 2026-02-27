# ✅ CÁCH 2 — Prefix Sum 2D (row prefix + above)
# 👉 Ý tưởng: Mỗi ô lưu tổng hình chữ nhật từ (0,0) → ô đó. Dùng bảng lệch +1 hàng +1 cột để khỏi xử lý biên

from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])                     
        self.sumMat = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            row_prefix = 0                                           # tổng prefix theo hàng
            for c in range(cols):
                row_prefix += matrix[r][c]                           # cộng dồn hàng hiện tại
                above = self.sumMat[r][c + 1]                        # tổng phía trên
                self.sumMat[r + 1][c + 1] = row_prefix + above       # tổng từ (0,0) → (r,c)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1  # đổi sang index lệch
        bottomRight = self.sumMat[row2][col2]                            # tổng lớn
        above = self.sumMat[row1 - 1][col2]                              # cắt phần trên
        left = self.sumMat[row2][col1 - 1]                               # cắt phần trái
        topLeft = self.sumMat[row1 - 1][col1 - 1]                        # cộng lại góc chung
        return bottomRight - above - left + topLeft

# ===== TEST VS CODE =====
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(1, 1, 2, 2))  # 5 + 6 + 8 + 9 = 28
