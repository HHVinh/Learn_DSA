from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        n = len(nums)

        # Nếu threshold < số phần tử thì chắc chắn không chia được
        if threshold < n:
            return -1

        # Nếu threshold == số phần tử, tức là mỗi phần tử phải "tách riêng"
        # => đáp án là số lớn nhất (max(nums))
        if threshold == n:
            return max(nums)

        # Hàm kiểm tra: với 1 divisor = mid,
        # tổng số phần tử sau khi chia (làm tròn lên) có <= threshold không
        def check(mid: int) -> bool:
            total = 0
            for num in nums:
                # công thức (num + mid - 1) // mid = chia và làm tròn lên
                total += (num + mid - 1) // mid

                # nếu đã vượt threshold thì không cần tính tiếp => return False ngay
                if total > threshold:
                    return False
            return total <= threshold

        # Binary Search trên đoạn [1, max(nums)]
        l, r = 1, max(nums)
        while l < r:
            mid = l + (r - l) // 2  # tránh tràn số (an toàn hơn l+r)//2
            if check(mid):
                # nếu mid chia được thì thử giảm divisor
                r = mid
            else:
                # nếu mid không chia được thì tăng divisor
                l = mid + 1

        return l


# ===============================
# Code chạy thử trong VS Code
# ===============================
if __name__ == "__main__":
    # Cho sẵn mảng nums 5 phần tử
    nums = [19, 23, 7, 45, 12]

    # Nhập threshold từ bàn phím
    threshold = int(input("Nhập threshold: "))

    sol = Solution()
    result = sol.smallestDivisor(nums, threshold)

    print("Kết quả smallestDivisor:", result)
