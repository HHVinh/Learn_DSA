# LeetCode 75 - Sort Colors
# Cách 1: Dutch National Flag (3 con trỏ)
# Time: O(n), Space: O(1)

class Solution:
    def sortColors(self, nums):
        low = 0                       # ranh giới cuối của vùng 0
        mid = 0                       # phần tử đang xét
        high = len(nums) - 1          # ranh giới đầu của vùng 2

        while mid <= high:
            if nums[mid] == 0:        # nếu gặp số 0
                nums[low], nums[mid] = nums[mid], nums[low]  # đưa 0 về trái
                low += 1              # mở rộng vùng 0
                mid += 1              # sang phần tử tiếp theo

            elif nums[mid] == 1:      # nếu là số 1
                mid += 1              # đúng vị trí, chỉ cần đi tiếp

            else:                     # nếu là số 2
                nums[mid], nums[high] = nums[high], nums[mid]  # đưa 2 về phải
                high -= 1             # thu nhỏ vùng chưa xử lý
                # KHÔNG tăng mid vì phần tử mới swap lên chưa được xét


def main():
    nums = [2, 0, 2, 1, 1, 0]          # test mẫu
    print("Before:", nums)

    Solution().sortColors(nums)

    print("After: ", nums)


if __name__ == "__main__":
    main()
