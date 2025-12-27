class SolutionRightToLeft:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Đảm bảo text2 là chuỗi ngắn hơn để tối ưu bộ nhớ
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)

        # dp[j] = LCS của text1[i:] và text2[j:]
        dp = [0] * (n + 1)

        # Duyệt text1 từ phải sang trái
        for i in range(m - 1, -1, -1):
            prev = 0  # prev = dp[i+1][j+1]
            # Duyệt text2 từ phải sang trái
            for j in range(n - 1, -1, -1):
                temp = dp[j]  # lưu dp[i+1][j]

                if text1[i] == text2[j]:
                    # Ký tự giống nhau → kéo dài LCS
                    dp[j] = 1 + prev
                else:
                    # Ký tự khác nhau → chọn tốt hơn
                    dp[j] = max(dp[j], dp[j + 1])

                # Cập nhật prev cho cột tiếp theo
                prev = temp

        # dp[0] là LCS của toàn bộ 2 chuỗi
        return dp[0]


# ------------------ CHẠY TEST ------------------
if __name__ == "__main__":
    sol = SolutionRightToLeft()
    text1 = "abcde"
    text2 = "ace"
    print("LCS (Right → Left):", sol.longestCommonSubsequence(text1, text2))
