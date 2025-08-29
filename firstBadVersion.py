def isBadVersion(version: int) -> bool:
    return version == n


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l < r:
            mid = l + (r - l) // 2  # tránh overflow (không quan trọng ở Python nhưng là best practice)
            if isBadVersion(mid):
                # mid là bad => first bad nằm ở [l..mid]
                r = mid
            else:
                # ngược lại => first bad nằm ở [mid+1..r]
                l = mid + 1
        return l


if __name__ == "__main__":
    # Nhập số lượng phiên bản
    n = int(input("Nhập số lượng phiên bản n: "))

    result = Solution().firstBadVersion(n)
    print(f"Phiên bản lỗi đầu tiên là: {result}")
