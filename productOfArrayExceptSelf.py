from typing import List  # cần import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Khởi tạo mảng kết quả với giá trị 1
        # res[i] sẽ chứa tích của tất cả các phần tử trừ nums[i]
        res = [1] * len(nums)

        # prefix = tích các phần tử đứng trước vị trí i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix        # lưu tích trước nums[i]
            prefix *= nums[i]      # cập nhật prefix sau khi nhân nums[i]

        # postfix = tích các phần tử đứng sau vị trí i
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):   # duyệt ngược từ cuối về đầu
            res[i] *= postfix      # nhân thêm tích phần sau nums[i]
            postfix *= nums[i]     # cập nhật postfix sau khi nhân nums[i]

        return res

if __name__ == "__main__":
    # Người dùng nhập mảng số nguyên, cách nhau bởi dấu cách
    nums = list(map(int, input("Nhập các số nguyên cách nhau bởi dấu cách: ").split()))
    
    # Gọi hàm
    sol = Solution()
    result = sol.productExceptSelf(nums)
    
    # In kết quả
    print("Kết quả (product except self):", result)
