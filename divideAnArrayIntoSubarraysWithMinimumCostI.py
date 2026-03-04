# 3010. Divide an Array Into Subarrays With Minimum Cost I

from typing import List
class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Khởi tạo 2 biến min với giá trị vô cực
        min1 = float('inf') # Số nhỏ nhất
        min2 = float('inf') # Số nhỏ thứ hai

        # Duyệt từ phần tử thứ 2 trở đi (bỏ qua nums[0] vì nó luôn được chọn)
        for x in nums[1:]:
            if x < min1:
                # Nếu x nhỏ hơn cả min1
                # -> Đẩy min1 xuống làm min2, x chiếm ngôi min1
                min2 = min1
                min1 = x
            elif x < min2:
                # Nếu x chỉ nhỏ hơn min2 (nhưng lớn hơn min1)
                # -> x chiếm ngôi min2
                min2 = x
        
        return nums[0] + min1 + min2
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumCost([1,3,5,2,4,6]))  # Output: 6
    print(sol.minimumCost([5,1,2]))        # Output: 8
    print(sol.minimumCost([10,10,10]))     # Output: 30