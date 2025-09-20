from typing import List  # để dùng List[int]

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}  # dictionary lưu số lần xuất hiện của từng số

        # duyệt qua từng phần tử trong nums
        for num in nums:
            if num in count:
                count[num] += 1   # nếu đã có trong dictionary thì cộng thêm 1
            else:
                count[num] = 1    # nếu chưa có thì khởi tạo = 1
        
        # tìm key (số) có value (số lần xuất hiện) lớn nhất
        res = max(count, key=count.get)

        # kiểm tra xem res có thật sự là majority element không
        if count[res] > len(nums) // 2:
            return res
        else:
            return None  # nếu không có majority thì trả về None

# --- TEST ---
nums = [3, 3, 4, 2, 3, 3, 5]
solution = Solution()
print(solution.majorityElement(nums))  # Kết quả: 3
