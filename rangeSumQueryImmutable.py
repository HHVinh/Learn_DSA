from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        """
        Hàm khởi tạo:
        - Nhận mảng nums
        - Tạo mảng cộng dồn (prefix sum) để tính tổng nhanh
        """
        # Bước 1: Thêm 0 vào đầu để dễ tính toán
        # self.nums[0] = 0, self.nums[1] = nums[0], ...
        self.nums = [0] + nums

        # Bước 2: Cộng dồn từng phần tử (tính prefix sum)
        for i in range(1, len(self.nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        """
        Trả về tổng các phần tử trong đoạn [left, right]
        bằng cách lấy hiệu giữa hai mốc cộng dồn.
        """
        return self.nums[right + 1] - self.nums[left]


# -----------------------------
# CHẠY THỬ TRONG VS CODE
# -----------------------------
if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    arr = NumArray(nums)

    print("Mảng gốc:", nums)
    print("Tổng đoạn [0, 2] =", arr.sumRange(0, 2))  # -2 + 0 + 3 = 1
    print("Tổng đoạn [2, 5] =", arr.sumRange(2, 5))  # 3 - 5 + 2 - 1 = -1
    print("Tổng đoạn [0, 5] =", arr.sumRange(0, 5))  # Tổng toàn mảng = -3
