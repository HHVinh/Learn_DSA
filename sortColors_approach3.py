# LeetCode 75 - Sort Colors
# Cách 3: Ghi đè dựa trên so sánh toán học (tmp < 2, tmp < 1)
# Time: O(n), Space: O(1)
# Cách này ngắn nhưng KHÓ HIỂU – dùng để tham khảo

class Solution:
    def sortColors(self, nums):
        zero = 0                      # ranh giới vùng 0
        one = 0                       # ranh giới vùng 1

        for two in range(len(nums)):
            tmp = nums[two]           # lưu giá trị cũ
            nums[two] = 2             # mặc định vị trí hiện tại là 2

            if tmp < 2:               # nếu là 0 hoặc 1
                nums[one] = 1         # ghi đè thành 1
                one += 1              # mở rộng vùng 1

            if tmp < 1:               # nếu là 0
                nums[zero] = 0        # ghi đè thành 0
                zero += 1             # mở rộng vùng 0


def main():
    nums = [2, 0, 2, 1, 1, 0]
    print("Before:", nums)

    Solution().sortColors(nums)

    print("After: ", nums)


if __name__ == "__main__":
    main()
