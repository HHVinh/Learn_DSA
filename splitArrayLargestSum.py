from typing import List
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Kiểm tra "hold" (giới hạn tổng tối đa mỗi nhóm), có thể chia nums thành <= k nhóm hay không.
        def check(hold) -> bool:
            dem, tong = 1, 0  # dem = số nhóm hiện tại, tong = tổng nhóm đang cộng dồn
            for num in nums:
                tong += num
                # Nếu tổng vượt quá "hold", bắt buộc phải tách sang nhóm mới
                if tong > hold:
                    tong = num       # nhóm mới bắt đầu với phần tử hiện tại
                    dem += 1         # tăng số nhóm lên 1
                    if dem > k:      # nếu số nhóm vượt quá k thì thất bại
                        return False
            return True  # nếu chia được trong <= k nhóm thì hợp lệ

        # Tìm giá trị nhỏ nhất của "tổng lớn nhất" khi chia mảng thành k nhóm
        l, r = max(nums), sum(nums)  # l: nhỏ nhất có thể, r: lớn nhất có thể
        while l < r:
            m = l + (r - l) // 2     # mid: giá trị "tổng nhóm" thử nghiệm
            if check(m):
                r = m                # nếu chia được, thử giảm giới hạn xuống
            else:
                l = m + 1            # nếu không chia được, phải tăng giới hạn
        return l  # l chính là kết quả cuối cùng

if __name__ == "__main__":

    nums = [4, 2, 5, 7, 9, 2, 5, 6]
    # Nhập số k
    k = int(input("Nhập số k: "))

    sol = Solution()
    ket_qua = sol.splitArray(nums, k)
    print("Kết quả (tổng lớn nhất nhỏ nhất có thể):", ket_qua)

