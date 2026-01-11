from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)

        # ---- Lặp khi còn ít nhất 1 hàng và 1 cột ----
        while left < right and top < bottom:

            # ---- Đi sang phải (hàng trên cùng) ----
            for c in range(left, right):
                res.append(matrix[top][c])
            top += 1  # co biên trên xuống

            # ---- Đi xuống (cột phải cùng) ----
            for r in range(top, bottom):
                res.append(matrix[r][right - 1])
            right -= 1  # co biên phải sang trái

            # ---- Kiểm tra còn đi tiếp được không ----
            # RẤT QUAN TRỌNG: tránh trùng phần tử
            if not (left < right and top < bottom):
                break

            # ---- Đi sang trái (hàng dưới cùng) ----
            for c in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][c])
            bottom -= 1  # co biên dưới lên

            # ---- Đi lên (cột trái cùng) ----
            for r in range(bottom - 1, top - 1, -1):
                res.append(matrix[r][left])
            left += 1  # co biên trái sang phải

        return res

if __name__ == "__main__":
    solution = Solution()

    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix2 = [
        [1, 2, 3, 4]
    ]

    matrix3 = [
        [1],
        [2],
        [3],
        [4]
    ]

    print("Matrix 1:", solution.spiralOrder(matrix1))
    print("Matrix 2:", solution.spiralOrder(matrix2))
    print("Matrix 3:", solution.spiralOrder(matrix3))
