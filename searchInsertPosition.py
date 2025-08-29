from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        Tìm vị trí chèn target vào trong mảng nums (đã sắp xếp tăng dần).
        Nếu target đã tồn tại, trả về index của nó.
        Nếu chưa có, trả về index mà nó nên được chèn vào để giữ thứ tự.
        """

        # Ở đây r = len(nums) thay vì len(nums)-1,
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2

            # Nếu phần tử giữa nhỏ hơn target thì target chắc chắn nằm bên phải
            if nums[m] < target:
                l = m + 1
            else:
                # Ngược lại, target nằm bên trái (hoặc chính tại m)
                r = m

        # Khi vòng lặp kết thúc l == r, => đây chính là vị trí cần chèn target
        return l

if __name__ == "__main__":
    # Cho sẵn một mảng đã sắp xếp tăng dần
    nums = [1, 3, 5, 6]
    print("Mảng gốc:", nums)

    # Người dùng nhập target
    target = int(input("Nhập target cần tìm/chèn: "))

    # Gọi hàm
    result = Solution().searchInsert(nums, target)
    print(f"Target {target} nên nằm ở vị trí index: {result}")
