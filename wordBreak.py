from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Chuyển wordDict sang set để kiểm tra tồn tại O(1)
        wordSet = set(wordDict)

        # Độ dài lớn nhất của 1 từ trong dictionary
        # Dùng để giới hạn số lần kiểm tra (tối ưu)
        maxLen = max(len(word) for word in wordDict)

        n = len(s)

        # dp[i] = True nếu s[0:i] (từ đầu đến i-1) chia được hợp lệ
        dp = [False] * (n + 1)

        # Chuỗi rỗng luôn chia được
        dp[0] = True

        # Duyệt từng vị trí kết thúc i của chuỗi
        for i in range(1, n + 1):

            # l là độ dài của từ đang thử cắt ở CUỐI chuỗi s[0:i]
            for l in range(1, maxLen + 1):

                # Nếu l quá dài → cắt vượt quá đầu chuỗi → bỏ qua
                if i - l < 0:
                    continue

                # Kiểm tra:
                # 1. dp[i-l] == True  → phần trước chia được
                # 2. s[i-l:i] nằm trong wordSet → từ cuối hợp lệ
                if dp[i - l] and s[i - l:i] in wordSet:
                    dp[i] = True      # s[0:i] chia được
                    break             # dừng sớm, không cần kiểm tra nữa

        # Kết quả là dp[n] (toàn bộ chuỗi)
        return dp[n]


# =========================
# Code test để chạy VS Code
# =========================
if __name__ == "__main__":
    sol = Solution()

    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(sol.wordBreak(s1, wordDict1))  # True

    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(sol.wordBreak(s2, wordDict2))  # True

    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(sol.wordBreak(s3, wordDict3))  # False
