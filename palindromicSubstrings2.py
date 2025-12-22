class Solution:

    def countSubstrings(self, s: str) -> int:
        res = 0                              # Biến đếm tổng số chuỗi con đối xứng

        for i in range(len(s)):              # Duyệt từng vị trí trong chuỗi
            res += self.countPali(s, i, i)   # Đếm palindrome lẻ (tâm tại i)
            res += self.countPali(s, i, i+1) # Đếm palindrome chẵn (tâm giữa i và i+1)

        return res                           # Trả về tổng số palindrome tìm được

    def countPali(self, s, l, r):
        res = 0                              # Đếm số palindrome với cặp tâm (l, r)

        # Mở rộng sang trái và phải miễn là còn trong chuỗi và 2 ký tự bằng nhau
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1                         # Mỗi lần match là tìm được 1 palindrome
            l -= 1                           # Mở rộng sang trái
            r += 1                           # Mở rộng sang phải

        return res                           # Trả về số palindrome từ tâm này


# ================== PHẦN CHẠY TRÊN VS CODE ==================
if __name__ == "__main__":
    solution = Solution()

    s1 = "abc"
    s2 = "aaa"
    s3 = "abba"

    print("Input:", s1, "=> Output:", solution.countSubstrings(s1))
    print("Input:", s2, "=> Output:", solution.countSubstrings(s2))
    print("Input:", s3, "=> Output:", solution.countSubstrings(s3))
