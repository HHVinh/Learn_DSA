from typing import List
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        # Nếu số hoa ít hơn số bó cần * số hoa mỗi bó => không thể tạo bó
        if len(bloomDay) < m * k:
            return -1
        
        # Hàm check(mid): Kiểm tra xem nếu chờ đến ngày mid,
        # ta có tạo được ít nhất m bó hoa (mỗi bó có k hoa liên tiếp) hay không
        def check(mid) -> bool:
            bongHoa = 0   # số hoa liên tiếp đã nở
            boHoa = 0     # số bó đã tạo được

            for num in bloomDay:
                if num <= mid:        # hoa này đã nở vào ngày mid
                    bongHoa += 1
                    if bongHoa == k:  # nếu đủ k hoa liên tiếp
                        boHoa += 1    # tạo được 1 bó
                        bongHoa = 0   # reset, bắt đầu đếm chuỗi mới
                else:
                    bongHoa = 0       # gặp hoa chưa nở thì chuỗi bị đứt, reset

            return boHoa >= m

            # 💡 Cách 2 (tương tự logic trên nhưng gọn hơn):
            # if num > mid:
            #     bongHoa = 0
            # else:
            #     boHoa += (bongHoa + 1) // k
            #     bongHoa = (bongHoa + 1) % k

        # Binary search để tìm ngày nhỏ nhất thỏa điều kiện
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid   # có thể tạo đủ bó => thử ngày nhỏ hơn
            else:
                l = mid + 1  # chưa đủ bó => cần thêm ngày
        return l


# ========================
# Code để test trong VS Code
# ========================
if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m, k = 3, 1

    sol = Solution()
    print("Kết quả:", sol.minDays(bloomDay, m, k))  # Dự kiến: 3

    # Thử thêm test khác
    print("Test 2:", sol.minDays([7, 7, 7, 7, 12, 7, 7], 2, 3))  # Dự kiến: 12
    print("Test 3:", sol.minDays([1000000000, 1000000000], 1, 1))  # Dự kiến: 1000000000
    print("Test 4:", sol.minDays([1, 10, 3, 10, 2], 3, 2))  # Dự kiến: -1
