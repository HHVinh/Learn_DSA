class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i]: độ dài LCS kết thúc tại text1[i]
        dp = [0] * len(text1)

        longest = 0  # Lưu độ dài LCS lớn nhất tìm được

        # Duyệt từng ký tự trong text2
        for c in text2:
            cur_length = 0  # Lưu giá trị dp lớn nhất bên trái (trước i)

            # Duyệt từng ký tự trong text1
            for i, val in enumerate(dp):
                # Nếu dp[i] lớn hơn cur_length
                # => cập nhật cur_length (di chuyển sang phải)
                if cur_length < val:
                    cur_length = val

                # Nếu ký tự khớp nhau
                elif c == text1[i]:
                    dp[i] = cur_length + 1   # Cập nhật LCS mới tại vị trí i
                    longest = max(longest, dp[i])  # Cập nhật kết quả

        return longest


# ====== TEST CHẠY TRONG VS CODE ======
if __name__ == "__main__":
    sol = Solution()

    text1 = "abcde"
    text2 = "ace"
    print(sol.longestCommonSubsequence(text1, text2))  # 3

    text1 = "abc"
    text2 = "abc"
    print(sol.longestCommonSubsequence(text1, text2))  # 3

    text1 = "abc"
    text2 = "def"
    print(sol.longestCommonSubsequence(text1, text2))  # 0
