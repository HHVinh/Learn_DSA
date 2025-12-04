from typing import List   # Dùng để khai báo kiểu List cho rõ ràng

class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1: số tiền lớn nhất có thể cướp được từ nhà i-2 trở về trước
        # rob2: số tiền lớn nhất có thể cướp được đến nhà i-1
        rob1, rob2 = 0, 0

        # Duyệt từng nhà trong danh sách nums
        for num in nums:
            # temp là số tiền lớn nhất có thể có ở nhà hiện tại
            # Có 2 lựa chọn:
            # 1. Cướp nhà hiện tại: num + rob1
            # 2. Không cướp nhà hiện tại: giữ nguyên rob2
            temp = max(num + rob1, rob2)

            # Cập nhật lại rob1 và rob2 cho vòng lặp tiếp theo
            rob1 = rob2
            rob2 = temp

        # Kết quả cuối cùng là số tiền lớn nhất có thể cướp được
        return rob2


# ================== PHẦN CHẠY CHƯƠNG TRÌNH ==================

if __name__ == "__main__":
    nums = list(map(int, input("Nhập danh sách tiền (cách nhau bởi dấu cách): ").split()))

    solution = Solution()
    result = solution.rob(nums)

    print("Số tiền lớn nhất có thể cướp được là:", result)
