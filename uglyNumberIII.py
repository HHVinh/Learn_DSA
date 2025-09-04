import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Tính bội chung nhỏ nhất (LCM) của các cặp và bộ ba
        ab = a * b // math.gcd(a, b)   # LCM(a, b)
        ac = a * c // math.gcd(a, c)   # LCM(a, c)
        bc = b * c // math.gcd(b, c)   # LCM(b, c)
        abc = a * bc // math.gcd(a, bc)  # LCM(a, b, c)

        # Hàm check(mid): kiểm tra xem có ít nhất n số "xấu" ≤ mid không
        # Công thức áp dụng nguyên lý bao hàm - loại trừ (Inclusion-Exclusion):
        # + mid // a: số bội của a <= mid
        # + mid // b: số bội của b <= mid
        # + mid // c: số bội của c <= mid
        # - mid // ab: trừ đi phần đếm trùng bội của a và b
        # - mid // ac: trừ đi phần đếm trùng bội của a và c
        # - mid // bc: trừ đi phần đếm trùng bội của b và c
        # + mid // abc: cộng lại phần đã bị trừ 2 lần (bội chung của cả 3)
        def check(mid) -> bool:
            total = (
                mid // a + mid // b + mid // c
                - mid // ab - mid // bc - mid // ac
                + mid // abc
            )
            return total >= n  # True nếu có ít nhất n số <= mid

        # Binary Search trên khoảng [1, n * min(a, b, c)]
        l, r = 1, n * min(a, b, c)
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):  # Nếu đủ n số "xấu" trong [1..mid]
                r = mid     # Thu hẹp về bên trái
            else:
                l = mid + 1 # Chưa đủ, dịch sang phải
        return l


# --- Chạy chương trình ---
if __name__ == "__main__":
    # Yêu cầu nhập từ bàn phím
    n = int(input("Nhập n: "))
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))

    sol = Solution()
    ket_qua = sol.nthUglyNumber(n, a, b, c)
    print(f"Số ugly thứ {n} là: {ket_qua}")
