from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
    
    def hasDuplicate2(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
nums = list(map(int,input("Nhập các số cách nhau bởi khoảng trắng: ").split()))

# Nếu nhập kí tự thì chỉ cần dùng input
# nums = input("Nhập các ký tự cách nhau bởi khoảng trắng: ").split()
""" Giải thích:
    - các hàm split, len, set vẫn áp dụng được chữ và số
    - .split() → tách chuỗi thành list con theo dấu cách.
    - map(int, ...) → chuyển từng phần tử sang int. => không trả về list nữa
    - list(...) → biến kết quả map thành list. """
s = Solution()
print("Cách 1: ")
print(s.hasDuplicate(nums))
print("Cách 2:")
print(s.hasDuplicate2(nums))
