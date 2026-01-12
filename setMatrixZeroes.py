from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])

        # ===== Kiểm tra xem hàng đầu và cột đầu có chứa số 0 không =====
        first_row_zero = any(matrix[0][c] == 0 for c in range(n))
        first_col_zero = any(matrix[r][0] == 0 for r in range(m))
        # 👉 any() làm đúng 3 việc: duyệt từng phần tử, gặp True → dừng ngay, không có True → trả False

        # ===== Dùng hàng đầu & cột đầu làm marker =====
        # Duyệt từ (1,1) để KHÔNG phá marker sớm
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0   # đánh dấu hàng r
                    matrix[0][c] = 0   # đánh dấu cột c

        # ===== Set 0 cho phần bên trong dựa trên marker =====
        for r in range(1, m):
            for c in range(1, n):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # ===== Nếu hàng đầu ban đầu có 0 thì set cả hàng đầu =====
        if first_row_zero:
            for c in range(n):
                matrix[0][c] = 0

        # ===== Nếu cột đầu ban đầu có 0 thì set cả cột đầu =====
        if first_col_zero:
            for r in range(m):
                matrix[r][0] = 0

if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]

    matrix3 = [
        [1, 0]
    ]

    solution.setZeroes(matrix1)
    solution.setZeroes(matrix2)
    solution.setZeroes(matrix3)

    print("Matrix 1:")
    for row in matrix1:
        print(row)

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nMatrix 3:")
    for row in matrix3:
        print(row)
