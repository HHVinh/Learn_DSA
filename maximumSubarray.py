# maximum_subarray.py
# LeetCode 53 - Maximum Subarray
# Thuật toán: Kadane (O(n) time, O(1) space)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Khởi tạo tổng dãy con đang xét
        current_sum = nums[0]

        # Kết quả lớn nhất tìm được
        max_sum = nums[0]

        # Duyệt từ phần tử thứ 2 trở đi
        for i in range(1, len(nums)):

            # Nếu tổng trước đó âm thì bỏ, bắt đầu lại từ nums[i]
            if current_sum < 0:
                current_sum = nums[i]
            else:
                current_sum = current_sum + nums[i]

            # Cập nhật kết quả lớn nhất
            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


# ================== CHẠY THỬ ==================
if __name__ == "__main__":
    solution = Solution()

    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = solution.maxSubArray(nums)

    print("Mảng đầu vào:", nums)
    print("Tổng dãy con liên tiếp lớn nhất:", result)
