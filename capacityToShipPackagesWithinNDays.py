from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        Bài toán: Tìm sức chứa nhỏ nhất của tàu sao cho có thể chở hết hàng 'weights' trong đúng 'days' ngày.
        Ý tưởng: Dùng binary search trên khoảng sức chứa có thể.
        """

        # Hàm kiểm tra: với sức chứa capacity, có chở xong trong 'days' ngày không?
        def check(capacity) -> bool:
            day = 1       # Bắt đầu từ ngày thứ 1
            total = 0     # Tổng cân nặng trong ngày hiện tại
            for w in weights:
                total += w
                if total > capacity:
                    # Nếu vượt quá tải trọng => sang ngày tiếp theo
                    day += 1
                    total = w   # Bắt đầu ngày mới với kiện hàng hiện tại
                    if day > days:
                        return False  # Không thể chở kịp trong days ngày
            return True  # Chở xong trong <= số ngày cho phép

        # Giới hạn tìm kiếm:
        # - Tải trọng nhỏ nhất = max(weights) (ít nhất phải chở được kiện nặng nhất)
        # - Tải trọng lớn nhất = sum(weights) (chở tất cả trong 1 ngày)
        l, r = max(weights), sum(weights)

        # Binary search để tìm tải trọng nhỏ nhất thỏa điều kiện
        while l < r:
            m = l + (r - l) // 2
            if check(m):
                # Nếu với capacity m mà chở được trong 'days' ngày => thử tải trọng nhỏ hơn nữa
                r = m
            else:
                # Nếu không chở kịp => phải tăng tải trọng
                l = m + 1

        # Khi vòng lặp kết thúc: l == r. Đây là tải trọng nhỏ nhất có thể chở trong 'days' ngày
        return l


if __name__ == "__main__":
    # Cho sẵn danh sách kiện hàng (đã cố định)
    weights = [1,2,3,4,5,6,7,8,9,10]
    print("Danh sách kiện hàng:", weights)

    # Nhập số ngày cần giao
    days = int(input("Nhập số ngày cần giao: "))

    # Gọi hàm giải
    result = Solution().shipWithinDays(weights, days)
    print(f"Sức chứa nhỏ nhất của tàu để giao trong {days} ngày là: {result}")
