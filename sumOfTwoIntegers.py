class Solution:
    def getSum(self, a: int, b: int) -> int:
        # mask giúp giả lập số nguyên 32-bit (Python không giới hạn số bit)
        mask = 0xFFFFFFFF        # = 32 bit toàn 1
        max_int = 0x7FFFFFFF     # = số dương lớn nhất của int 32-bit

        # Lặp cho tới khi không còn carry
        while b != 0:
            # 1️⃣ carry: tìm chỗ cả a và b đều là 1
            # & : chỉ giữ bit 1 nếu cả hai cùng là 1
            # << 1 : dời carry sang bit bên trái
            carry = (a & b) << 1

            # 2️⃣ cộng không nhớ
            # ^ : nếu khác nhau thì 1, giống nhau thì 0
            a = (a ^ b) & mask

            # 3️⃣ b giữ carry để cộng tiếp vòng sau
            b = carry & mask

        # Nếu a <= max_int → số dương bình thường
        # Nếu > max_int → là số âm (bù 2), cần chuyển lại
        return a if a <= max_int else ~(a ^ mask)


# ======================
# MAIN - chạy trong VS Code
# ======================
if __name__ == "__main__":
    sol = Solution()

    tests = [
        (1, 2),
        (5, 7),
        (-3, 1),
        (-4, -6),
        (10, -3)
    ]

    for a, b in tests:
        print(f"getSum({a}, {b}) = {sol.getSum(a, b)}")
