from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]
    
s = Solution()

nums = list(map(int, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))
target = int(input("Nhập giá trị mục tiêu: "))

print(s.twoSum(nums,target))

