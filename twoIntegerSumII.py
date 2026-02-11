# 167. Two Sum II - Input Array Is Sorted
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curr_sum = numbers[l] + numbers[r]
            
            if curr_sum == target:
                # SỬA Ở ĐÂY: Trả về chỉ số (Indices)
                # Bài 167 yêu cầu 1-based index nên cộng thêm 1
                return [l + 1, r + 1] 
            
            elif curr_sum > target:
                r -= 1
            else:
                l += 1
        
        return [] # Nên trả về list rỗng thay vì -1 cho đúng type hint
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))  # Output: [1, 2]
    print(sol.twoSum([2,3,4], 6))      # Output: [1, 3]
    print(sol.twoSum([-1,0], -1))      # Output: [1, 2]