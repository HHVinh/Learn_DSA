# 560. Subarray Sum Equals K

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # res: số lượng subarray thỏa mãn
        # curSum: tổng prefix hiện tại
        res = 0
        curSum = 0

        # prefixSums[p] = số lần prefix sum p đã xuất hiện
        # Khởi tạo 0:1 để xử lý trường hợp subarray bắt đầu từ index 0
        prefixSums = {0: 1}

        # Duyệt từng phần tử trong mảng
        for num in nums:
            # Cập nhật prefix sum
            curSum += num

            # Ta cần tìm prefix sum trước đó sao cho:
            # curSum - previousSum = k
            # => previousSum = curSum - k
            diff = curSum - k

            # Nếu diff đã xuất hiện trước đó,
            # thì số lần xuất hiện của diff chính là
            # số subarray kết thúc tại vị trí hiện tại có tổng = k
            res += prefixSums.get(diff, 0)

            # Lưu lại prefix sum hiện tại
            prefixSums[curSum] = prefixSums.get(curSum, 0) + 1

        return res


def main():
    solution = Solution()

    # Test case 1
    nums1 = [1, 1, 1]
    k1 = 2
    print("Test 1")
    print("nums =", nums1)
    print("k =", k1)
    print("Result:", solution.subarraySum(nums1, k1))
    print()

    # Test case 2 (có số âm)
    nums2 = [1, 2, 3, -2, 5]
    k2 = 6
    print("Test 2")
    print("nums =", nums2)
    print("k =", k2)
    print("Result:", solution.subarraySum(nums2, k2))
    print()

    # Test case 3
    nums3 = [3, 4, 7, 2, -3, 1, 4, 2]
    k3 = 7
    print("Test 3")
    print("nums =", nums3)
    print("k =", k3)
    print("Result:", solution.subarraySum(nums3, k3))


if __name__ == "__main__":
    main()
