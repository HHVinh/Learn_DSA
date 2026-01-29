# 912 Shell Sort - Sắp xếp mảng bằng thuật toán Shell Sort
# Tư tưởng: sắp xếp từ xa đến gần (gap lớn → gap nhỏ)
from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if n <= 1: # Nếu mảng có 0 hoặc 1 phần tử thì không cần sắp xếp
            return nums

        gap = n // 2 # Bước nhảy ban đầu

        while gap >= 1: # Lặp cho đến khi gap = 0

            for i in range(gap, n): # Duyệt từng phần tử từ vị trí gap trở đi

                tmp = nums[i] # Lưu lại giá trị hiện tại để chèn

                j = i - gap # So sánh với phần tử đứng trước nó gap bước

                while j >= 0 and nums[j] > tmp: # Dịch các phần tử lớn hơn tmp sang phải gap bước
                    nums[j + gap] = nums[j]
                    j -= gap

                nums[j + gap] = tmp # Chèn tmp vào đúng vị trí

            gap //= 2 # Giảm gap để sắp xếp chi tiết hơn

        return nums


# =========================
# HÀM MAIN ĐỂ CHẠY VS CODE
# =========================
def main():
    nums = [8, 5, 3, 7, 6, 2]

    print("Mảng ban đầu:")
    print(nums)

    solution = Solution()
    sorted_nums = solution.sortArray(nums)

    print("Mảng sau khi sắp xếp:")
    print(sorted_nums)


# Chạy chương trình
if __name__ == "__main__":
    main()
