from typing import List            # import để dùng kiểu List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Hàm kiểm tra: với divisor = mid thì tổng có <= threshold không
        def check(mid: int) -> bool:
            count = 0                              # tổng sau khi chia
            for num in nums:                       # duyệt từng số trong nums
                count += (num + mid - 1) // mid    # ceil(num / mid)
                if count > threshold:              # nếu vượt ngưỡng
                    return False                   # mid quá nhỏ
            return True                            # mid hợp lệ

        l, r = 1, max(nums)                        # divisor nhỏ nhất là 1, lớn nhất là max(nums)

        while l < r:                               # binary search
            mid = l + (r - l) // 2                 # tránh overflow (chuẩn)
            if check(mid):                         # nếu mid hợp lệ
                r = mid                            # thử divisor nhỏ hơn
            else:
                l = mid + 1                        # mid quá nhỏ → tăng divisor

        return l                                   # l là divisor nhỏ nhất thỏa điều kiện

if __name__ == "__main__":
    sol = Solution()

    nums = [1, 2, 5, 9]
    threshold = 6

    result = sol.smallestDivisor(nums, threshold)
    print(result)   # Kết quả đúng: 5
