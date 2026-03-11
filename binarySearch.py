# 704. Binary Search
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Cách tính mid an toàn, tránh tràn số (Overflow) trong các ngôn ngữ khác
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # Target nằm ở nửa phải, dời left lên
                left = mid + 1
            else:
                # Target nằm ở nửa trái, dời right xuống
                right = mid - 1
                
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1,0,3,5,9,12], 9))  # Output: 4
    print(solution.search([-1,0,3,5,9,12], 2))  # Output: -1