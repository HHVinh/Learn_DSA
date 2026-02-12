# 334. Reverse String

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1


if __name__ == "__main__":
    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)
    print(s)  # Output: ["o", "l", "l", "e", "h"]