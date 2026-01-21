# ==========================================
# LeetCode 338 - Counting Bits
# Cách 1: DP + dịch bit (dễ hiểu nhất)
# ==========================================

def countBits_shift(n: int):
    # dp[i] = số bit 1 của i
    dp = [0] * (n + 1)

    # Bắt đầu từ 1 vì dp[0] = 0 đã biết
    for i in range(1, n + 1):
        # i >> 1  : dịch phải 1 bit (tương đương chia 2) => số này sẽ luôn nhỏ hơn i và đã có dp[]
        # i & 1   : kiểm tra bit cuối (1 nếu i lẻ, 0 nếu i chẵn) => nếu i lẻ thì cộng thêm 1 vào dp[] đã có
        dp[i] = dp[i >> 1] + (i & 1)

    return dp


# ===============================
# Chạy thử trong VS Code
# ===============================
if __name__ == "__main__":
    n = int(input("Nhập n: "))
    result = countBits_shift(n)
    print("Kết quả:", result)
