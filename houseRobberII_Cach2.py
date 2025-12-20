from typing import List   # Dùng để khai báo kiểu List[int]

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:                 # Nếu chỉ có 1 nhà → cướp nhà đó
            return nums[0]

        # Vì nhà nằm thành vòng tròn:
        # - Không thể cướp đồng thời nhà đầu và nhà cuối
        # → Chia thành 2 trường hợp và lấy max
        return max(
            self.helper(nums[1:]),         # Trường hợp 1: bỏ nhà đầu, cướp từ nhà 1 → cuối
            self.helper(nums[:-1])         # Trường hợp 2: bỏ nhà cuối, cướp từ nhà đầu → n-2
        )

    def helper(self, nums: List[int]) -> int:
        if not nums:                       # Nếu danh sách rỗng
            return 0

        if len(nums) == 1:                 # Nếu chỉ có 1 nhà
            return nums[0]

        dp = [0] * len(nums)               # dp[i]: tiền tối đa cướp được từ nhà 0 → i
        dp[0] = nums[0]                    # Nhà đầu tiên: chỉ cướp được chính nó
        dp[1] = max(nums[0], nums[1])      # Nhà thứ 2: chọn cướp nhà 0 hoặc nhà 1

        for i in range(2, len(nums)):      # Duyệt từ nhà thứ 2 trở đi
            dp[i] = max(
                dp[i - 1],                 # Không cướp nhà i
                nums[i] + dp[i - 2]        # Cướp nhà i → cộng với dp[i-2]
            )

        return dp[-1]                      # Kết quả là giá trị lớn nhất cuối cùng


# ================== PHẦN CHẠY TRÊN VS CODE ==================
if __name__ == "__main__":
    solution = Solution()

    nums1 = [2, 3, 2]
    nums2 = [1, 2, 3, 1]
    nums3 = [1, 2, 3]

    print("Input:", nums1, "=> Output:", solution.rob(nums1))
    print("Input:", nums2, "=> Output:", solution.rob(nums2))
    print("Input:", nums3, "=> Output:", solution.rob(nums3))
