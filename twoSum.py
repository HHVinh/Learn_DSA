from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Dictionary: dict{key:value}
            # key: khóa (duy nhất, không trùng lặp).
            # value: giá trị (có thể trùng).

        # Tạo 1 dict rỗng
        preMap = {}

        # enumerate(chỉ số, giá trị)
        for i, n in enumerate(nums):
            giaTriConThieu = target - n
            if giaTriConThieu in preMap:
                # Trả về vị trí của giaTriConThieu trong preMap và chỉ số i hiện tại
                return [preMap[giaTriConThieu], i]
            # Nếu không tìm ra thì thêm giá trị n vào dict làm key, value chính là vị trí của n trong nums
            preMap[n] = i
    
s = Solution()

nums = list(map(int, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))
target = int(input("Nhập giá trị mục tiêu: "))

print(s.twoSum(nums,target))

