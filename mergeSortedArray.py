# 88: Merge Sorted Array

from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        last = m + n - 1           # vị trí cuối cùng của nums1 sau khi merge
        i = m - 1                  # con trỏ cuối phần hợp lệ của nums1
        j = n - 1                  # con trỏ cuối của nums2

        # chạy cho đến khi nums2 hết phần tử
        while j >= 0:
            # nếu nums1 còn phần tử và phần tử nums1 lớn hơn nums2
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[last] = nums1[i]   # đưa phần tử lớn hơn về cuối
                i -= 1                   # dịch con trỏ nums1
            else:
                nums1[last] = nums2[j]   # đưa phần tử của nums2 vào
                j -= 1                   # dịch con trỏ nums2

            last -= 1                    # dịch vị trí ghi tiếp theo


if __name__ == "__main__":
    solution = Solution()
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(nums1)  # Output: [1,2,2,3,5