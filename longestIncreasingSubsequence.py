from bisect import bisect_left, bisect_right
from typing import List

class SolutionBisect:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # tails[i] = giá trị nhỏ nhất có thể kết thúc LIS dài i+1
        tails = []

        for num in nums:
            # Tìm vị trí đầu tiên >= num
            pos = bisect_left(tails, num)

            if pos == len(tails):
                # num lớn hơn tất cả → mở rộng LIS
                tails.append(num)
            else:
                # thay thế để giữ giá trị kết thúc nhỏ nhất có thể
                tails[pos] = num

        return len(tails)

# =========================
# Ví dụ minh họa bisect
# =========================
    """
    Giải thích:
    arr = [2, 4, 4, 4, 6, 8]
           0  1  2  3  4  5

    bisect_left  → vị trí đầu tiên >= x
    bisect_right → vị trí đầu tiên > x

    bisect_left(arr, 4)  = 1
    bisect_right(arr, 4) = 4
    """


# =========================
# Code test chạy VS Code
# =========================
if __name__ == "__main__":
    sol = SolutionBisect()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS length (bisect):", sol.lengthOfLIS(nums))
