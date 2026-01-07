from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Xoay ma trận 90 độ theo chiều kim đồng hồ (in-place)
        Không trả về gì, chỉ thay đổi trực tiếp matrix
        """

        n = len(matrix)

        # =========================
        # 1️⃣ Reverse theo chiều dọc (lật trên xuống dưới)
        # =========================
        # Ví dụ:
        #
        #  [1, 2, 3]  ->  [7, 8, 9]
        #  [4, 5, 6]  ->  [4, 5, 6]
        #  [7, 8, 9]  ->  [1, 2, 3]
    
        matrix.reverse()   # in-place, KHÔNG tạo list mới

        # =========================
        # 2️⃣ Transpose ma trận
        # =========================
        # Đổi matrix[i][j] ↔ matrix[j][i]
        # Chỉ duyệt nửa trên (j > i) để tránh swap 2 lần
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# =========================
# Code test để chạy VS Code
# =========================
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Matrix ban đầu:")
    for row in matrix:
        print(row)

    sol = Solution()
    sol.rotate(matrix)

    print("\nMatrix sau khi rotate 90° clockwise:")
    for row in matrix:
        print(row)
