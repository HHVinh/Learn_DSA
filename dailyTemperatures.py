# 739. Daily Temperatures
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        # Khởi tạo mảng kết quả toàn số 0. 
        # (Nếu ngày nào không tìm được ngày ấm hơn, nó sẽ giữ nguyên giá trị 0)
        res = [0] * n 
        
        # Stack chỉ lưu 'index' của các ngày chưa tìm được ngày ấm hơn
        stack = [] 
        
        # Dùng enumerate để lấy cả index (i) và nhiệt độ (t) cùng lúc
        for i, t in enumerate(temperatures):
            
            # Nếu stack có phần tử VÀ nhiệt độ hôm nay (t) > nhiệt độ của ngày trên đỉnh Stack
            while stack and t > temperatures[stack[-1]]:
                # Lấy index của ngày lạnh hơn ra khỏi stack
                prev_index = stack.pop()
                
                # Tính số ngày phải chờ và gán vào kết quả
                res[prev_index] = i - prev_index
            
            # Bỏ ngày hôm nay vào stack để nó tự đi tìm ngày ấm hơn ở các vòng lặp sau
            stack.append(i)
            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])) # Output: [1, 1, 4, 2, 1, 1, 0, 0]
    print(solution.dailyTemperatures([30, 40, 50, 60])) # Output: [1, 1, 1, 0]
    print(solution.dailyTemperatures([30, 60, 90])) # Output: [1, 1, 0]