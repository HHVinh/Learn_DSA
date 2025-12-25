from typing import List

class SolutionManual:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []

        for num in nums:
            # Tự tìm vị trí chèn (giống bisect_left)
            left, right = 0, len(tails)

            while left < right:
                mid = (left + right) // 2

                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # left là vị trí đầu tiên >= num
            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)


# =========================
# Code test chạy VS Code
# =========================
if __name__ == "__main__":
    sol = SolutionManual()

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print("LIS length (manual):", sol.lengthOfLIS(nums))  # 4
