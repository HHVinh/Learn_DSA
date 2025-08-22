class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1       # khởi tạo 2 biến trỏ đầu và cuối mảng
        # Tìm pivot (vị trí phần tử nhỏ nhất)
        while l < r:
            m = (l + r) // 2          # lấy chỉ số giữa
            if nums[m] > nums[r]:     # nếu phần tử giữa > phần tử cuối
                l = m + 1             # pivot nằm bên phải
            else:
                r = m                 # pivot nằm bên trái hoặc chính giữa
        
        pivot = l                     # pivot là vị trí phần tử nhỏ nhất
        l, r = 0, len(nums) - 1       # reset lại phạm vi tìm kiếm

        # Xác định target nằm ở nửa nào
        if target >= nums[pivot] and target <= nums[r]:
            l = pivot                 # target nằm bên phải pivot
        else:
            r = pivot - 1             # target nằm bên trái pivot
        
        # Binary search trong nửa đã chọn
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:     # tìm thấy target
                return m
            elif nums[m] < target:    # target nằm bên phải
                l = m + 1
            else:                     # target nằm bên trái
                r = m - 1
        
        return -1                     # không tìm thấy

if __name__ == "__main__":
    nums = list(map(int, input("Nhập mảng (cách nhau bởi dấu cách): ").split()))
    target = int(input("Nhập giá trị cần tìm: "))

    sol = Solution()
    result = sol.search(nums, target)

    if result != -1:
        print(f"Tìm thấy {target} tại vị trí index {result}")
    else:
        print(f"Không tìm thấy {target} trong mảng")
