# 42. Trapping Rain Water
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        
        # leftMax: Bức tường cao nhất đã gặp từ phía bên trái
        # rightMax: Bức tường cao nhất đã gặp từ phía bên phải
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            
            # Nguyên tắc: Nước luôn bị giới hạn bởi bức tường THẤP HƠN trong hai phía (trái/phải).
            
            if leftMax < rightMax: # Nếu tường chắn bên trái THẤP HƠN tường chắn bên phải:
                # => Ta biết chắc chắn rằng nước ở vị trí `l+1` sẽ bị chặn bởi `leftMax`.
                # Dù ở giữa hay bên phải có tường cao bao nhiêu đi nữa thì `leftMax` vẫn là 
                # "nút thắt cổ chai" (bottleneck), nên ta an tâm tính toán theo `leftMax`.
                
                l += 1  # Di chuyển con trỏ trái sang vị trí tiếp theo cần tính
                
                # Cập nhật leftMax: Xem cột mới này có cao hơn tường cũ không?
                leftMax = max(leftMax, height[l])
                
                # - Nếu cột hiện tại (height[l]) thấp hơn leftMax -> Có đọng nước.
                # - Nếu cột hiện tại chính là leftMax mới -> leftMax - height[l] = 0 (Không đọng).
                res += leftMax - height[l]
                
            else: # Ngược lại, nếu tường chắn bên phải THẤP HƠN hoặc bằng tường chắn bên trái:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res
    
if __name__ == "__main__":
    solution = Solution()
    height = [4,2,0,3,2,5]
    print(solution.trap(height))  # Output: 9