# 189. Rotate Array

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Xoay mảng sang phải k bước bằng cách:
        1. Đảo ngược toàn bộ mảng
        2. Đảo ngược k phần tử đầu
        3. Đảo ngược phần còn lại
        """

        n = len(nums)
        k %= n  # xử lý khi k > n

        # Bước 1: đảo ngược toàn bộ mảng
        nums.reverse()

        # Bước 2: đảo ngược k phần tử đầu
        nums[:k] = reversed(nums[:k])

        # Bước 3: đảo ngược phần còn lại
        nums[k:] = reversed(nums[k:])


def main():
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3

    print("Before rotate:", nums)
    solution.rotate(nums, k)
    print("After rotate :", nums)


if __name__ == "__main__":
    main()
