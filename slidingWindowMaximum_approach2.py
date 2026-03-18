# 239. Sliding Window Maximum
from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = deque() # Lưu GIÁ TRỊ (Value), không lưu Index
        n = len(nums)
        res = []

        for i in nums[:k]: # 1. Khởi tạo cửa sổ đầu tiên
            # Duy trì tính giảm dần: Loại bỏ các số bé hơn số mới vào (vì chúng vô dụng)
            while d and d[-1] < i:
                d.pop()
            d.append(i)

        res.append(d[0]) # d[0] luôn là Max hiện tại

        for p in range(k, n): # 2. Bắt đầu trượt cửa sổ (p là phần tử MỚI vào)
            
            # Logic trượt ra: Kiểm tra phần tử vừa bị loại khỏi cửa sổ (nums[p-k])
            # Nếu nó chính là Max (d[0]) thì phải xóa khỏi đầu hàng đợi
            if nums[p-k] == d[0]:
                d.popleft()

            # Logic trượt vào: Tiếp tục loại bỏ kẻ yếu để duy trì hàng đợi giảm dần
            while d and d[-1] < nums[p]:
                d.pop()
            d.append(nums[p])
            
            res.append(d[0]) # Ghi nhận Max của cửa sổ mới

        return res

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Output: [3,3,5,5,6,7]
    print(solution.maxSlidingWindow([1], 1))  # Output: [1]
    print(solution.maxSlidingWindow([9,11], 2))  # Output: [11]
    print(solution.maxSlidingWindow([4,-2], 2))  # Output: [4]