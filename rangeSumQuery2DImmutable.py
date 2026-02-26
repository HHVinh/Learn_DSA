# ⭐ Bài 304 CÁCH 1 — Prefix Sum 2D CHUẨN (BEST PRACTICE)
# 👉 Ý tưởng: dp[r+1][c+1] = tổng từ (0,0) → matrix[r][c]. Dòng 0 & cột 0 toàn số 0 → không cần if

from typing import List
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # Tạo bảng dp kích thước (rows + 1) x (cols + 1) toàn số 0
        # self.dp[r+1][c+1] sẽ lưu tổng từ góc (0,0) đến matrix[r][c]
        self.dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            for c in range(cols):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c]                                       # ô hiện tại
                    + self.dp[r][c + 1]                                # cộng phần trên
                    + self.dp[r + 1][c]                                # cộng phần trái
                    - self.dp[r][c]                                    # trừ phần bị cộng 2 lần
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Lưu ý: Do bảng dp bị lệch index +1, nên:
        # row2 trong matrix ứng với row2 + 1 trong dp
        # row1 (biên trên) cần trừ đi dòng row1 trong dp
        return (
            self.dp[row2 + 1][col2 + 1]                                # tổng lớn
            - self.dp[row1][col2 + 1]                                  # bỏ phần trên
            - self.dp[row2 + 1][col1]                                  # bỏ phần trái
            + self.dp[row1][col1]                                      # cộng lại góc giao
        )

# ===== TEST VS CODE =====
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    obj = NumMatrix(matrix)
    print(obj.sumRegion(1, 1, 2, 2))  # 28
