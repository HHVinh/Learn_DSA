# ==========================================
# LeetCode 338 - Counting Bits
# Cách 2: DP + Brian Kernighan (tối ưu nhất)
# ==========================================

def countBits_and(n: int):
    # dp[i] = số bit 1 của i
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # i & (i - 1): xóa bit 1 thấp nhất của i => kết quả là số nhỏ hơn i và đã có dp
        # +1 vì ta vừa xóa 1 bit 1
        dp[i] = dp[i & (i - 1)] + 1

    return dp


# ===============================
# Chạy thử trong VS Code
# ===============================
if __name__ == "__main__":
    n = int(input("Nhập n: "))
    result = countBits_and(n)
    print("Kết quả:", result)
