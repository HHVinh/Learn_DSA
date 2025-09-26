from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Khởi tạo tam giác Pascal rỗng
        triangle = []
        
        # Lặp qua từng dòng từ 0 đến numRows - 1
        for row_num in range(numRows):
            # Mỗi dòng ban đầu có (row_num + 1) phần tử đều là 1
            row = [1] * (row_num + 1)
            
            # Điền các phần tử bên trong (không tính phần tử đầu và cuối)
            for j in range(1, row_num):
                # Công thức: phần tử hiện tại = phần tử phía trên-bên trái + phía trên-bên phải
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            
            # Thêm dòng vừa tạo vào tam giác
            triangle.append(row)
        
        return triangle

# --- Đoạn code để chạy thử ---
if __name__ == "__main__":
    soDong = 5  # Bạn có thể thay đổi số dòng của tam giác Pascal
    solution = Solution()
    ketQua = solution.generate(soDong)
    print("Tam giác Pascal với", soDong, "dòng là:")
    for dong in ketQua:
        print(dong)
