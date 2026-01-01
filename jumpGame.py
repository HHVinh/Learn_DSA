from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1          # Vị trí cần phải nhảy tới (ban đầu là ô cuối)

        # Duyệt từ vị trí kế cuối về đầu mảng
        for i in range(len(nums) - 2, -1, -1):

            # Nếu từ i có thể nhảy tới (hoặc vượt) goal hiện tại
            if i + nums[i] >= goal:
                goal = i              # Cập nhật goal mới về vị trí i

        # Nếu goal có thể lùi về vị trí 0 thì xuất phát từ đầu tới được cuối
        return goal == 0


# ================== CHẠY THỬ TRONG VS CODE ==================
if __name__ == "__main__":
    solution = Solution()

    # Test 1
    nums1 = [2, 3, 1, 1, 4]
    print("Input:", nums1)
    print("Can jump:", solution.canJump(nums1))  # True

    print("-" * 40)

    # Test 2
    nums2 = [3, 2, 1, 0, 4]
    print("Input:", nums2)
    print("Can jump:", solution.canJump(nums2))  # False
