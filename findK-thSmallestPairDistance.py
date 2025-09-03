from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # Sắp xếp mảng để các phần tử theo thứ tự tăng dần
        nums.sort()
        n = len(nums)

        # Hàm kiểm tra xem có đủ ít nhất k cặp có khoảng cách <= mid không
        def check(mid) -> bool:
            count = 0       # đếm số cặp thỏa mãn
            l = 0           # con trỏ trái
            # duyệt từng phần tử làm con trỏ phải
            for r in range(n):
                # dịch con trỏ trái để đảm bảo khoảng cách <= mid
                while nums[r] - nums[l] > mid:
                    l += 1
                # số cặp mới sinh ra với nums[r] chính là (r - l)
                count += r - l
            # nếu số cặp đủ lớn hơn hoặc bằng k thì trả về True
            return count >= k

        # khoảng tìm kiếm nhị phân: từ 0 đến khoảng cách lớn nhất
        l, r = 0, nums[-1] - nums[0]

        # binary search để tìm khoảng cách nhỏ nhất
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                # nếu có đủ cặp với khoảng cách <= mid, thu hẹp về trái
                r = mid
            else:
                # nếu chưa đủ cặp, dịch sang phải để tăng khoảng cách
                l = mid + 1
        return l

# ============================
# Code chạy thử trong VS Code
# ============================

if __name__ == "__main__":
    nums = [1, 3, 1, 5, 0, 9]  # Cho sẵn mảng
    print("Mảng:", nums)
    k = int(input("Nhập k: "))  # Yêu cầu nhập k
    sol = Solution()
    ket_qua = sol.smallestDistancePair(nums, k)
    print(f"{k}-th khoảng cách nhỏ nhất là:", ket_qua)
