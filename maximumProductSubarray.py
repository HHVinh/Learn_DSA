
from typing import List
# Hàm tìm tích lớn nhất của một subarray liên tục trong danh sách nums
class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        # Giá trị trả về ban đầu là phần tử đầu tiên
        res = nums[0]

        # curMax: tích lớn nhất kết thúc tại vị trí hiện tại
        # curMin: tích nhỏ nhất kết thúc tại vị trí hiện tại
        # Bắt đầu từ 1 để không ảnh hưởng khi nhân số đầu tiên
        curMax = 1
        curMin = 1

        # Duyệt từng phần tử trong mảng
        for num in nums:

            # Lưu lại giá trị tạm của curMax trước khi cập nhật vì curMin sẽ dùng curMax cũ để tính
            temp = curMax * num

            # Cập nhật curMax:
            # - num * curMax: nhân tiếp với chuỗi trước (nếu nó tốt)
            # - num * curMin: trong trường hợp num âm => âm * âm = dương
            # - num: bắt đầu chuỗi mới
            curMax = max(num * curMax, num * curMin, num)

            # Cập nhật curMin:
            # - temp (curMax cũ * num)
            # - num * curMin: từng âm/dương có thể cho kết quả nhỏ hơn
            # - num: tự nó có thể là nhỏ nhất
            curMin = min(temp, num * curMin, num)

            # Cập nhật kết quả lớn nhất tìm được
            res = max(res, curMax)

        # Trả về kết quả cuối cùng
        return res


if __name__ == "__main__":
    # Bạn có thể sửa input dưới đây để test
    nums = [2, 3, -2, 4]

    solution = Solution()
    result = solution.maxProduct(nums)

    print("Mảng:", nums)
    print("Tích lớn nhất của subarray:", result)