from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            # Tính diện tích hiện tại
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)

            # Di chuyển con trỏ: bỏ đi cột thấp hơn
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

heights = list(map(int, input("Nhập chiều cao các cột (cách nhau bởi dấu cách): ").split()))
sol = Solution()
ket_qua = sol.maxArea(heights)
print("Diện tích chứa nước lớn nhất là:", ket_qua)
