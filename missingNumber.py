from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n là số lượng phần tử trong mảng. Các số đúng ra phải có là: 0, 1, 2, ..., n
        n = len(nums)

        # Khởi tạo biến xorr bằng n
        # Vì trong vòng for chỉ chạy từ 0 đến n-1 nên ta XOR trước số n
        xorr = n

        # Duyệt qua từng chỉ số i của mảng
        for i in range(n):
            # a ^ a = 0
            # 0 ^ a = a
            # Ví dụ: nums = [0, 1, 3]
            # Hiểu là (0 ^ 1 ^ 2 ^ 3) ^ (0 ^ 1 ^ 3) = 2

            xorr ^= i ^ nums[i] 
            # => xorr = 3 ^ 0(i = 0) ^ 0(nums[0]) = 3;
            #    xorr = 3 ^ 1(i = 1) ^ 1(nums[1]) = 3;
            #    xorr = 3 ^ 2(i = 2) ^ 3(nums[2]) = 2

        # Sau khi XOR hết:
        # - Các số xuất hiện đủ sẽ bị triệt tiêu
        # - Chỉ còn lại số bị thiếu
        return xorr

def main():
    solution = Solution()
    nums = [3, 0, 1]
    print("Kết quả là: ",solution.missingNumber(nums))  # Output: 2

if __name__ == "__main__":
    main()