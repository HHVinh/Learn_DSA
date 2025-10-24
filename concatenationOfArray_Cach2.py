from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(2):
            for num in nums:
                res.append(num)
        return res


if __name__ == "__main__":
    # Nhập mảng ban đầu từ bàn phím (các số cách nhau bởi dấu cách)
    raw_input = input("Nhập mảng ban đầu (các số cách nhau bởi dấu cách): ")
    
    # Chuyển chuỗi nhập vào thành list số nguyên
    nums = list(map(int, raw_input.split()))
    
    # Gọi hàm trong class Solution
    solution = Solution()
    result = solution.getConcatenation(nums)
    
    # In kết quả
    print("Mảng ban đầu:", nums)
    print("Mảng sau khi nhân đôi:", result)
