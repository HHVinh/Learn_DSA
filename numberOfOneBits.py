def hammingWeight(n: int) -> int:
    count = 0  # biến đếm số bit 1

    # while n != 0 nghĩa là: còn bit 1 thì còn lặp
    while n != 0:
        print(f"n hiện tại: {n} (nhị phân: {bin(n)[2:]})")

        # n - 1: làm thay đổi bit 1 thấp nhất của n
        print(f"n - 1     : {n - 1} (nhị phân: {bin(n - 1)[2:]})")

        # AND từng bit:
        # 1 & 1 = 1 ---- 1 & 0 = 0 ----- 0 & 1 = 0 ---- 0 & 0 = 0
        n = n & (n - 1)

        print(f"n & (n-1) : {n} (nhị phân: {bin(n)[2:]})")
        print("-" * 40)

        count += 1  # mỗi lần AND xóa được 1 bit 1

    return count


# ===============================
# Chương trình chính
# ===============================
if __name__ == "__main__":
    n = int(input("Nhập số n: "))
    result = hammingWeight(n)
    print(f"\n👉 Số bit 1 của {n} là: {result}")
