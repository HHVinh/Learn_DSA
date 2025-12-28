class SolutionLeftToRight:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Đảm bảo text2 là chuỗi ngắn hơn để tối ưu bộ nhớ
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        # dp[j] = LCS của text1[:i] và text2[:j]
        dp = [0] * (n + 1)

        # Duyệt từng ký tự của text1 từ trái sang phải
        for i in range(1, m + 1):
            prev = 0  # prev = dp[i-1][j-1]
            for j in range(1, n + 1):
                temp = dp[j]  # lưu dp[i-1][j] trước khi bị ghi đè

                if text1[i - 1] == text2[j - 1]:
                    # Ký tự giống nhau → kéo dài LCS
                    dp[j] = prev + 1
                else:
                    # Ký tự khác nhau → chọn phương án tốt hơn
                    dp[j] = max(dp[j], dp[j - 1])

                # Cập nhật prev cho cột tiếp theo
                prev = temp

        # dp[n] là LCS của toàn bộ 2 chuỗi
        return dp[n]


# ------------------ CHẠY TEST ------------------
if __name__ == "__main__":
    sol = SolutionLeftToRight()
    text1 = "abcde"
    text2 = "ace"
    print("LCS (Left → Right):", sol.longestCommonSubsequence(text1, text2))
