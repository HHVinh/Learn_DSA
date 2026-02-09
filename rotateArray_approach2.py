# 189. Rotate Array

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Xoay mảng sang phải k bước bằng cách đảo mảng thủ công
        """

        n = len(nums)
        k %= n  # xử lý khi k > n

        # Hàm đảo ngược đoạn [l, r]
        def reverse(l: int, r: int) -> None:
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Bước 1: đảo ngược toàn bộ mảng
        reverse(0, n - 1)

        # Bước 2: đảo ngược k phần tử đầu
        reverse(0, k - 1)

        # Bước 3: đảo ngược phần còn lại
        reverse(k, n - 1)


def main():
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Before rotate:", nums)
    solution.rotate(nums, k)
    print("After rotate :", nums)


if __name__ == "__main__":
    main()
