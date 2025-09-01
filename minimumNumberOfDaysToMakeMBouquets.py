from typing import List

def minDays(bloomDay: List[int], m: int, k: int) -> int:
    # Hàm kiểm tra: giả sử hôm nay là 'days'
    # -> Có làm được m bó hoa hay không?
    def feasible(days) -> bool:
        bouquets = 0   # số bó hoa đã làm được
        flowers = 0    # số bông hoa liên tiếp đã nở

        for bloom in bloomDay:
            if bloom <= days:   # hoa đã nở
                flowers += 1
                if flowers == k:   # đủ k bông liên tiếp -> làm được 1 bó
                    bouquets += 1
                    flowers = 0    # reset để tính bó tiếp theo
            else:
                flowers = 0   # gặp hoa chưa nở thì chuỗi liên tiếp bị ngắt

        return bouquets >= m

    # Nếu tổng số hoa ít hơn m*k thì chắc chắn không thể
    if len(bloomDay) < m * k:
        return -1

    # Tìm ngày nhỏ nhất bằng binary search
    left, right = 1, max(bloomDay)
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
    return left

# -------------------------
# Chạy thử trong VS Code
if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]  # Ngày nở của từng hoa
    m = 3   # cần 3 bó hoa
    k = 1   # mỗi bó cần 1 bông hoa
    print("Kết quả:", minDays(bloomDay, m, k))  # Output mong đợi: 3
