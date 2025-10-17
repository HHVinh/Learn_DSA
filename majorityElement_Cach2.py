from typing import List  # để dùng List[int]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0
        for num in nums:
            if count == 0:
                res = num
            
            if num == res:
                count += 1
            else:
                count -= 1
        return res

# --- TEST ---
nums = [3, 3, 4, 2, 3, 3, 5]
solution = Solution()
print(solution.majorityElement(nums))  # Kết quả: 3
