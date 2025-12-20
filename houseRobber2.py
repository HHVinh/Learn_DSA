from typing import List   # Import List để dùng kiểu List[int]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:                     # Nếu danh sách rỗng → không cướp được gì
            return 0

        if len(nums) == 1:               # Nếu chỉ có 1 nhà → cướp nhà đó
            return nums[0]

        dp = [0] * len(nums)             # dp[i]: số tiền tối đa cướp được từ nhà 0 → i
        dp[0] = nums[0]                  # Nhà đầu tiên: chỉ có thể cướp chính nó
        dp[1] = max(nums[0], nums[1])    # Nhà 1: chọn cướp nhà 0 hoặc nhà 1

        for i in range(2, len(nums)):    # Duyệt từ nhà thứ 2 trở đi
            dp[i] = max(
                dp[i - 1],               # Không cướp nhà i → giữ kết quả trước đó
                nums[i] + dp[i - 2]      # Cướp nhà i → cộng với dp của i-2
            )

        return dp[-1]                    # Kết quả là giá trị cuối cùng trong dp


# ================== PHẦN CHẠY TRÊN VS CODE ==================
if __name__ == "__main__":
    solution = Solution()                # Tạo đối tượng Solution

    nums1 = [1, 2, 3, 1]
    nums2 = [2, 7, 9, 3, 1]
    nums3 = [2, 1, 1, 2]

    print("Input:", nums1, "=> Output:", solution.rob(nums1))
    print("Input:", nums2, "=> Output:", solution.rob(nums2))
    print("Input:", nums3, "=> Output:", solution.rob(nums3))
