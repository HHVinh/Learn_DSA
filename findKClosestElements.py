# 658. Find K Closest Elements
from typing import List
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # Tìm vị trí bắt đầu (left) tốt nhất cho cửa sổ k phần tử
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            
            # So sánh khoảng cách của 'đầu mút bên trái' (mid) 
            # với 'ứng viên ngay sau cửa sổ' (mid + k)
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1  # Bên phải tốt hơn, dịch phải
            else:
                right = mid     # Bên trái tốt hơn (hoặc bằng), giữ lại/dịch trái
                
        return arr[left : left + k]
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.findClosestElements([1,2,3,4,5], 4, 3))  # Output: [1,2,3,4]
    print(solution.findClosestElements([1,2,3,4,5], 4, -1))  # Output: [1,2,3,4]
    print(solution.findClosestElements([1,2,3,4,5], 4, 6))  # Output: [2,3,4,5]
    print(solution.findClosestElements([1,2,3,4,5], 4, 5))  # Output: [2,3,4,5]