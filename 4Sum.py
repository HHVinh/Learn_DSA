# 18. 4Sum
from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort() # Bắt buộc sort
        n = len(nums)
        res = []
        
        # Vòng lặp cho số thứ 1
        for i in range(n - 3):
            # 1. Tránh trùng lặp số thứ 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # PRUNING 1 (Cắt tỉa):
            # Nếu 4 số nhỏ nhất bắt đầu từ i đã lớn hơn target -> Dừng luôn vì các số sau càng lớn hơn
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            # Nếu số i cộng 3 số lớn nhất mà vẫn nhỏ hơn target -> i này quá nhỏ, bỏ qua
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
                
            # Vòng lặp cho số thứ 2
            for j in range(i + 1, n - 2):
                # 2. Tránh trùng lặp số thứ 2
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # PRUNING 2 (Cắt tỉa tương tự cho vòng lặp j):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                
                # Two Pointers cho 2 số còn lại
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Bỏ qua các số trùng lặp ở left và right
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
                        
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return res
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solution.fourSum(nums, target))  # Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]