# LeetCode 75 - Sort Colors
# Cách 2: Ghi đè bằng 3 biến zero, one, two
# Ý tưởng: xây mảng từ trái sang phải
# Time: O(n), Space: O(1)

class Solution:
    def sortColors(self, nums):
        zero = 0                      # ranh giới vùng 0
        one = 0                       # ranh giới vùng 1
        two = 0                       # ranh giới vùng 2

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[two] = 2         # mặc định mở rộng vùng 2
                nums[one] = 1         # đè lại thành 1
                nums[zero] = 0        # đè lại thành 0
                two += 1              # cập nhật ranh giới
                one += 1
                zero += 1

            elif nums[i] == 1:
                nums[two] = 2         # mở rộng vùng 2
                nums[one] = 1         # đè lại thành 1
                two += 1
                one += 1

            else:                     # nums[i] == 2
                nums[two] = 2         # đúng vị trí luôn
                two += 1


def main():
    nums = [2, 0, 2, 1, 1, 0]
    print("Before:", nums)

    Solution().sortColors(nums)

    print("After: ", nums)


if __name__ == "__main__":
    main()
