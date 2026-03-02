# 42. Trapping Rain Water
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lmax, rmax = 0, 0
        water = 0
        
        while l <= r:
            
            # Nguyên tắc: Nước bị giới hạn bởi thanh chắn THẤP HƠN.
            # Nếu bên Trái thấp hơn (hoặc bằng) bên Phải:
            # -> Ta chắc chắn nước ở l chỉ phụ thuộc vào lmax (vì bên phải đã có cái cao hơn đỡ rồi).
            if height[l] <= height[r]:
                
                # Nếu cột hiện tại cao hơn tường chắn trái cũ -> Cập nhật tường mới
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    # Nếu thấp hơn tường -> Có chỗ trũng -> Tính nước
                    water += lmax - height[l]
                
                # Xử lý xong cột l, dịch sang phải
                l += 1
                
            # Ngược lại: Bên Phải thấp hơn bên Trái
            # -> Nước ở r chỉ phụ thuộc vào rmax.
            else:
                
                # Tương tự: Cập nhật tường phải hoặc tính nước
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    water += rmax - height[r]
                
                # Xử lý xong cột r, dịch sang trái
                r -= 1
                
        return water
    
if __name__ == "__main__":
    solution = Solution()
    height = [4,2,0,3,2,5]
    print(solution.trap(height))  # Output: 9