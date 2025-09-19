class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):                 # nếu s dài hơn t thì chắc chắn không thể là subsequence
            return False
        
        ss, tt = 0, 0                       # ss duyệt chuỗi s, tt duyệt chuỗi t
        while ss < len(s) and tt < len(t):  # khi chưa duyệt hết cả hai chuỗi
            if s[ss] == t[tt]:              # nếu ký tự khớp
                ss += 1                     # tiến con trỏ của s
                tt += 1                     # tiến con trỏ của t
            else:
                tt += 1                     # nếu không khớp thì chỉ tiến con trỏ t
        return ss == len(s)                 # nếu duyệt hết s thì s là subsequence của t

# ---- Chạy chương trình ----
if __name__ == "__main__":
    s = input("Nhập chuỗi s: ")             # chuỗi cần kiểm tra
    t = input("Nhập chuỗi t: ")             # chuỗi gốc
    sol = Solution()
    if sol.isSubsequence(s, t):
        print(f'"{s}" là subsequence của "{t}"')
    else:
        print(f'"{s}" KHÔNG phải subsequence của "{t}"')
