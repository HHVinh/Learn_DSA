from typing import List  # để dùng List[int]

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1  # giá trị mặc định thay thế cho phần tử cuối cùng

        # duyệt ngược từ cuối mảng về đầu
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]                 # lưu giá trị gốc của arr[i]
            arr[i] = rightMax             # thay arr[i] bằng phần tử lớn nhất bên phải
            rightMax = max(rightMax, temp)  # cập nhật rightMax

        return arr

# --- TEST ---
arr = [17, 18, 5, 4, 6, 1]
solution = Solution()
print(solution.replaceElements(arr))  # Kết quả: [18, 6, 6, 6, 1, -1]
