from typing import List          # Import để VS Code không báo lỗi kiểu dữ liệu


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:               # Nếu chỉ có 1 bậc
            return 1             # Chỉ có 1 cách leo

        def matrix_mult(A, B):   # Hàm nhân 2 ma trận 2x2
            return [
                [
                    A[0][0] * B[0][0] + A[0][1] * B[1][0],  # Phần tử [0][0]
                    A[0][0] * B[0][1] + A[0][1] * B[1][1]   # Phần tử [0][1]
                ],
                [
                    A[1][0] * B[0][0] + A[1][1] * B[1][0],  # Phần tử [1][0]
                    A[1][0] * B[0][1] + A[1][1] * B[1][1]   # Phần tử [1][1]
                ]
            ]

        def matrix_pow(M, p):    # Hàm lũy thừa ma trận bằng chia để trị
            result = [[1, 0],    # Ma trận đơn vị (identity matrix)
                      [0, 1]]
            base = M             # Ma trận cơ sở ban đầu

            while p:             # Khi số mũ còn > 0
                if p % 2 == 1:   # Nếu p là số lẻ
                    result = matrix_mult(result, base)  # Nhân vào kết quả
                base = matrix_mult(base, base)           # Bình phương ma trận
                p //= 2          # Chia p cho 2

            return result        # Trả về ma trận M^p

        M = [[1, 1],             # Ma trận Fibonacci
             [1, 0]]

        result = matrix_pow(M, n)  # Tính M^n
        return result[0][0]        # F(n+1) chính là số cách leo


# -----------------------------
# PHẦN CHẠY THỬ TRONG VS CODE
# -----------------------------
if __name__ == "__main__":

    n = 5                        # Số bậc cầu thang

    solution = Solution()
    answer = solution.climbStairs(n)

    print("Số bậc:", n)
    print("Số cách leo:", answer)
