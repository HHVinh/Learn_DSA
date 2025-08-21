class Solution:
    def finMin(self, nums: list[int]) -> int:   # Hàm tìm phần tử nhỏ nhất trong mảng xoay
        l, r = 0, len(nums) - 1                 # l: đầu mảng, r: cuối mảng

        if nums[l] < nums[r]:                   # Nếu mảng vẫn tăng dần bình thường (chưa xoay)
            return nums[l]                      # Trả về phần tử đầu tiên

        while l < r:                            # Khi còn ít nhất 2 phần tử
            m = (l + r) // 2                    # Tính chỉ số giữa
            if nums[m] < nums[r]:               # Nếu mid nhỏ hơn phần tử cuối
                r = m                           # Min nằm bên trái (kể cả mid) → thu hẹp r
            else:                               # Ngược lại, mid >= nums[r]
                l = m + 1                       # Min nằm bên phải mid → bỏ mid
        return nums[l]                          # Khi l == r, đây chính là vị trí min

# --- Chạy thử ---
sol = Solution()
nums = list(map(int, input("Nhập các số cách nhau bởi khoảng trắng: ").split()))
print(sol.finMin(nums))  # In ra phần tử nhỏ nhất

