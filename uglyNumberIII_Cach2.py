import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # Hàm tính LCM (Least Common Multiple)
        def lcm(x, y):
            return x * y // math.gcd(x, y)

        # Tính LCM các cặp và bộ ba
        ab = lcm(a, b)
        ac = lcm(a, c)
        bc = lcm(b, c)
        abc = lcm(a, bc)

        # Hàm đếm xem có bao nhiêu số ugly <= x
        def countUgly(x):
            return (
                x // a + x // b + x // c
                - x // ab - x // ac - x // bc
                + x // abc
            )

        # Binary search để tìm số nhỏ nhất có ít nhất n số ugly
        l, r = 1, n * min(a, b, c)
        while l < r:
            mid = (l + r) // 2
            if countUgly(mid) >= n:
                r = mid
            else:
                l = mid + 1
        return l


# --- Chạy chương trình ---
if __name__ == "__main__":
    n = int(input("Nhập n: "))
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    c = int(input("Nhập c: "))

    sol = Solution()
    ket_qua = sol.nthUglyNumber(n, a, b, c)
    print(f"Số ugly thứ {n} là: {ket_qua}")
