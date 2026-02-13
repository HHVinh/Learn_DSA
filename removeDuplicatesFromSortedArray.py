# 26: Remove Duplicates from Sorted Array

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Nếu mảng rỗng thì không có phần tử hợp lệ
        if not nums:
            return 0

        i = 0  # trỏ vào vị trí cuối của dãy KHÔNG trùng

        # Duyệt từ phần tử thứ 2 trở đi
        for num in nums[1:]:
            if nums[i] != num:     # nếu gặp giá trị mới
                i += 1             # tăng vị trí hợp lệ
                nums[i] = num      # ghi giá trị mới vào mảng

        return i + 1               # số phần tử không trùng

if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = solution.removeDuplicates(nums)
    print(f"Số phần tử không trùng: {k}")
    print(f"Mảng sau khi loại bỏ trùng: {nums[:k]}")
