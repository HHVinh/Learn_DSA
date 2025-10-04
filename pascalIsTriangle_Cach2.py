from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Khởi tạo tam giác Pascal với các phần tử toàn là 1
        # Hàng i sẽ có (i+1) phần tử
        res = [[1] * (i + 1) for i in range(numRows)]

        # Bắt đầu từ hàng thứ 3 (chỉ số 2) vì hàng 0 và 1 đã đúng sẵn rồi
        for i in range(2, numRows):
            # Cập nhật các phần tử bên trong (không phải mép ngoài)
            for j in range(1, i):
                # Quy tắc Pascal: phần tử = tổng của 2 phần tử phía trên
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]

        return res

"""
        res = [[1] * (i + 1) for i in range(numRows)]
Câu lệnh này là list comprehension. Nó tương đương với:
        res = []
        for i in range(numRows):   # i = 0,1,2,3,4
            res.append([1] * (i + 1))

Khi i = 0 → [1] * (0+1) = [1]
Khi i = 1 → [1] * (1+1) = [1, 1]
Khi i = 2 → [1] * (2+1) = [1, 1, 1]
Khi i = 3 → [1] * (3+1) = [1, 1, 1, 1]
Khi i = 4 → [1] * (4+1) = [1, 1, 1, 1, 1]
"""

if __name__ == "__main__":
    # Nhập số hàng từ bàn phím
    numRows = int(input("Nhập số hàng của tam giác Pascal: "))

    # Tạo đối tượng Solution và gọi hàm generate
    solution = Solution()
    triangle = solution.generate(numRows)

    # In kết quả
    print("Tam giác Pascal với", numRows, "hàng là:")
    for row in triangle:
        print(row)
