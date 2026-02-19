# 219. Contains Duplicate II

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Kiểm tra xem trong mảng nums có tồn tại hai phần tử giống nhau
        sao cho khoảng cách chỉ số của chúng không vượt quá k hay không.
        """

        # Dictionary lưu vị trí xuất hiện gần nhất của mỗi số
        mp = {}

        # Duyệt mảng cùng với chỉ số
        for i, num in enumerate(nums):

            # Nếu số đã từng xuất hiện trước đó
            if num in mp:
                # Kiểm tra khoảng cách giữa 2 lần xuất hiện
                if i - mp[num] <= k:
                    return True

            # Cập nhật vị trí xuất hiện gần nhất của num
            mp[num] = i

        # Duyệt hết mảng mà không thỏa điều kiện
        return False


def main():
    """
    Hàm main để chạy thử trong VS Code
    """

    solution = Solution()

    # Test case 1
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print("Test 1:")
    print("nums =", nums1)
    print("k =", k1)
    print("Result:", solution.containsNearbyDuplicate(nums1, k1))
    print()

    # Test case 2
    nums2 = [1, 0, 1, 1]
    k2 = 1
    print("Test 2:")
    print("nums =", nums2)
    print("k =", k2)
    print("Result:", solution.containsNearbyDuplicate(nums2, k2))
    print()

    # Test case 3
    nums3 = [1, 2, 3, 1, 2, 3]
    k3 = 2
    print("Test 3:")
    print("nums =", nums3)
    print("k =", k3)
    print("Result:", solution.containsNearbyDuplicate(nums3, k3))


# Chỉ chạy main khi file được chạy trực tiếp
if __name__ == "__main__":
    main()
