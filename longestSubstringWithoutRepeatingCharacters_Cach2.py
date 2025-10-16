class Solution:
    # Cách 2: Dùng dict để lưu vị trí index cuối cùng của ký tự
    def lengthOfLongestSubstring2(self, s: str) -> int:
        mapDict = {}                 # Dictionary lưu {ký tự: vị trí index gần nhất}
        res = 0                      # Biến lưu kết quả
        l, n = 0, len(s)             # Con trỏ trái và độ dài chuỗi

        for r in range(n):           # Duyệt con trỏ phải r
            if s[r] in mapDict:      # Nếu ký tự đã xuất hiện
                # Dịch con trỏ trái l sang bên phải của vị trí cũ (nếu cần)
                l = max(l, mapDict[s[r]] + 1)
            mapDict[s[r]] = r        # Cập nhật vị trí mới nhất của ký tự
            res = max(res, r - l + 1)# Cập nhật độ dài lớn nhất
        return res

if __name__ == "__main__":
    s = input("Nhập chuỗi cần kiểm tra: ")
    sol = Solution()
    print("Độ dài substring không lặp (Cách 1 - set):", sol.lengthOfLongestSubstring(s))
    print("Độ dài substring không lặp (Cách 2 - dict):", sol.lengthOfLongestSubstring2(s))

