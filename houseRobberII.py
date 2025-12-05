from typing import List   # Dùng để khai báo kiểu List cho rõ ràng
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Nếu không có nhà nào thì không cướp được tiền
        if not nums:
            return 0

        # Nếu chỉ có 1 nhà thì cướp luôn nhà đó
        if len(nums) == 1:
            return nums[0]

        # Vì các nhà xếp thành vòng tròn nên:
        # - Không thể cướp cả nhà đầu và nhà cuối
        # Ta tách thành 2 trường hợp:
        # 1️⃣ Bỏ nhà đầu → xét từ nhà thứ 2 đến hết
        # 2️⃣ Bỏ nhà cuối → xét từ nhà đầu đến nhà kế cuối
        return max(
            self.helper(nums[1:]),   # TH1: bỏ nhà đầu
            self.helper(nums[:-1])   # TH2: bỏ nhà cuối
        )

    def helper(self, nums):
        # rob1: số tiền tối đa của nhà i-2
        # rob2: số tiền tối đa của nhà i-1
        rob1, rob2 = 0, 0

        # Duyệt từng nhà trong danh sách
        for num in nums:
            # Có 2 lựa chọn:
            # 1. Cướp nhà hiện tại → rob1 + num
            # 2. Bỏ qua nhà hiện tại → giữ rob2
            newRob = max(rob1 + num, rob2)

            # Dịch rob1, rob2 sang vòng tiếp theo
            rob1 = rob2
            rob2 = newRob

        # rob2 là số tiền lớn nhất có thể cướp được
        return rob2


# ================== PHẦN CHẠY CHƯƠNG TRÌNH ==================

if __name__ == "__main__":
    nums = list(map(int, input("Nhập danh sách tiền (cách nhau bởi dấu cách): ").split()))

    solution = Solution()
    result = solution.rob(nums)

    print("Số tiền lớn nhất có thể cướp được là:", result)
