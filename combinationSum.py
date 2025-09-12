from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []                                # Danh sách kết quả (mảng các tổ hợp)
        nums = sorted(candidates)               # Sắp xếp lại để dễ dừng khi vượt target

        def dfs(i, cur, total):
            # i: chỉ số bắt đầu duyệt (để tránh lặp tổ hợp ngược như [2,3] và [3,2])
            # cur: tổ hợp hiện tại
            # total: tổng hiện tại

            if total == target:                 # Nếu đạt target
                res.append(cur.copy())          # Lưu lại 1 bản sao tổ hợp
                return                          # Quay ra, không tìm tiếp

            for j in range(i, len(nums)):       # Duyệt từ chỉ số i → hết mảng
                if total + nums[j] > target:    # Nếu vượt target thì dừng (vì nums đã sort)
                    return

                cur.append(nums[j])             # Chọn nums[j]
                dfs(j, cur, total + nums[j])    # Đệ quy, cho phép chọn lại nums[j]
                cur.pop()                       # Bỏ nums[j] để thử số khác (backtracking)

        dfs(0, [], 0)                           # Bắt đầu từ index 0, tổ hợp rỗng, tổng = 0
        return res

# ----------------- Chạy thử -----------------

# Cho sẵn mảng
candidates = [2, 3, 6, 7]

# Nhập target từ bàn phím
target = int(input("Nhập target: "))

# Gọi hàm
sol = Solution()
result = sol.combinationSum(candidates, target)

print("Các tổ hợp thỏa mãn:")
print(result)
