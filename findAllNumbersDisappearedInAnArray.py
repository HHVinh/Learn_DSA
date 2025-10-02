from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Bước 1: Duyệt qua từng phần tử để đánh dấu
        for x in nums:
            idx = abs(x) - 1   # vì giá trị nằm trong [1..n], nên trừ 1 để ra index
            if nums[idx] > 0:  # chỉ đánh dấu khi chưa bị đánh dấu trước đó
                nums[idx] *= -1   # đánh dấu bằng cách đổi dấu sang âm

        # Bước 2: Thu thập kết quả
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:    # nếu còn dương nghĩa là chưa được đánh dấu
                res.append(i + 1)  # i+1 chính là số bị thiếu

        return res
    
"""
Ví dụ minh họa: nums = [4,3,2,7,8,2,3,1]

Gặp 4 → đánh dấu vị trí 3 (nums[3]) thành âm → nums = [4,3,2,-7,8,2,3,1]
Gặp 3 → đánh dấu nums[2] → nums = [4,3,-2,-7,8,2,3,1]
Gặp 2 → đánh dấu nums[1] → nums = [4,-3,-2,-7,8,2,3,1]
Gặp 7 → đánh dấu nums[6] → nums = [4,-3,-2,-7,8,2,-3,1]
Gặp 8 → đánh dấu nums[7] → nums = [4,-3,-2,-7,8,2,-3,-1] ... tiếp tục.
Sau khi duyệt, mảng có giá trị dương ở vị trí 4 và 5 → thiếu số 5,6.
"""


# ------------------ Ví dụ chạy thử ------------------
if __name__ == "__main__":
    sol = Solution()

    # Ví dụ 1
    nums1 = [4,3,2,7,8,2,3,1]
    print("Mảng:", nums1)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums1))  
    # Kết quả mong đợi: [5,6]

    # Ví dụ 2
    nums2 = [1,1]
    print("\nMảng:", nums2)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums2))  
    # Kết quả mong đợi: [2]

    # Ví dụ 3
    nums3 = [2,2,2,2]
    print("\nMảng:", nums3)
    print("Các số bị thiếu:", sol.findDisappearedNumbers(nums3))  
    # Kết quả mong đợi: [1,3,4]
