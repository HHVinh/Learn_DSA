# 881. Boats to Save People
# Bài này giới hạn 1 lần thuyền chở tối đa 2 người với tổng trọng lượng không vượt quá limit.
from typing import List
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  # BƯỚC 1: Sắp xếp
        l, r = 0, len(people) - 1  # BƯỚC 2: Khởi tạo 2 con trỏ
        boats = 0

        while l <= r:  # BƯỚC 3: Duyệt cho đến khi hết người
            # Logic ghép cặp
            if people[l] + people[r] <= limit:
                l += 1  # Nếu ghép được, người nhẹ (l) cũng được lên thuyền
            
            r -= 1      # Người nặng (r) LUÔN LUÔN lên thuyền (dù đi chung hay đi một mình)
            boats += 1  # Tăng số lượng thuyền

        return boats

if __name__ == "__main__":
    solution = Solution()
    # Ví dụ kiểm thử
    print(solution.numRescueBoats([1,2], 3))  # Output: 1
    print(solution.numRescueBoats([3,2,2,1], 3))  # Output: 3
    print(solution.numRescueBoats([3,5,3,4], 5))  # Output: 4