# 11. Container With Most Water
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1

        while l < r:
            minL = height[l]
            minR = height[r]
            
            # Cột bên trái thấp hơn -> Nó là điểm nghẽn. Tính diện tích theo minL
            if minL < minR:
                temp = minL * (r - l)
                
                # TỐI ƯU: Ép con trỏ l chạy liên tục bỏ qua các cột thấp hơn minL
                while l < r and height[l] <= minL:
                    l += 1
                    
            # Cột bên phải thấp hơn hoặc bằng -> Tính diện tích theo minR
            else:
                temp = minR * (r - l)
                
                # TỐI ƯU: Ép con trỏ r chạy liên tục bỏ qua các cột thấp hơn minR
                while l < r and height[r] <= minR:
                    r -= 1
            
            # Cập nhật diện tích lớn nhất
            if res < temp:
                res = temp

        return res


heights = list(map(int, input("Nhập chiều cao các cột (cách nhau bởi dấu cách): ").split()))
sol = Solution()
ket_qua = sol.maxArea(heights)
print("Diện tích chứa nước lớn nhất là:", ket_qua)

